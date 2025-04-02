import pygame as pg
import sys
from player import Player

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
fonte_botao = pg.font.Font(None, 60)

# Fundo da tela inicial 
escala = 5 # Escala para pixelar as imagens (quanto maior, mais pixelado)
fundo_tela_inicial = pg.image.load("imagens/background.jpg")
fundo_tela_inicial = pg.transform.scale(fundo_tela_inicial, (LARGURA, ALTURA))
fundo_reduzido_inicial = pg.transform.scale(fundo_tela_inicial, (LARGURA // escala, ALTURA // escala ))
fundo_tela_incial = pg.transform.scale(fundo_reduzido_inicial, (LARGURA, ALTURA))

# Fundo de tela do jogo 
fundo_tela_jogo = pg.image.load("imagens/Ladeira_da_Misericorida_Olinda.webp")
fundo_tela_jogo = pg.transform.scale(fundo_tela_jogo, (LARGURA, ALTURA))
fundo_reduzido_jogo = pg.transform.scale(fundo_tela_jogo, (LARGURA // escala, ALTURA // escala ))
fundo_tela_jogo = pg.transform.scale(fundo_reduzido_jogo, (LARGURA, ALTURA))

# Botões
texto_botao = fonte_botao.render("Iniciar Jogo", True, BRANCO)
texto_botao_sair = fonte_botao.render("Sair", True, BRANCO)
texto_botao_reiniciar = fonte_botao.render("Jogar Novamente", True, BRANCO)

botao_rect = pg.Rect(0, 0, texto_botao.get_width() + 40, texto_botao.get_height() + 20)
botao_rect.center = (LARGURA // 2, ALTURA // 2 - 20)
botao_sair_rect = pg.Rect(0, 0, texto_botao_sair.get_width() + 40, texto_botao_sair.get_height() + 20)
botao_sair_rect.center = (LARGURA // 2, ALTURA // 2 + 120)
botao_reiniciar_rect = pg.Rect(0,0, texto_botao_reiniciar.get_width() + 40, texto_botao_reiniciar.get_height() + 20)
botao_reiniciar_rect.center = (LARGURA // 2, ALTURA // 2 + 220)

# Música 
pg.mixer.music.load("sons/marcelorossiter-voltei-recife-8e035859.mp3")
pg.mixer.music.set_volume(1)

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
            
        tela.blit(fundo_tela_incial, (0, 0))

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
    global vencedor
    global total_coletaveis  

    relogio = pg.time.Clock()
    tempo_restante = 60000  # 1 minuto 
    tempo_inicial = pg.time.get_ticks()
    fonte_tempo = pg.font.Font(None, 50)
    fonte_info = pg.font.Font(None, 40)

    FPS = 60
    jogador = Player(LARGURA // 2, ALTURA - 100, 2, 5)
    esquerda = direita = False

    total_coletaveis = 0  

    vencedor = False  
    rodando = True  
    while rodando:
        relogio.tick(FPS)

        # Tempo  
        tempo_atual = pg.time.get_ticks()
        tempo_decorrido = tempo_atual - tempo_inicial
        tempo_restante -= tempo_decorrido  
        tempo_inicial = tempo_atual  
        qtd_agua = 0 # Bebidas 
        qtd_beats = 0
        qtd_vida = 3


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
        
        # Verifica se o tempo acabou
        if tempo_restante <= 0 or jogador.vidas == 0:  
            vencedor = True 
            rodando = False  # Sai do loop

        # Aqui adiciona condição para verificar se as vidas acabaram

        # Atualizar tela do jogo
        tela.blit(fundo_tela_jogo, (0, 0))
        jogador.move(esquerda, direita, LARGURA)
        jogador.draw(tela)

        pg.draw.rect(tela, VERMELHO, (((LARGURA // 2) - 50), 0, 100, 35), border_radius=3)  
        tempo_segundos = max (0,tempo_restante // 1000)
        texto_tempo = fonte_tempo.render(f"00:{tempo_segundos}", True, CINZA_ESCURO)  
        rect_tempo = texto_tempo.get_rect(center=(LARGURA // 2,  19))
        tela.blit(texto_tempo, rect_tempo.topleft)

        # Retângulo amarelo no canto superior direito
        pg.draw.rect(tela, (215, 215, 0), (10, 10, 160, 70), border_radius=10)
        pg.draw.rect(tela, (255, 165, 0), (10, 10, 160, 70), 3, border_radius=10)  # Borda laranja
        sombra = pg.Surface((160, 70), pg.SRCALPHA)
        sombra.fill((255, 255, 0, 100))  # Sombra amarela translúcida
        tela.blit(sombra, (12, 12))

        texto_beats = fonte_info.render(f"Beats: {qtd_beats}", True, CINZA_ESCURO)
        texto_agua = fonte_info.render(f"Agua: {qtd_agua}", True, CINZA_ESCURO)
        tela.blit(texto_beats, (20, 20))
        tela.blit(texto_agua, (20, 45))

        pg.display.update()
    
    tela_final(vencedor, total_coletaveis)
    return vencedor, total_coletaveis   

# Tela final
def tela_final(vencedor, total_coletaveis):
    rodando = True
    fonte_mensagem = pg.font.Font(None, 40)  
    largura_mensagem = 500  
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
                
        tela.blit(fundo_tela_incial, (0, 0))

        # Definir mensagem conforme resultado
        if vencedor:
            mensagem = f"Parabéns! Você coletou {total_coletaveis} itens!"      
        else:
            mensagem = "Infelizmente suas vidas acabaram antes do tempo."

        retangulo_mensagem = pg.Rect(0, 0, largura_mensagem, altura_mensagem)
        retangulo_mensagem.center = (LARGURA // 2, ALTURA // 2)
        pg.draw.rect(tela, CINZA_ESCURO, retangulo_mensagem, border_radius=15)  
        pg.draw.rect(tela, BRANCO, retangulo_mensagem.inflate(-10, -10), border_radius=15)  
       
        texto_mensagem = fonte_mensagem.render(mensagem, True, CINZA_ESCURO)
        rect_mensagem = texto_mensagem.get_rect(center=(LARGURA // 2, ALTURA//2))
        tela.blit(texto_mensagem, rect_mensagem)


        cor_botao_reiniciar = VERDE if botao_reiniciar_rect.collidepoint(mouse_pos) else VERDE_ESCURO
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
                if botao_reiniciar_rect.collidepoint(evento.pos):
                    jogo()
                if botao_sair_rect.collidepoint(evento.pos): # Sair se clicar em sair 
                    pg.quit()
                    sys.exit()

        # Botão reiniciar com efeito 
        pg.draw.rect(tela, CINZA_ESCURO, botao_reiniciar_rect.inflate(10, 10), border_radius=15)  
        pg.draw.rect(tela, cor_botao_reiniciar, botao_reiniciar_rect, border_radius=15)
        tela.blit(texto_botao_reiniciar, texto_botao_reiniciar.get_rect(center=botao_reiniciar_rect.center))

        # Botão sair com efeito 
        pg.draw.rect(tela, CINZA_ESCURO, botao_sair_rect.inflate(10, 10), border_radius=15)  
        pg.draw.rect(tela, cor_botao_sair, botao_sair_rect, border_radius=15)
        tela.blit(texto_botao_sair, texto_botao_sair.get_rect(center=botao_sair_rect.center))

        pg.display.flip()

# Executar jogo
if __name__ == "__main__":
    tela_inicial()
    vencedor, total_coletaveis = jogo()  
    tela_final(vencedor, total_coletaveis)  

