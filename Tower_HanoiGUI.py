import pygame , sys
from Test import Test
from pygame.locals import *


SPACE_PER_PEG = 200



def display_pile_of_pegs(pegs, start_x, start_y, peg_height, screen):


    for i, pegwidth in enumerate(pegs):

        pygame.draw.rect(screen,(255,0,0),(start_x + (SPACE_PER_PEG - pegwidth)/2 , start_y - peg_height * i,pegwidth ,peg_height))

def draw_text(text, font , color, surface, x , y ):
    textobj = font.render(text, 1 , color)
    textrect = textobj.get_rect()
    textrect.topleft = (x , y)
    surface.blit(textobj, textrect)


def draw_tower(surface):
    pygame.draw.rect(surface, (0 , 0 , 0), pygame.Rect(140, 100, 20, 550))
    pygame.draw.rect(surface, (0 , 0 , 0), pygame.Rect(340, 100, 20, 550))
    pygame.draw.rect(surface, (0 , 0 , 0), pygame.Rect(540, 100, 20, 550))
    

def visual_hanoi_simulation( base_width, peg_height, moves):

    pygame.init()
    Font = pygame.font.SysFont(None, 100)
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode( (750, 650) )
    pygame.display.set_caption('Towers of Hanoi')
    for i in reversed(moves):
        for j in range(0,len(i.Towers)):
            for c in range (0 ,len(i.Towers[j])):
                i.Towers[j][c] = i.Towers[j][c] * base_width 
    Continue = True     
      
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if Continue:
          
                 
            for move in reversed(moves):
                screen.fill((255, 255, 255))
                screen.fill((0,0,0), rect= [0, 545 , 800,700])
                draw_tower(screen)
 
                for i, pile in enumerate(move.Towers):
                    display_pile_of_pegs(pile, 50 + SPACE_PER_PEG*i, 500, peg_height, screen)
                pygame.display.flip()

                clock.tick(3)
            Continue= False
        draw_text("we reach the goal", Font, (255,0,0), screen,100 ,10 ) 
        pygame.display.update()

if __name__ == "__main__":
    Path = Test()
    moves = Path.Path
    visual_hanoi_simulation(base_width= 30,peg_height= 40, moves=moves )
    