def run_game():
    import pygame
    import sys

    pygame.init() 
    pygame.mixer.init() 

    
    pygame.mixer.music.load("assets_tic_tac_toe/background_music.mp3")# Load the background music file
    pygame.mixer.music.set_volume(0.5) # Set the volume
    pygame.mixer.music.play(-1)  # Loop the music indefinitely

    WIDTH, HEIGHT = 900, 900  # Set the dimensions of the game window
    SCREEN = pygame.display.set_mode((WIDTH, HEIGHT)) # Set the game window size
    pygame.display.set_caption("Tic Tac Toe!") # Set the title of the game window
    BOARD = pygame.image.load("assets_tic_tac_toe/Board.png") # Load the game board image
    X_IMG = pygame.image.load("assets_tic_tac_toe/X.png") # Load the image for player X
    O_IMG = pygame.image.load("assets_tic_tac_toe/O.png") # Load the image for player O
    BG_COLOR = (214, 201, 227) # Set the background color of the game window
    button_w, button_h = 200, 60 # Set the width and height of the buttons
    center_x = 450 # Set the center x-coordinate for the buttons
    start_y = 300 # Set the starting y-coordinate for the buttons
    spacing = 30 # Set the spacing between the buttons

    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # Initialize the tic-tac-toe board with numbers
    graphical_board = [[[None, None], [None, None], [None, None]],
                       [[None, None], [None, None], [None, None]],
                       [[None, None], [None, None], [None, None]]] # Create a 3x3 grid to hold the graphical elements for each cell of the board
    to_move = 'X' # Set the first player to move as 'X'
    SCREEN.fill(BG_COLOR) # Fill the game window with the background color
    SCREEN.blit(BOARD, (64, 64)) # Draw the game board image at the specified position
    pygame.display.update() # Update the display to show the initial game state
    game_finished = False  # Flag to indicate if the game has finished
    game_result = None # Variable to store the result of the game (winner or draw)
    is_muted = False  # Flag to indicate if the game is muted

    def render_board(board, ximg, oimg):
        """
        Renders the current state of the tic-tac-toe board by updating the graphical_board
        with the appropriate image (X or O) and its position for each cell.

        Args:
            board (list[list[str]]): A 3x3 matrix representing the tic-tac-toe board, where each cell contains 'X', 'O', or an empty value.
            ximg (pygame.Surface): The image surface to use for rendering 'X' marks.
            oimg (pygame.Surface): The image surface to use for rendering 'O' marks.

        Returns:
            None
        """
        for i in range(3): # Iterate through each row of the board
            for j in range(3): # Iterate through each column of the board
                if board[i][j] == 'X': # If the cell contains 'X', update the graphical_board with the X image and its position
                    graphical_board[i][j][0] = ximg
                    graphical_board[i][j][1] = ximg.get_rect(center=(j*300+150, i*300+150))
                elif board[i][j] == 'O': # If the cell contains 'O', update the graphical_board with the O image and its position
                    graphical_board[i][j][0] = oimg
                    graphical_board[i][j][1] = oimg.get_rect(center=(j*300+150, i*300+150))

    def add_XO(board, graphical_board, to_move):
        """
        Handles the placement of 'X' or 'O' on the tic-tac-toe board based on the current mouse position.

        Args:
            board (list[list[str]]): The current state of the tic-tac-toe board as a 2D list.
            graphical_board (list[list[tuple]]): A 2D list representing the graphical elements (image, position) for each cell.
            to_move (str): The symbol ('X' or 'O') of the player whose turn it is.

        Returns:
            tuple: A tuple containing the updated board and the symbol of the next player to move.

        """
        current_pos = pygame.mouse.get_pos()
        converted_x = (current_pos[0]-65)/835*2
        converted_y = current_pos[1]/835*2
        x = round(converted_x)
        y = round(converted_y)
        if 0 <= x < 3 and 0 <= y < 3:
            if board[y][x] != 'O' and board[y][x] != 'X':
                board[y][x] = to_move
                to_move = 'O' if to_move == 'X' else 'X'
        render_board(board, X_IMG, O_IMG)
        for i in range(3):
            for j in range(3):
                if graphical_board[i][j][0] is not None:
                    SCREEN.blit(graphical_board[i][j][0], graphical_board[i][j][1])
        return board, to_move

    def check_win(board):
        """
        This function examines the provided 3x3 board to determine if either player ('X' or 'O') has won
        by completing a row, column, or diagonal. If a win is detected, it updates the graphical board
        to highlight the winning line using a special image and updates the display. If no win is found
        and there are still empty cells, it returns None. If the board is full and no winner is found,
        it returns "DRAW".

        Args:
            board (list[list[str]]): A 3x3 list representing the tic-tac-toe board, where each cell contains
                either 'X', 'O', or another value indicating an empty cell.

        Returns:
            str or None: Returns 'X' or 'O' if a player has won, "DRAW" if the board is full with no winner,
            or None if the game is still ongoing.
        """
        winner = None
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2] and board[row][0] in ['X', 'O']:
                winner = board[row][0]
                for i in range(3):
                    graphical_board[row][i][0] = pygame.image.load(f"assets_tic_tac_toe/Winning {winner}.png")
                    SCREEN.blit(graphical_board[row][i][0], graphical_board[row][i][1])
                pygame.display.update()
                return winner
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] in ['X', 'O']:
                winner = board[0][col]
                for i in range(3):
                    graphical_board[i][col][0] = pygame.image.load(f"assets_tic_tac_toe/Winning {winner}.png")
                    SCREEN.blit(graphical_board[i][col][0], graphical_board[i][col][1])
                pygame.display.update()
                return winner
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] in ['X', 'O']:
            winner = board[0][0]
            for i in range(3):
                graphical_board[i][i][0] = pygame.image.load(f"assets_tic_tac_toe/Winning {winner}.png")
                SCREEN.blit(graphical_board[i][i][0], graphical_board[i][i][1])
            pygame.display.update()
            return winner
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] in ['X', 'O']:
            winner = board[0][2]
            graphical_board[0][2][0] = pygame.image.load(f"assets_tic_tac_toe/Winning {winner}.png")
            SCREEN.blit(graphical_board[0][2][0], graphical_board[0][2][1])
            graphical_board[1][1][0] = pygame.image.load(f"assets_tic_tac_toe/Winning {winner}.png")
            SCREEN.blit(graphical_board[1][1][0], graphical_board[1][1][1])
            graphical_board[2][0][0] = pygame.image.load(f"assets_tic_tac_toe/Winning {winner}.png")
            SCREEN.blit(graphical_board[2][0][0], graphical_board[2][0][1])
            pygame.display.update()
            return winner
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ['X', 'O']:
                    return None
        return "DRAW"

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if game_finished:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pose = event.pos
                    if continue_rect.collidepoint(mouse_pose):
                        board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                        graphical_board = [[[None, None], [None, None], [None, None]],
                                           [[None, None], [None, None], [None, None]],
                                           [[None, None], [None, None], [None, None]]]
                        to_move = 'X'
                        SCREEN.fill(BG_COLOR)
                        SCREEN.blit(BOARD, (64, 64))
                        pygame.display.update()
                        game_finished = False
                    if quit_rect.collidepoint(mouse_pose):
                        return
                    if mute_rect.collidepoint(mouse_pose):
                        if is_muted:
                            pygame.mixer.music.unpause()
                            is_muted = False
                        else:
                            pygame.mixer.music.pause()
                            is_muted = True
            else:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    board, to_move = add_XO(board, graphical_board, to_move)
                    result = check_win(board)
                    if result is not None:
                        game_finished = True
                        game_result = result
                    pygame.display.update()

        if game_finished: # resetes the game to the starting state
            SCREEN.fill((255,255,255))

            result_font = pygame.font.SysFont(None, 60)
            if game_result == "DRAW":
                result_text = result_font.render("It's a Draw!", True, (50, 50, 50))
            else:
                result_text = result_font.render(f"{game_result} Wins!", True, (50, 50, 50))
            SCREEN.blit(result_text, result_text.get_rect(center=(center_x, start_y - 80)))

            continue_rect = pygame.Rect(center_x - button_w//2, start_y, button_w, button_h)
            quit_rect = pygame.Rect(center_x - button_w//2, start_y + button_h + spacing, button_w, button_h)
            mute_rect = pygame.Rect(center_x - button_w//2, start_y + 2 * (button_h + spacing), button_w, button_h)

            pygame.draw.rect(SCREEN, (100, 200, 100), continue_rect, border_radius=15)
            pygame.draw.rect(SCREEN, (200, 100, 100), quit_rect, border_radius=15)
            pygame.draw.rect(SCREEN, (120, 120, 200), mute_rect, border_radius=15)

            font = pygame.font.SysFont(None, 40)
            cont_text = font.render("Resume", True, (255,255,255))
            quit_text = font.render("Back", True, (255,255,255))
            mute_text = font.render("Mute" if not is_muted else "Unmute", True, (255,255,255))

            SCREEN.blit(cont_text, cont_text.get_rect(center=continue_rect.center))
            SCREEN.blit(quit_text, quit_text.get_rect(center=quit_rect.center))
            SCREEN.blit(mute_text, mute_text.get_rect(center=mute_rect.center))

            pygame.display.update()


if __name__ == '__main__':
    run_game()

