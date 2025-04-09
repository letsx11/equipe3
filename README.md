# NaLadeira - Jogo 2D em Python com Pygame: 

## Membros da equipe:
- Andrya Gabryelle Santos de Araujo
- Clara Dias Guimarães
- Gabriela Alves Fernandes Vieira
- Gabriela Marques de Rangel Moreira
- Iago Lopes da Silva
- Leticia Santos Xavier






## Descrição do Jogo:
O jogo é dividido em três partes: a primeira delas é o menu inicial, onde o jogador pode clicar em "Iniciar Jogo", o que o levará à segunda parte, na qual o jogo propriamente dito acontece, ou clicar em "Sair" para fechar o jogo. Lembrando que, a qualquer momento, caso o jogador queira abandonar o jogo, a tecla "ESC" pode ser pressionada.

Ao chegar à segunda parte, haverá bebidas caindo de cima da tela, sendo elas: (bebidas). O objetivo é pegar a maior quantidade de bebidas possível dentro de (tempo padrão do jogo), exceto (exceção), pois, a cada uma coletada, uma das três vidas é retirada.

Além disso, cada bebida tem seu "poder especial". A latinha de Beats, por exemplo, aumenta a velocidade do jogador em (aumento da vel), já a água aumenta o seu tempo de jogo em (aumento de tempo).

Há duas formas de o jogo terminar: uma é se o jogador perder as três vidas, e a outra é se o tempo limite expirar. Qualquer uma das duas o levará à terceira parte, que é a tela final. Caso o jogo termine devido à perda total das vidas, aparecerá apenas uma mensagem informando que o jogador perdeu. Caso contrário, será exibido o total de bebidas que ele conseguiu pegar. E, para as duas opções, no fim da tela terá: "Sair" ou "Jogar Novamente". 

## Capturas de Tela
### Tela Inicial
![Screenshot 2025-04-09 135918](https://github.com/user-attachments/assets/0542799a-f2dd-4c15-bd20-ad99e8c746fc)
### Tela de Jogo
![Screenshot 2025-04-09 140000](https://github.com/user-attachments/assets/de116bd5-132d-496a-8ca0-1fe85509ee98)
### Telas finais
![Screenshot 2025-04-09 140151](https://github.com/user-attachments/assets/10d6f05a-44f9-46e3-9f12-4c64ec7be804)
![Screenshot 2025-04-09 140234](https://github.com/user-attachments/assets/1c43c99e-923c-4907-b3b8-5f58f15bb4c8)

## Arquitetura do Projeto
- main.py: Trata-se do módulo central do jogo, o qual nele junta todas a estruturas assim fazendo com que o jogo funcione. 
- player.py: Esse arquivo complementa o personagem principal do jogo, trazendo suas características e movimentações presentes no jogo.
- coletaveis.py: Comporta a classe dos 3 objetos coletáveis (água, beats e pitu), essenciais para a dinamica e funcionamento do jogo. 
- fontes/: Pasta que armazena a fonte dos textos presentes no jogo.
- imagens/: Pasta com toda a parte gráfica do jogo (capas, coletáveis, vidas, personagem)
- sons/: Pasta com todo os áudios presentes (música inicial, sons 





