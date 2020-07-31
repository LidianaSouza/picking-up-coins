## Picking up coins

##### Objetivo

O projeto foi desenvolvido como trabalho de fim de curso da disciplina de Linguagens de Programação/UFRJ. O requisito é que seja um código que rode na placa Pyboard. Para aqueles que não possuam a placa é possível projetar e executar em uma interface online que simula as funcionalidades dela.

##### Funcionamento e conceitos

A proposta do jogo é que o usuário colete o maior número de "moedas" sem deixar que alguma toque no "chão".

##### Como testar

- Acesse https://micropython.org/unicorn/;
- Copie o cole o código disponível neste repositório em "PickingUpCoins.py" na seção à direita que está com alguns comentários;
- É obrigatório selecionar os itens "I2C LCD" e "ADC" para que os componentes necessários sejam associados à simulação da placa. As opções de itens aparecem em "PERIPHERALS";

##### Jogando

O jogo inicia com o "personagem coletor" (um quadrado branco) no visor na parte inferior dele. Com o tempo passará a "cair" as "moedas" (quadrados brancos) e para que o personagem as pegue basta mover o "ADC" para o lado a direção de queda da mesma. 

##### Considerações

- A simulação da placa é muito limitada quanto ao processamento, por isto o jogo é construído de uma forma bem simples; 
- Este README foi escrito após um ano da disciplina, então caso haja alguma inconsistência no código, me desculpe :) ;
- Foi utilizada uma classe para produção de números aleatórios que não é de minha autoriza. Notifico no código e reafirmo aqui. Inclusive, agradeço e deixo aqui o link para acesso ao código do Peter Hinch: https://forum.micropython.org/viewtopic.php?t=2727
- O nome e a documentação em inglês foram um devaneio da época, me desculpe :)
