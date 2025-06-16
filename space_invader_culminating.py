from ursina import *
from random import randint, uniform
from ursina import application
import time

def update():
    """
    Updates the game state every frame.
    Handles player movement based on keyboard input, updates invader and bullet positions,
    checks for collisions between bullets and invaders, plays explosion sounds on hit,
    and manages game over conditions if invaders reach the bottom of the screen.

    """
    global invaders, bullets, score, text

    if not game_running:
        return

    player.x += held_keys['d'] * time.dt * player.dx
    player.x -= held_keys['a'] * time.dt * player.dx
    player.x = clamp(player.x, -0.5, 0.5) 

    for invader in invaders:
        invader.y += time.dt * invader.dy

        if invader.y < -0.55:
            player.y = 10
            end_game("You lost! Reload the game!")

    for bullet in bullets:
        bullet.y += time.dt * bullet.dy
        hit_info = bullet.intersects()
        if hit_info.hit:
            Audio('assets_Space_invader\\explosion_sound.wav', autoplay=True)
            bullet.x = 10
            if hit_info.entity in invaders:
                hit_info.entity.x = uniform(-0.5, 0.5)
                hit_info.entity.y = uniform(0.8, 1.2)


def input(key):
    """
    Handles keyboard input during the game.
    If the game is running and the 'space' key is pressed, plays a laser sound and creates a new bullet,
    adding it to the global bullets list.
    Args:
        key (str): The key that was pressed.
    """
    global bullets
    if not game_running:
        return

    if key == "space":
        Audio('assets_Space_invader\\laser_sound.wav', autoplay=True)
        bullet = Bullet()
        bullets.append(bullet)


def end_game(message):
    """
    Ends the current game session, displays a game over message, and enables the restart and back buttons.

    Args:
        message (str): The message to display when the game ends (e.g., "Game Over", "You Win!").

    """
    global game_running, game_over_text
    game_running = False
    game_over_text = Text(text=message, origin=(0, 0), scale=2, color=color.yellow, background=True, y=0.1)
    restart_button.enabled = True
    back_button.enabled = True


def reset_game():
    """
    Resets the game state to its initial configuration.
    This function clears all existing bullets and invaders, reinitializes the invader list,
    resets the player's position, removes any game over text, disables the restart and back buttons,
    and sets the game as running.
    """
    global bullets, invaders, score, game_running, text, game_over_text

    for bullet in bullets:
        destroy(bullet)
    for invader in invaders:
        destroy(invader)

    bullets = []
    invaders = []

    for i in range(10):
        invader = Invader()
        invaders.append(invader)

    player.x = 0
    player.y = -0.5

    if game_over_text:
        destroy(game_over_text)
        game_over_text = None

    restart_button.enabled = False
    back_button.enabled = False

    game_running = True


def quit_game():
    application.quit()


class Invader(Entity):
    """
    Represents an alien invader entity in the Space Invaders game.

    Inherits from:
        Entity

    Attributes:
        parent: The parent field or container for the invader.
        model (str): The 3D model used for the invader (default: 'quad').
        texture (str): The file path to the invader's texture image.
        scale (float): The scale factor for the invader's size.
        position (tuple): The (x, y, z) coordinates for the invader's initial position, randomized within specified ranges.
        collider (str): The type of collider used for collision detection (default: 'box').
        dy (float): The vertical movement speed of the invader.

    Methods:
        __init__(): Initializes a new Invader instance with randomized position and default attributes.
    """
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = 'quad'
        self.texture = 'assets_Space_invader\\alien.png'
        self.scale = 0.1
        self.position = (uniform(-0.5, 0.5), uniform(0.8, 1.2), -0.1)
        self.collider = 'box'
        self.dy = -0.15


class Player(Entity):
    """
    Represents the player entity in the Space Invaders game.

    Inherits from:
        Entity

    Attributes:
        parent: The parent field or scene to which the player belongs.
        model (str): The 3D model used to represent the player.
        texture (str): The texture applied to the player's model.
        scale (tuple): The scale of the player model in (x, y, z) dimensions.
        position (tuple): The initial position of the player in the game world.
        dx (float): The movement speed of the player along the x-axis.
    """
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = 'cube'
        self.texture = 'assets_Space_invader\\Space_ship.png'
        self.scale = (0.1, 0.2, 0.2)
        self.position = (0, -0.5, -0.1)
        self.dx = 0.5


class Bullet(Entity):
    """
    A class representing a bullet entity in the Space Invaders game.

    Inherits from:
        Entity

    Attributes:
        parent: The parent entity or field to which the bullet belongs.
        model (str): The 3D model used for the bullet (default: 'cube').
        color: The color of the bullet (default: color.green).
        texture (str): The texture applied to the bullet (default: 'assets_Space_invader\\laser').
        scale (tuple): The scale of the bullet in (x, y, z) dimensions (default: (0.02, 0.1, 0.1)).
        position: The initial position of the bullet, set to the player's position.
        y (float): The vertical position of the bullet, slightly above the player.
        collider (str): The type of collider used for collision detection (default: 'box').
        dy (float): The vertical speed at which the bullet moves (default: 0.8).
    """
    def __init__(self):
        super().__init__()
        self.parent = field
        self.model = 'cube'
        self.color = color.green
        self.texture = 'assets_Space_invader\\laser'
        self.scale = (0.02, 0.1, 0.1)
        self.position = player.position
        self.y = player.y + 0.2
        self.collider = 'box'
        self.dy = 0.8


app = Ursina()

field_size = 10
Entity(model='quad', scale=60, texture='assets_Space_invader\\blue_sky')
field = Entity(model='quad', color=color.rgba(255, 255, 255, 0), scale=(10, 10),
               position=(field_size // 2, field_size // 2, -0.01))

bullets = []
invaders = []

player = Player()
for i in range(10):
    invader = Invader()
    invaders.append(invader)

 

game_running = True
game_over_text = None  

restart_button = Button(text='Restart', scale=(0.2, 0.1), y=-0.2, on_click=reset_game, enabled=False)
back_button = Button(text='Back', scale=(0.2, 0.1), y=-0.35, on_click=quit_game, enabled=False)

camera.position = (field_size // 2, -18, -18)
camera.rotation_x = -56


def main():
    app.run()


if __name__ == '__main__':
    main()
