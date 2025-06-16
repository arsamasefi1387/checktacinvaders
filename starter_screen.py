import pygame
import subprocess



pygame.init()

screen_width , screen_height =  (900 , 900)

screen = pygame.display.set_mode((screen_width , screen_height))

BG_Color =  (214, 201, 227)


def tic_tac_to_game(start_rect, hovered=False):
    color = (100, 200, 100)
    if hovered:
        color = (80, 180, 80)
    pygame.draw.rect(screen, color, start_rect, border_radius=20)
    game_icon = pygame.image.load("assets_tic_tac_toe/tic_tac_toe.png")  
    game_icon = pygame.transform.smoothscale(game_icon, (start_rect.width - 20, start_rect.height - 20))

    icon_rect = game_icon.get_rect(center=start_rect.center)
    screen.blit(game_icon, icon_rect)

def Space_invaders_game(start_rect, hovered=False):
    color = (100, 100, 200)
    if hovered:
        color = (80, 80, 180)
    pygame.draw.rect(screen, color, start_rect, border_radius=20)
    game_icon = pygame.image.load("assets_Space_invader\\space_icon.png")  
    game_icon = pygame.transform.smoothscale(game_icon, (start_rect.width - 20, start_rect.height - 20))

    icon_rect = game_icon.get_rect(center=start_rect.center)
    screen.blit(game_icon, icon_rect)

def checkers_game(start_rect, hovered=False):
    color = (200,100,200)
    if hovered:
        color = (180, 80, 180)
    pygame.draw.rect(screen, color, start_rect, border_radius=20)
    game_icon = pygame.image.load("assets_Space_invader\\chekers.png")  
    game_icon = pygame.transform.smoothscale(game_icon, (start_rect.width - 20, start_rect.height - 20))

    icon_rect = game_icon.get_rect(center=start_rect.center)
    screen.blit(game_icon, icon_rect)

def QUIT_BUTTON(stop_rect, hovered=False):
    color = (200, 100, 100) 
    
    if hovered:
        color = (180, 80, 80)
    pygame.draw.rect(screen, color, stop_rect, border_radius=20)
    font = pygame.font.SysFont(None, 60)
    text = font.render("QUIT", True, (255, 255, 255))
    screen.blit(text, text.get_rect(center=stop_rect.center))


def starter_screen():
    running = True

    while running:
        screen.fill(BG_Color)
        mouse_pos = pygame.mouse.get_pos()
        game_1_rect = pygame.Rect(0, 0, 250, 150)
        game_1_rect.center = (450, 130)
        stop_rect = pygame.Rect(0, 0, 250, 150)
        stop_rect.center = (450, 770)
        space_invaders_rect = pygame.Rect(0, 0, 250, 150)
        space_invaders_rect.center = (450 , 350)
        checkers_rect =pygame.Rect(0,0,250,150)
        checkers_rect.center = (450 , 570)

        tic_tac_to_game(game_1_rect, game_1_rect.collidepoint(mouse_pos))
        QUIT_BUTTON(stop_rect, stop_rect.collidepoint(mouse_pos))
        Space_invaders_game(space_invaders_rect , space_invaders_rect.collidepoint(mouse_pos))
        checkers_game(checkers_rect , checkers_rect.collidepoint(mouse_pos))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if game_1_rect.collidepoint(event.pos):
                    subprocess.run(["python", "tic_tac_toe.py"])
                elif stop_rect.collidepoint(event.pos):
                     running = False
                elif space_invaders_rect.collidepoint(event.pos):
                    subprocess.run(["python", "space_invader_culminating.py"])
                elif checkers_rect.collidepoint(event.pos):
                    subprocess.run(["python", "checkers_main.py"])

    pygame.quit()

starter_screen()