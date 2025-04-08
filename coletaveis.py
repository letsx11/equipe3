import pygame as pg

LARGURA, ALTURA = 700, 600

# Classe coletáveis (Super classe)
class Coletavel(pg.sprite.Sprite) :
    def __init__(self, x, y, velocidade, tipo) :
        super().__init__()
        
        if tipo == "agua" :
            # Imagem água
            self.image = pg.image.load("imagens/agua.png")  
            self.image = pg.transform.scale(self.image, (40, 45))  
        elif tipo == "beats" :
            # Imagem beats
            self.image = pg.image.load("imagens/beats.png")  
            self.image = pg.transform.scale(self.image, (20, 35))  
        else :
            # Imagem pitu
            self.image = pg.image.load("imagens/pitu.png") 
            self.image = pg.transform.scale(self.image, (25, 35))  

        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidade = velocidade
        self.tipo = tipo  # Salva os tipos

    def update(self) :
        self.rect.y += self.velocidade  
        # Remove se sair da tela
        if self.rect.top > ALTURA :  
            self.kill()
