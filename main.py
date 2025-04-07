import pygame as pg
import sys
import random
from player import Player 
from coletaveis import Coletavel

pg.init()
pg.mixer.init()

# Configurações da tela
LARGURA, ALTURA = 700, 600
tela = pg.display.set_mode((LARGURA, ALTURA))
pg.display.set_caption("Carnagame")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERMELHO_ESCURO = (180, 0, 0)
VERDE = (0, 255, 0)
VERDE_ESCURO = (0, 180, 0)
CINZA_ESCURO = (50, 50, 50)

# Fonte 
fonte = pg.font.Font('fontes/fonte3.ttf', 30)

# Fundo da tela inicial 
fundo_tela_inicial = pg.image.load("imagens/capa_inicial.png")
fundo_tela_inicial = pg.transform.scale(fundo_tela_inicial, (LARGURA, ALTURA))

# Fundo de tela do jogo 
fundo_tela_jogo = pg.image.load("imagens/ladeira_olinda.png")
fundo_tela_jogo = pg.transform.scale(fundo_tela_jogo, (LARGURA, ALTURA))

# Botões
texto_botao = fonte.render("Iniciar", True, BRANCO)
texto_botao_sair = fonte.render("Sair", True, BRANCO)
texto_botao_sair_final = fonte.render("Sair", True, BRANCO)
texto_botao_reiniciar = fonte.render(f"Jogar Novamente", True, BRANCO)

botao_rect = pg.Rect(0, 0, texto_botao.get_width() + 40, texto_botao.get_height() + 20)
botao_rect.center = (300, 551)
botao_sair_rect = pg.Rect(0, 0, texto_botao_sair.get_width() + 40, texto_botao_sair.get_height() + 20)
botao_sair_rect.center = (410, 551)
botao_sair_final_rect = pg.Rect(0, 0, texto_botao_sair_final.get_width() + 40, texto_botao_sair.get_height() + 20)
botao_sair_final_rect.center = (LARGURA/2, 500)
botao_reiniciar_rect = pg.Rect(0,0, texto_botao_reiniciar.get_width() + 40, texto_botao_reiniciar.get_height() + 20)
botao_reiniciar_rect.center = (353, 551)

# Música 
pg.mixer.music.load("sons/marcelorossiter-voltei-recife-8e035859.mp3")
pg.mixer.music.set_volume(1)

# Função vidas
imagem_vida = pg.image.load('imagens/coracao_vida.png').convert_alpha()
imagem_vida = pg.transform.scale(imagem_vida, (40, 40))  
imagem_sem_vida = pg.image.load('imagens/coracao_sem_vida.png').convert_alpha()
imagem_sem_vida = pg.transform.scale(imagem_sem_vida, (40, 40))  

def desenhar_vidas(qtd_vida):
    for i in range(3):
        x = LARGURA - (i + 1) * 45
        y = 10
        if i < qtd_vida:
            tela.blit(imagem_vida, (x, y))
        else:
            tela.blit(imagem_sem_vida, (x, y))

# Tela inicial
def tela_inicial():
    rodando = True
    pg.mixer.music.play(-1)
    while rodando:
        mouse_pos = pg.mouse.get_pos()

        # Detectar se o mouse está sobre os botões
        cor_botao = VERDE if botao_rect.collidepoint(mouse_pos) else VERDE_ESCURO
        cor_botao_sair = VERMELHO if botao_sair_rect.collidepoint(mouse_pos) else VERMELHO_ESCURO

        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN: # Sair se apertar em ESC
                if evento.key == pg.K_ESCAPE:   
                    pg.quit()
                    sys.exit()
            if evento.type == pg.QUIT: # Sair se fechar o pygame 
                pg.quit()
                sys.exit()
            if evento.type == pg.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(evento.pos):
                    pg.mixer.music.stop()
                    return  
                if botao_sair_rect.collidepoint(evento.pos): # Sair se clicar em sair 
                    pg.quit()
                    sys.exit()
            
        tela.blit(fundo_tela_inicial, (0, 0))

        # Botão iniciar com efeito 
        pg.draw.rect(tela, CINZA_ESCURO, botao_rect.inflate(10, 10), border_radius=15)  
        pg.draw.rect(tela, cor_botao, botao_rect, border_radius=15)
        tela.blit(texto_botao, texto_botao.get_rect(center=botao_rect.center))

        # Botão sair com efeito 
        pg.draw.rect(tela, CINZA_ESCURO, botao_sair_rect.inflate(10, 10), border_radius=15)  
        pg.draw.rect(tela, cor_botao_sair, botao_sair_rect, border_radius=15)
        tela.blit(texto_botao_sair, texto_botao_sair.get_rect(center=botao_sair_rect.center))

        pg.display.flip()
    
