#configurações iniciais  

import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game")
largura, altura = 1200, 800
tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

#cores 
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelha = (255,0,0)
verde = (0, 255, 0)


#propriedades da cobra
tamanho_quadrado = 10
velocidade_jogo = 15

def gerar_comida():
   comida_x = round(random.randrange(0,largura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
   comida_y = round(random.randrange(0,altura - tamanho_quadrado) / tamanho_quadrado) * tamanho_quadrado
   return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
   pygame.draw.rect(tela, vermelha, [comida_x, comida_y, tamanho, tamanho ])

def desenhar_cobra(tamanho, pixels):
   for pixel in pixels:
      pygame.draw.rect(tela, verde, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao):
   fonte = pygame.font.SysFont("Helvetica", 25)
   text = fonte.render(f"Pontos: {pontuacao}", False, verde)
   tela.blit(text, [1,1])

def selecionar_velocidade(tecla):
   if tecla == pygame.K_DOWN:
      velocidade_x = 0
      velocidade_y = tamanho_quadrado
   
   elif tecla == pygame.K_UP:
      velocidade_x = 0
      velocidade_y = -tamanho_quadrado
   
   elif tecla == pygame.K_RIGHT:
      velocidade_x = tamanho_quadrado
      velocidade_y = 0
   
   elif tecla == pygame.K_LEFT:
      velocidade_x = -tamanho_quadrado
      velocidade_y = 0


   return velocidade_x, velocidade_y



def play_game():
   end_game = False

   x = largura / 2
   y = altura / 2

   velocidade_cobra_x = 0
   velocidade_cobra_y = 0

   tamanho_cobra = 1
   pixels = []
   comida_x, comida_y = gerar_comida()
   
   while not end_game:
      tela.fill(preta)


      for evento in pygame.event.get():
         if evento.type == pygame.QUIT:
            end_game = True
         elif evento.type == pygame.KEYDOWN:
            velocidade_cobra_x, velocidade_cobra_y = selecionar_velocidade(evento.key)
      
      #desenhar comida
      desenhar_comida(tamanho_quadrado, comida_x, comida_y)
      
      #desenhar pontuacao
      desenhar_pontuacao(tamanho_cobra - 1)

      #atualizar posicao cobra
      x += velocidade_cobra_x
      y += velocidade_cobra_y

      #desenhar cobra
      pixels.append([x,y])
      if len(pixels) > tamanho_cobra:
         del pixels[0]
      
      for pixel in pixels[:-1]:
         if pixel == [x,y]:
            end_game = True
      desenhar_cobra(tamanho_quadrado, pixels)

      #atualização da tela
      pygame.display.update()

      #criar uma nova comida
      if x == comida_x and y == comida_y:
         tamanho_cobra += 1
         comida_x, comida_y = gerar_comida()

      relogio.tick(velocidade_jogo)

#criar um loop infinito

#desenhar os objetos do jogo na tela
#pontuação 
#cobrinha
#comida

#criar logica de terminar o jogo
#oque acontece:
#cobra bateu na parede
#cobra bateu em si mesma

#pegar interações do usuario
#fechou a tela 
#apertou teclas para mover a cobra



play_game()
