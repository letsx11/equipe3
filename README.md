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

Ao chegar à segunda parte, haverá bebidas caindo de cima da tela, sendo elas: água, beats e pitu. O objetivo é pegar a maior quantidade de bebidas possível dentro de 30 segundos, exceto a pitu, pois, a cada uma coletada, uma das três vidas é retirada.

Além disso, cada bebida tem seu "poder especial". A latinha de Beats, por exemplo, aumenta a velocidade do jogador em 0.5, já a água aumenta o seu tempo de jogo em 1 segundo.

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
- main.py: Arquivo principal do jogo, responsável por integrar todos os módulos e coordenar o funcionamento geral da aplicação.
- player.py: Define o personagem principal, incluindo suas características, animações e movimentações dentro do jogo.
- coletaveis.py: Contém a classe dos três itens coletáveis (água, beats e pitu), fundamentais para a mecânica e a dinâmica do jogo.
- fontes/: Diretório responsável por armazenar as fontes utilizadas nos textos do jogo.
- imagens/: Pasta que reúne todos os elementos gráficos do jogo, como capas, personagens, itens coletáveis e indicadores de vida.
- sons/: Diretório que guarda todos os arquivos de áudio do jogo, incluindo a música de abertura e os efeitos sonoros de coleta.
  
## Ferramentas 
- Pygame:
- Random:
- Sys:
- Time:
- VS code:
- Git Hub:
- Discord:
- Inteligencia Artificial:
- Photoshop:

## Divisão de tarefas
| **Integrate** | **Tarefas** |
| :---: | :--: |
| Andrya Araújo | Classe dos coletáveis; Criação dos sprites  |
| Clara Dias | Função principal do jogo; Organização do main |
| Iago Lopes | Classe do player; Implementação da coleta dos itens |
| Gabriela Alves | Interface tela inicial/final; Organização do main |
| Gabriela Marques | Classe dos coletáveis; Organização do main |
| Letícia Xavier | Interface tela inicial/final; GitHub e Relatório |

## Conceitos Utilizados:
- Classes e objetos: foram utilizados para definir estruturas e atribuir a elas características e funcionalidades específicas dentro do código, como a classe "player" e a classe "coletaveis".
- Condicionais: aplicadas ao longo de todo o projeto, permiti com que o jogo reaja de forma dinâmica às interações do usuário.
- Funções: responsáveis por organizar o código, separando suas funcionalidades de forma clara e eficiente.
- Laços de repetição: presentes em grande parte do código, são essenciais para garantir o fluxo contínuo e o funcionamento geral do jogo.
- Tuplas: utilizadas para armazenar dados fixos, como a definição de cores no formato RGB e a posição dos botões na interface.

## Desafios



