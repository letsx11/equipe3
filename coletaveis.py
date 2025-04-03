import pygame as pg

# Classe coletáveis (Super classe)
class Coletavel(pg.sprite.Sprite):
    def __init__(self, x, y, velocidade, tipo):
        super().__init__()
        
        if tipo == "agua":
            self.image = pg.image.load("agua.png")  # Imagem água
        elif tipo == "beats":
            self.image = pg.image.load("beats.png")  # Imagem beats
        else:
            self.image = pg.image.load("pitu.png") # Imagem pitu

        self.image = pg.transform.scale(self.image, (40, 50))  
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.velocidade = velocidade
        self.tipo = tipo  # Salva os tipos

    def update(self):
        self.rect.y += self.velocidade  
        if self.rect.top > ALTURA:  # Remove se sair da tela
            self.kill()
