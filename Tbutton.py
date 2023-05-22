import pygame

class Button:
    def __init__(self, width, height, text, button_colour, text_colour):
        self.width = width
        self.height = height
        self.text = text
        self.button_colour = button_colour

        font = pygame.font.Font(None, 36)
        self.text_surface = font.render(self.text, True, text_colour)
        self.text_rect = self.text_surface.get_rect()

    def draw_button(self, window, x, y):
        self.x = x
        self.y = y
        
        pygame.draw.rect(window, self.button_colour, (x, y, self.width, self.height))
        self.text_rect.center = ((x + (self.width / 2)), (y + (self.height / 2)))
        window.blit(self.text_surface, self.text_rect)
    
    def change_colour(self, event, first_colour, secound_colour):
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()

            if self.x < mouse_pos[0] < self.x + self.width and self.y < mouse_pos[1] < self.y + self.height:
                self.button_colour = secound_colour
            else:
                self.button_colour = first_colour