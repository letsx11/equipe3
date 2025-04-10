# NaLadeira - Jogo 2D em Python com Pygame: 

## Membros da equipe:
- Andrya Gabryelle Santos de Araujo;
- Clara Dias Guimarães;
- Gabriela Alves Fernandes Vieira;
- Gabriela Marques de Rangel Moreira;
- Iago Lopes da Silva;
- Leticia Santos Xavier.

## Descrição do Jogo:
O jogo é dividido em três partes: a primeira delas é o menu inicial, onde o jogador pode clicar em "Iniciar Jogo", o que o levará à segunda parte, na qual o jogo propriamente dito acontece, ou clicar em "Sair" para fechar o jogo. Lembrando que, a qualquer momento, caso o jogador queira abandonar o jogo, a tecla "ESC" pode ser pressionada.

Ao chegar à segunda parte, haverá bebidas caindo de cima da tela, sendo elas: água, Beats e Pitu. O objetivo é pegar a maior quantidade de bebidas possível dentro de 30 segundos, exceto a Pitu, pois, a cada uma coletada, uma das três vidas é retirada.

O jogador pode se mover para a esquerda e para a direita utilizando as teclas "A" (esquerda) e "D" (direita).

Além disso, cada bebida tem seu "poder especial". A latinha de Beats, por exemplo, aumenta a velocidade do jogador em 0.5, já a água aumenta o seu tempo de jogo em 1 segundo.

Há duas formas de o jogo terminar: uma é se o jogador perder as três vidas, e a outra é se o tempo limite expirar. Qualquer uma das duas o levará à terceira parte, que é a tela final. Caso o jogo termine devido à perda total das vidas, aparecerá apenas uma mensagem informando que o jogador perdeu. Caso contrário, será exibido o total de bebidas que ele conseguiu pegar. E, para as duas opções, no fim da tela terá: "Sair" ou "Jogar Novamente".

