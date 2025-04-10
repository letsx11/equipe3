import pygame as pg

class Player(pg.sprite.Sprite):
    
    # Inicialização da classe com atributos de posição, escala da imagem, velocidade
    def __init__(self, x, y, escala, velocidade):
        pg.sprite.Sprite.__init__(self)
        self.vidas = 3
        self.direcao = 1
        self.virar = True
        self.velocidade = velocidade
        self.lista_animacao = []
        self.indiceframe = 0
        self.acao = 0
        self.update_time = pg.time.get_ticks()
        listatemp = []
        
        #Armazenamento de todos os frames da animação em que o personagem esta parado no indice 0 da lista de animação
        for i in range(2):
            img = pg.image.load(f'imagens/spritesheet/Idle/{i}.png')
            img = pg.transform.scale(img, (int(img.get_width()*escala), int(img.get_height()*escala)))
            listatemp.append(img)
        self.lista_animacao.append(listatemp)
        listatemp=[]

        # Armazenamento de todos os frames da animação em que o personagem esta correndo no indice 1 da lista de animação
        for i in range(5):
            img = pg.image.load(f'imagens/spritesheet/Run/{i}.png')
            img = pg.transform.scale(img, (int(img.get_width()*escala), int(img.get_height()*escala)))
            listatemp.append(img)
        self.lista_animacao.append(listatemp)
        listatemp=[]
        self.imagem = self.lista_animacao[self.acao][self.indiceframe]
        self.rect = self.imagem.get_rect()
        self.rect.center = (x,y)
        
    # Movimento do personagem
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
        
    # Percorre os quadros da animação do personagem
    def update_animation(self):
        # Intervalo de tempo entre os quadros de animação (100 milisegundos)
        cooldown = 100
        self.imagem = self.lista_animacao[self.acao][self.indiceframe]
        if pg.time.get_ticks()-self.update_time > cooldown:
            self.update_time = pg.time.get_ticks()
            self.indiceframe += 1
        # Caso a lista chegue ao fim, retorna ao começo e inicia o loop da animação
        if self.indiceframe >= len(self.lista_animacao[self.acao]):
            self.indiceframe = 0
            
    # Passagem de uma ação para a outra (personagem parado -> personagem correndo e vice-versa)
    def update_action(self, nova_acao):
        if nova_acao != self.acao:
            self.acao = nova_acao
            self.indiceframe = 0
            self.update_time = pg.time.get_ticks()
            
    # Impressão do personagem 
    def draw(self, tela):
       tela.blit(pg.transform.flip(self.imagem, self.virar, False), self.rect)
        
    # Perda de vida 
    def lose_lives(self):
        self.vidas-=1
