import pygame as pg
#Criação da classe do player, com seus respectivos métodos e atributos.
class Player(pg.sprite.Sprite):
    #Inicializando a classe com atributos de posição, escala da imagem, velocidade e etc...
    def __init__(self, x, y, escala, velocidade):
        pg.sprite.Sprite.__init__(self)
        img = pg.image.load(f'imagens/0.png')
        self.vidas = 3
        self.direcao = 1
        self.virar = True
        self.velocidade = velocidade
        self.imagem = pg.transform.scale(img, (int(img.get_width()*escala), int(img.get_height()*escala)))
        self.rect = self.imagem.get_rect()
        self.rect.center = (x,y)
    #Método responsável pelo movimento do personagem.
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
    #Método que faz com que o personagem seja impresso na tela do jogo.
    def draw(self, tela):
       tela.blit(pg.transform.flip(self.imagem, self.virar, False), self.rect)
    #Metódo responsavel por diminuir a vida do personagem.
    def lose_lives(self):
        self.vidas-=1
        

    

