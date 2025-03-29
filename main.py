import pygame as pg
from player import Player

pg.init()

largura = 600
altura = 800
tela = pg.display.set_mode((largura, altura))
pg.display.set_caption('Carnagame')

relogio = pg.time.Clock()
FPS = 60

def draw_background():
    imagemfundo = pg.image.load('imagem/background.jpg')
    tela.blit(imagemfundo, (0,0))

andaresquerda = False
andardireita = False

jogador = Player(largura/2, altura-100, 2, 3)

rodando = True


while rodando:

    relogio.tick(FPS)
    draw_background()
    jogador.draw(tela)
    jogador.move(andaresquerda, andardireita, largura)

    for event in pg.event.get():
        if(event.type == pg.QUIT):
            rodando = False   
        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_ESCAPE):
                rodando = False
            if(event.key == pg.K_a):
                andaresquerda = True
            if(event.key == pg.K_d):
                andardireita = True
        if(event.type == pg.KEYUP):
            if(event.key == pg.K_a):
                andaresquerda = False
            if(event.key == pg.K_d):
                andardireita = False

            
            
        

        

    pg.display.update()
    

pg.quit()