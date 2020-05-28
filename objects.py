

##THIS MODULE IS DEFINED FOR THE GAME OBJECTS
import pygame

# creating a player object
class new_player:
      def __init__(self, h = 10, w = 80, color = (200, 200, 200) ):
            self.h = h
            self.w = w
            self.color = color  #---(r,g,b)
            self.speed = 0
            
      def create_form(self, x, y):
            self.shape = pygame.Rect(x, y, self.w, self.h)

      def draw_self(self, surface):
            pygame.draw.rect(surface, self.color, self.shape)


# creating ball object
class new_ball:
      def __init__(self, h = 20, color = (200, 200, 200) ):
            self.h = h
            self.w = h
            self.color = color  #---(r,g,b)
            self.speed = 7
            self.h_speed = self.speed-1
            self.v_speed = self.speed
            
      def create_form(self, x, y):
            self.shape = pygame.Rect(x, y, self.w, self.h)

      def draw_self(self, surface):
            pygame.draw.ellipse(surface, self.color, self.shape)


