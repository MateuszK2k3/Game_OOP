import pygame
import Tobject
import Tbutton

# inicjalizacja Pygame
pygame.init()

# kolory
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
GRAY_2 = (48,48,48)

# parametry obiektu
OBJECT_SIZE = 20
OBJECT_SPEED = 3
OBJECT_COLOUR = WHITE

# ustawienia okna
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 800
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
WIDNOW_COLOUR = BLACK

#def back_button():
#    if event.type == pygame.MOUSEBUTTONDOWN:
#        mouse_pos = pygame.mouse.get_pos()
#        if 800 < mouse_pos[0] < 1000 and 700 < mouse_pos[1] < 750:
#            main_menu()
#    elif event.type == pygame.MOUSEMOTION:
#        mouse_pos = pygame.mouse.get_pos()
#       if 800 < mouse_pos[0] < 1000 and 700 < mouse_pos[1] < 750:
#            return True
#        else:
#            return False
    

# funkcja wyświetlająca menu
def main_menu():
    buttons_position_width = (WINDOW_WIDTH - 200)/ 2

    graj_button = Tbutton.Button(200, 50, "graj", GRAY, WHITE)
    info_button = Tbutton.Button(200, 50, "informacje", GRAY, WHITE)
    wyjscie_button = Tbutton.Button(200, 50, "wyjście", GRAY, WHITE)

    while True:
        # obsługa zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # obsługa przycisków
                mouse_pos = pygame.mouse.get_pos()
                if buttons_position_width < mouse_pos[0] < buttons_position_width+200 and 200 < mouse_pos[1] < 250:
                    # naciśnięto przycisk "Graj"
                    game_loop()
                elif buttons_position_width < mouse_pos[0] < buttons_position_width+200 and 300 < mouse_pos[1] < 350:
                    # naciśnięto przycisk "Info"
                    show_info()
                elif buttons_position_width < mouse_pos[0] < buttons_position_width+200 and 400 < mouse_pos[1] < 450:
                    # naciśnięto przycisk "Wyjście"
                    pygame.quit()
                    quit()
            
        # rysowanie menu
        WINDOW.fill(WIDNOW_COLOUR)
        font = pygame.font.Font(None, 72)
        text_surface = font.render("Gra", True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (WINDOW_WIDTH / 2, 100)
        WINDOW.blit(text_surface, text_rect)

        graj_button.change_colour(event, GRAY, GRAY_2)
        graj_button.draw_button(WINDOW, buttons_position_width, 200)

        info_button.change_colour(event, GRAY, GRAY_2)
        info_button.draw_button(WINDOW, buttons_position_width, 300)

        wyjscie_button.change_colour(event, GRAY, GRAY_2)
        wyjscie_button.draw_button(WINDOW, buttons_position_width, 400)


        pygame.display.update()

# funkcja wyświetlająca informacje
def show_info():
    back_button = Tbutton.Button(200, 50, "powrót", GRAY, WHITE)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            info = "Tutaj będą informacje na temat gry."
            font = pygame.font.Font(None, 36)
            text_surface = font.render(info, True, WHITE)
            text_rect = text_surface.get_rect()
            text_rect.center = (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
            WINDOW.fill(WIDNOW_COLOUR)
            WINDOW.blit(text_surface, text_rect)

            back_button.change_colour(event, GRAY, GRAY_2)
            back_button.draw_button(WINDOW, 800, 700)

            pygame.display.update()

def draw_window(moving_object):
    WINDOW.fill(WIDNOW_COLOUR)
    moving_object.draw(WINDOW)
    pygame.display.update()

# funkcja obsługująca rozgrywkę
def game_loop():
    moving_object = Tobject.MovingObject(OBJECT_SIZE, OBJECT_SPEED, OBJECT_COLOUR, [WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2])

    clock = pygame.time.Clock()
    #===============główna pętla====================
    while True:
        # FPS
        clock.tick(75)

        # wyjście z programu
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # poruszanie obiektem na mapie
        moving_object.move()
        moving_object.check_boundaries(WINDOW_WIDTH, WINDOW_HEIGHT)

        draw_window(moving_object)

if __name__ == "__main__":
    main_menu()