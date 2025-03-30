import pygame as pg
import sys

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
fundo_tela_incial = pg.image.load("olinda-carnaval.webp")
fundo_tela_incial = pg.transform.scale(fundo_tela_incial, (LARGURA, ALTURA))
fundo_reduzido_inicial = pg.transform.scale(fundo_tela_incial, (LARGURA // escala, ALTURA // escala ))
fundo_tela_incial = pg.transform.scale(fundo_reduzido_inicial, (LARGURA, ALTURA))

# Fundo de tela do jogo 
fundo_tela_jogo = pg.image.load("Ladeira_da_Misericorida_Olinda.webp")
fundo_tela_jogo = pg.transform.scale(fundo_tela_jogo, (LARGURA, ALTURA))
fundo_reduzido_jogo = pg.transform.scale(fundo_tela_jogo, (LARGURA // escala, ALTURA // escala ))
fundo_tela_jogo = pg.transform.scale(fundo_reduzido_jogo, (LARGURA, ALTURA))

# Botões
texto_botao = fonte_botao.render("Clique aqui para iniciar", True, BRANCO)
texto_botao_sair = fonte_botao.render("Sair", True, BRANCO)

botao_rect = pg.Rect(0, 0, texto_botao.get_width() + 40, texto_botao.get_height() + 20)
botao_rect.center = (LARGURA // 2, ALTURA // 2 - 20)
botao_sair_rect = pg.Rect(0, 0, texto_botao_sair.get_width() + 40, texto_botao_sair.get_height() + 20)
botao_sair_rect.center = (LARGURA // 2, ALTURA // 2 + 120)

# Música 
pg.mixer.music.load("marcelorossiter-voltei-recife-8e035859.mp3")
pg.mixer.music.set_volume(1)


# Classe do jogador
class Player(pg.sprite.Sprite):
    def __init__(self, x, y, escala, velocidade):
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load('imagem player.jpg')
        self.velocidade = velocidade
        self.virar = False
        self.direcao = 1
        self.imagem = pg.transform.scale(img, (int(img.get_width()*escala), int(img.get_height()*escala)))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x, y)
    
    def move(self, andaresquerda, andardireita, largura):
        dx = 0
        if(self.rect.x <= 0):
            self.rect.x = 0
        if(self.rect.x >= largura - self.imagem.get_width()):
            self.rect.x = largura - self.imagem.get_width()
        if(andaresquerda):
            dx = -self.velocidade
            self.virar = True
            self.direcao = -1
        if(andardireita):
            dx = self.velocidade
            self.virar = False
            self.direcao = 1
        self.rect.x += dx
    
    def draw(self):
        tela.blit(pg.transform.flip(self.imagem, self.virar, False), self.rect)

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
            if evento.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if evento.type == pg.MOUSEBUTTONDOWN:
                if botao_rect.collidepoint(evento.pos):
                    pg.mixer.music.stop()
                    return  
                if botao_sair_rect.collidepoint(evento.pos):
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
    relogio = pg.time.Clock()
    FPS = 60
    jogador = Player(LARGURA//2, ALTURA-100, 2, 5)
    esquerda = direita = False
    
    rodando = True
    while rodando:
        relogio.tick(FPS)
        
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                rodando = False
            if evento.type == pg.KEYDOWN:
                if evento.key == pg.K_ESCAPE:
                    return  
                if evento.key == pg.K_a:
                    esquerda = True
                if evento.key == pg.K_d:
                    direita = True
            if evento.type == pg.KEYUP:
                if evento.key == pg.K_a:
                    esquerda = False
                if evento.key == pg.K_d:
                    direita = False
        
        tela.blit(fundo_tela_jogo, (0, 0))
        jogador.move(esquerda, direita, LARGURA)
        jogador.draw()
        pg.display.update()
    
    pg.quit()
    sys.exit()

# Executar jogo
if __name__ == "__main__":
    tela_inicial()
    jogo()
