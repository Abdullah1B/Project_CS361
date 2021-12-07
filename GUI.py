import pygame , sys
from Node import Node
from Tower import Tower as tower
from Tower_Hanoi import Tower_Hanoi
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
    Font2 = pygame.font.SysFont(None,30)
    clock = pygame.time.Clock()
    num_move = len(moves) -1 
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
                draw_text(f"minimal moves: 7", Font2, (255,0,0), screen,30 ,10 ) 
                draw_tower(screen)
 
                for i, pile in enumerate(move.Towers):
                    display_pile_of_pegs(pile, 50 + SPACE_PER_PEG*i, 500, peg_height, screen)
                pygame.display.flip()

                clock.tick(3)
            Continue= False
        draw_text(f"moves: {num_move} ", Font2, (255,0,0), screen,500 ,10 ) 
        draw_text("we reach the goal", Font, (255,0,0), screen,100 ,30 ) 
        pygame.display.update()

if __name__ == "__main__":
    tower_a = tower(num_of_disk=3)
    tower_b = tower()
    tower_c = tower()

    G_tower_a = tower()
    G_tower_b = tower()
    G_tower_c = tower(num_of_disk=3)
    Initial = Node(tower_a, tower_b, tower_c, parent=None)
    Goal = Node(G_tower_a, G_tower_b, G_tower_c, parent=None, goal_node=True)
    Tower = Tower_Hanoi(Initial, Goal, 3, 2) 
    node = Tower.A_star_search()
    Path = Tower.path_to_goal(node)
    visual_hanoi_simulation(base_width= 30,peg_height= 40, moves=Path )
    