import pygame, sys, random
from objects import new_player, new_ball
from time import sleep

player_score = 0
cpu_score = 0

def collisions(ball, p1, p2, wn_height, wn_width):
      global player_score
      global cpu_score
      # ball with the window border
      if ball.shape.top <= 5:
            ball.v_speed *= -1
            player_score+=1
      if ball.shape.bottom>=wn_height-5:
            ball.v_speed *= -1
            cpu_score +=1
                  
      if ball.shape.left <= 0 or ball.shape.right >= wn_width:
            ball.h_speed *= -1

      # ball with the player and CPU
      if ball.shape.colliderect(p1.shape) or ball.shape.colliderect(p2.shape):
            ball.v_speed *= -1

      # player with the window border
      if p1.shape.x <= 0:
            p1.shape.x = 0
      if p1.shape.right >= wn_width:
            p1.shape.right = wn_width

      # opponant with window border
      if p2.shape.x <= 0:
            p2.shape.x = 0
      if p2.shape.right >= wn_width:
            p2.shape.right = wn_width


def form_creation(wn_height, wn_width):
      # ball
      ball = new_ball()
      ball.create_form( (wn_width/2 - ball.w/2), (wn_height/2 - ball.h/2) )

      # setting up the players
      p1 = new_player()
      p1.create_form( ((wn_width/2) - p1.w/2), wn_height-15)
      
      p2 = new_player()
      p2.create_form( ((wn_width/2) - p2.w/2),5)

      return ball, p1, p2


def get_text_objects(text, font):
      textsurf = font.render(text, True, (255, 255, 255))
      return textsurf, textsurf.get_rect()

def show_text(win, value = "", coords = (0,0), name = "score"):
      x, y = coords
      text  = pygame.font.Font("freesansbold.ttf", 20)
      TextSurf, TextRect = get_text_objects(name+" : "+str(value), text)
      TextRect.center = (x, y)
      win.blit(TextSurf, TextRect)


def counter(win, secs, x  = 0, y = 0, window_col = (0,0,0) ):
      largetext  = pygame.font.Font("freesansbold.ttf", 110)
      
      for sec in range(secs, 0, -1):
            TextSurf, TextRect = get_text_objects(str(sec), largetext)
            TextRect.center = (x, y)
            win.blit(TextSurf, TextRect )
            sleep(1)
            pygame.display.flip()
            win.fill(window_col)
      sleep(1.5)

def object_movement(ball, p1, p2):
      #ball movement
      ball.shape.x += ball.h_speed
      ball.shape.y += ball.v_speed
                    
      #player movement
      p1.shape.x += p1.speed

      #cpu movement
      p2.speed = 6
      if p2.shape.left > ball.shape.left:
            p2.shape.left -= p2.speed
      if p2.shape.right < ball.shape.right:
            p2.shape.right += p2.speed


def check_score():
      

def main():
      global score
      pygame.init()
      clock = pygame.time.Clock()
      p_speed = 9
      
      # setting the main window 
      wn_width = 980
      wn_height = 700
      bgcolor = pygame.Color("grey12")
      
      win = pygame.display.set_mode((wn_width, wn_height))
      pygame.display.set_caption("--- PONG GAME ---")

      win.fill(bgcolor)
      
      ball, p1, p2 = form_creation(wn_height, wn_width)


      show_text(win," ", (wn_width/2, wn_height/2), " Press <space> to play the game")
      pygame.display.flip()
      sleep(1.5)
      
            
      counter(win, 3, wn_width/2, wn_height/2, window_col = bgcolor)
      # game loop
      run = True
      while run:

            #check for events
            for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                  if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                              p1.speed = p_speed
                        if event.key == pygame.K_LEFT:
                              p1.speed = -p_speed
                  if event.type == pygame.KEYUP:
                        p1.speed = 0

                        
            #visuals
            win.fill(bgcolor)
            p1.draw_self(win)
            p2.draw_self(win)
            ball.draw_self(win)
            pygame.draw.aaline(win, (200, 200, 200), (0, wn_height/2), (wn_width, wn_height/2) )

            show_text(win, player_score, (50, (wn_height/2) + 20), "player")
            show_text(win, cpu_score, (40, (wn_height/2) - 20), "cpu")

            object_movement(ball, p1, p2)
            collisions(ball, p1, p2, wn_height, wn_width)


            runcheck_score()

            # updating the display
            pygame.display.flip()
            clock.tick(60)
      
      
if __name__ == "__main__":
      main()