## Capturas de Tela:
### Tela Inicial
![Screenshot 2025-04-09 135918](https://github.com/user-attachments/assets/0542799a-f2dd-4c15-bd20-ad99e8c746fc)
### Tela de Jogo
![Screenshot 2025-04-09 140000](https://github.com/user-attachments/assets/de116bd5-132d-496a-8ca0-1fe85509ee98)
### Telas finais
![Screenshot 2025-04-09 140151](https://github.com/user-attachments/assets/10d6f05a-44f9-46e3-9f12-4c64ec7be804)
![Screenshot 2025-04-09 140234](https://github.com/user-attachments/assets/1c43c99e-923c-4907-b3b8-5f58f15bb4c8)

## Itens Coletáveis:
### Água - ao coletar aumenta tempo e ganha 1 ponto.
![aguanovo](https://github.com/user-attachments/assets/b6c46e13-6119-4bf4-9c5f-8a642c9c7ec4)
### Beats - ao coletar aumenta velocidade e ganha 1 ponto.
![beatsnovo](https://github.com/user-attachments/assets/32355138-a998-480c-a81a-e06347250b69)
### Pitu - ao coletar perde-se 1 vida.
![pitu25](https://github.com/user-attachments/assets/dd5956ab-f7dc-43e9-bb2b-8a65809cc925)

## Arquitetura do Projeto:
- main.py: Arquivo principal do jogo, responsável por integrar todos os módulos e coordenar o funcionamento geral da aplicação.
- player.py: Define o personagem principal, incluindo suas características, animações e movimentações dentro do jogo.
- coletaveis.py: Contém a classe dos três itens coletáveis (água, beats e pitu), fundamentais para a mecânica e a dinâmica do jogo.
- fontes/: Diretório responsável por armazenar as fontes utilizadas nos textos do jogo.
- imagens/: Pasta que reúne todos os elementos gráficos do jogo, como capas, personagens, itens coletáveis e indicadores de vida.
- sons/: Diretório que guarda todos os arquivos de áudio do jogo, incluindo a música de abertura e os efeitos sonoros de coleta.
  
## Ferramentas: 
- Discord: ferramenta de comunicação em grupo, utilizada para troca de ideias, alinhamento de tarefas, discussões sobre o projeto e reuniões com monitores.
- GitHub: plataforma utilizada para armazenar, versionar e compartilhar o projeto, além de possibilitar o trabalho colaborativo com controle de alterações.
- Inteligência Artificial: recurso utilizado no desenvolvimento de imagens.
- Photoshop: utilizado para criar e editar elementos visuais do jogo, como os itens coletáveis e outras imagens da interface.
- Pygame: biblioteca utilizada para o desenvolvimento do jogo, fornecendo os recursos necessários para criar gráficos, sons e interações com o usuário.
- Random: módulo utilizado para gerar aleatoriedade no jogo, a qual deixa a experiência do usuário com jogo mais dinâmica (Ex.: random.randint() e random.choice(), usadas para posicionar e escolher os coletáveis que caem).
- Sys: módulo usado para lidar com funcionalidades do sistema, como a finalização do programa ou a manipulação de argumentos da linha de comando, a qual permite fechar o jogo corretamente (Ex.: sys.exit()), por exemplo.
- Time: utilizado para controlar o tempo dentro do jogo, como pausas, contagem regressiva e intervalos entre ações.
- VS Code: editor de código usado durante o desenvolvimento do projeto, oferecendo suporte a diversas linguagens, extensões e um ambiente prático para programação.

## Divisão de tarefas:
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
- Condicionais: aplicadas ao longo de todo o projeto, permitir com que o jogo reaja de forma dinâmica às interações do usuário.
- Funções: responsáveis por organizar o código, separando suas funcionalidades de forma clara e eficiente.
- Laços de repetição: presentes em grande parte do código, são essenciais para garantir o fluxo contínuo e o funcionamento geral do jogo.
- Listas: utilizadas para armazernar os frames responsáveis pela animação do personagem.
- Tuplas: utilizadas para armazenar dados fixos, como a definição de cores no formato RGB e a posição dos botões na interface.

## Desafios:
### Qual foi o maior erro cometido durante o projeto? Como vocês lidaram com ele?
O maior desafio enfrentado durante o projeto foi decidir por onde começar a criação do jogo. Perdemos bastante tempo em discussões, pois acreditávamos que, se uma parte não fosse concluída corretamente, poderia comprometer o desenvolvimento das demais. No entanto, conseguimos superar esse obstáculo ao buscar entender os mecanismos essenciais para o funcionamento do jogo e, principalmente, ao decidir iniciar a implementação mesmo sem ter a certeza do que estava correto. Essa iniciativa nos deu um ponto de partida e nos permitiu evoluir o projeto, aprendendo com os erros e realizando os ajustes necessários ao longo do caminho.
### Qual foi o maior desafio enfrentado durante o projeto? Como vocês lidaram com ele?
Um dos principais desafios enfrentados foi manter a organização do código em um ambiente onde várias pessoas estavam trabalhando simultaneamente, buscando deixá-lo o mais limpo e compreensível possível. Isso também refletiu na dificuldade inicial com o uso do GitHub. No entanto, conseguimos superar esses obstáculos por meio de uma comunicação mais clara entre os membros da equipe e da prática de comentar o código, facilitando o entendimento coletivo.

Além disso, o uso de ferramentas novas e de conceitos já conhecidos — mas aplicados de formas diferentes — também representou uma dificuldade no início. Assim como no caso do GitHub, a prática constante e os erros cometidos ao longo do processo se tornaram parte do aprendizado, permitindo que avançássemos no desenvolvimento com mais segurança e eficiência.
### Quais as lições aprendidas durante o projeto?
As principais lições aprendidas durante o projeto foram a importância da comunicação entre os membros do grupo e da organização geral do trabalho. Por se tratar de um projeto em equipe, onde todos estavam lidando com ferramentas e conceitos novos para o grupo, percebemos que, se tivéssemos priorizado a comunicação e a organização desde o início, o desenvolvimento teria sido mais leve e fluido. Essa experiência reforçou o valor da colaboração e do planejamento em projetos coletivos.
