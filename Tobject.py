import pygame

class MovingObject:
    def __init__(self, size, speed, color, position):
        self.size = size
        self.speed_x = speed
        self.speed_y = speed
        self.color = color
        self.rect = pygame.Rect(position[0], position[1], size, size)

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

    def check_boundaries(self, window_width, window_height):
        if self.rect.x < 0 or self.rect.x > window_width - self.size:
            self.speed_x *= -1
        if self.rect.y < 100 or self.rect.y > window_height - self.size:
            self.speed_y *= -1

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)