# Função principal do jogo
def jogo():

    coletaveis = pg.sprite.Group()
    tempo_ultimo_spawn = pg.time.get_ticks()
    intervalo_spawn = 1000  # Tempo entre cada spawn (1 segundos)

    global vencedor
    global total_coletaveis  

    relogio = pg.time.Clock()
    tempo_restante = 30000  # 30 segundos 
    tempo_inicial = pg.time.get_ticks()

    FPS = 60
    jogador = Player(LARGURA // 2, ALTURA - 100, 1, 5)
    esquerda = direita = False

    total_coletaveis = 0  
    qtd_agua = 0 
    qtd_beats = 0
    qtd_vida = 3

    vencedor = False  
    rodando = True  

    while rodando:
        relogio.tick(FPS)

        # Tempo  
        tempo_atual = pg.time.get_ticks()
        tempo_decorrido = tempo_atual - tempo_inicial
        tempo_restante -= tempo_decorrido  
        tempo_inicial = tempo_atual  

        if tempo_restante == 25:
            Coletavel.velocidade += 10
            intervalo_spawn == 1500
        elif tempo_restante == 15:
            Coletavel.velocidade += 15
            intervalo_spawn = 500
        elif tempo_restante == 10:
            intervalo_spawn = 200
            Coletavel.velocidade += 15


        # Cria novos objetos caindo
        if pg.time.get_ticks() - tempo_ultimo_spawn > intervalo_spawn:
            x_random = random.randint(0, LARGURA - 40)

            # Escolhe aleatoriamente qual coletável vai ser
            tipo_coletavel = random.choice(["agua", "beats", "pitu"])
            
            novo_coletavel = Coletavel(x_random, -50, 5, tipo_coletavel)  
            coletaveis.add(novo_coletavel)  
            tempo_ultimo_spawn = pg.time.get_ticks()
        
        coletaveis.update()

        # Processamento de eventos
        for evento in pg.event.get():
            if evento.type == pg.QUIT:  
                pg.quit()
                sys.exit()
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_ESCAPE:  
                    pg.quit()
                    sys.exit()
                if evento.key == pg.K_a: 
                    esquerda = True
                if evento.key == pg.K_d:
                    direita = True
            if evento.type == pg.KEYUP:
                if evento.key == pg.K_a:
                    esquerda = False
                if evento.key == pg.K_d:
                    direita = False
        
        # Verifica se o player coletou algum item
        coletados = pg.sprite.spritecollide(jogador, coletaveis, True)
        for item in coletados:
            if item.tipo == "agua":
                tempo_restante += 1000 # Aumenta tempo em 1 segundo
                qtd_agua += 1  # Aumenta a contagem de água
            elif item.tipo == "beats":
                jogador.velocidade += 1 # Aumenta velocidade
                qtd_beats += 1  # Aumenta a contagem de beats
            else:
                qtd_vida -= 1 
                if qtd_vida == 0:
                    rodando = False
        
        total_coletaveis = qtd_agua + qtd_beats
                
        # Verifica se o tempo acabou
        if tempo_restante <= 0:  
            vencedor = True 
            rodando = False  # Sai do loop

        # Atualizar tela do jogo
        tela.blit(fundo_tela_jogo, (0, 0))
        coletaveis.draw(tela)
        jogador.update_animation()
        jogador.draw(tela)
        if esquerda or direita:
            jogador.update_action(1)
        else:
            jogador.update_action(0) 
        jogador.move(esquerda, direita, LARGURA)

        # Contagem tempo
        pg.draw.rect(tela, VERMELHO, (((LARGURA // 2) - 60), 0, 120, 35), border_radius=3)  
        pg.draw.rect(tela, (255, 165, 0), (((LARGURA // 2) - 60), 0, 120, 35), 3, border_radius=3)  # Borda laranja
        tempo_segundos = max (0,tempo_restante // 1000)
        texto_tempo = fonte.render(f"00:{tempo_segundos}", True, BRANCO)  
        rect_tempo = texto_tempo.get_rect(center=(LARGURA // 2,  15))
        tela.blit(texto_tempo, rect_tempo.topleft)

        # Contagem de itens coletados 
        pg.draw.rect(tela, VERMELHO, (10, 0, 190, 70), border_radius=3)
        pg.draw.rect(tela, (255, 165, 0), (10, 0, 190, 70), 3, border_radius=3)  # Borda laranja
        sombra = pg.Surface((160, 70), pg.SRCALPHA)
        tela.blit(sombra, (12, 12))

        texto_beats = fonte.render(f"Beats:{qtd_beats}", True, BRANCO)
        texto_agua = fonte.render(f"Agua:{qtd_agua}", True, BRANCO)
        tela.blit(texto_beats, (15, 0))
        tela.blit(texto_agua, (15, 30))

        desenhar_vidas(qtd_vida)
        
        pg.display.update()
    
    tela_final(vencedor, total_coletaveis)
    return vencedor, total_coletaveis   

# Tela final
def tela_final(vencedor, total_coletaveis):
    rodando = True 
    largura_mensagem = 600  
    altura_mensagem = 70

    while rodando:
        mouse_pos = pg.mouse.get_pos()
        for evento in pg.event.get():
            if evento.type == pg.QUIT:  
                pg.quit()
                sys.exit()
            if evento.type == pg.KEYDOWN and evento.key == pg.K_ESCAPE: 
                pg.quit()
                sys.exit() 
                
        tela.blit(fundo_tela_inicial, (0, 0))

        # Definir mensagem conforme resultado
        if vencedor:
            mensagem = f"Você coletou {total_coletaveis} itens!"      
        else:
            mensagem = "Suas vidas acabaram :/"

        retangulo_mensagem = pg.Rect(0, 0, largura_mensagem, altura_mensagem)
        retangulo_mensagem.center = (LARGURA // 2, ALTURA // 2)
        pg.draw.rect(tela, CINZA_ESCURO, retangulo_mensagem, border_radius=15)  
        pg.draw.rect(tela, BRANCO, retangulo_mensagem.inflate(-10, -10), border_radius=15)  
       
        texto_mensagem = fonte.render(mensagem, True, CINZA_ESCURO)
        rect_mensagem = texto_mensagem.get_rect(center=(LARGURA // 2, ALTURA//2))
        tela.blit(texto_mensagem, rect_mensagem)


        cor_botao_reiniciar = VERDE if botao_reiniciar_rect.collidepoint(mouse_pos) else VERDE_ESCURO
        cor_botao_sair = VERMELHO if botao_sair_final_rect.collidepoint(mouse_pos) else VERMELHO_ESCURO

        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN: # Sair se apertar em ESC
                if evento.key == pg.K_ESCAPE:   
                    pg.quit()
                    sys.exit()
            if evento.type == pg.QUIT: # Sair se fechar o pygame 
                pg.quit()
                sys.exit()
            if evento.type == pg.MOUSEBUTTONDOWN:
                if botao_reiniciar_rect.collidepoint(evento.pos):
                    jogo()
                if botao_sair_final_rect.collidepoint(evento.pos): # Sair se clicar em sair 
                    pg.quit()
                    sys.exit()

        # Botão reiniciar com efeito 
        pg.draw.rect(tela, CINZA_ESCURO, botao_reiniciar_rect.inflate(10, 10), border_radius=15)  
        pg.draw.rect(tela, cor_botao_reiniciar, botao_reiniciar_rect, border_radius=15)
        tela.blit(texto_botao_reiniciar, texto_botao_reiniciar.get_rect(center=botao_reiniciar_rect.center))

        # Botão sair com efeito 
        pg.draw.rect(tela, CINZA_ESCURO, botao_sair_final_rect.inflate(10, 10), border_radius=15)  
        pg.draw.rect(tela, cor_botao_sair, botao_sair_final_rect, border_radius=15)
        tela.blit(texto_botao_sair_final, texto_botao_sair_final.get_rect(center=botao_sair_final_rect.center))

        pg.display.flip()

# Executar jogo
if __name__ == "__main__":
    tela_inicial()
    vencedor, total_coletaveis = jogo()  
    tela_final(vencedor, total_coletaveis)  
