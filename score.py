import pygame

class Score(pygame.sprite.Sprite):
    def __init__(self, font, pos=(10, 10), color = (255,255,255)):
        super().__init__()
        
        self.score = 0
        self.font = font
        self.color = color
        self.pos = pos
        self.image = self.font.render(f"Score: {self.score}",True, self.color)
        self.rect = self.image.get_rect(topleft=self.pos)
        
    def add(self, points):
        self.score += points
        self.image = self.font.render(f"Score: {self.score}", True, self.color)
    
    def update(self):
        pass

    def draw(self, screen):
        print("drawing score to screen")
        screen.blit(self.image, self.pos)