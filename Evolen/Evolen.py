
import arcade
import math

SCREEN_WIDTH = 1024	
SCREEN_HEIGHT = 576

SPRITE_SCALING_PLAYER = 0.3
MOVEMENT_SPEED = 5

class EvolenGame(arcade.Window):
    """ Main application class. """
    

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.ALMOND)

    def setup(self):
        # Set up your game here
        self.player_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("resources/t-rex-1M.png", SPRITE_SCALING_PLAYER)     
        width, height = self.get_size()
        self.player_sprite.center_x = width/2
        self.player_sprite.center_y = height/2
        self.player_list.append(self.player_sprite)
        self.__rad = 0.0


    def on_draw(self):
        """ Render the screen. """
        arcade.start_render()
        # Your drawing code goes here
        self.player_list.draw()

    def update(self, delta_time):
        """ All the logic to move, and the game logic goes here. """
        self.player_sprite.center_x += MOVEMENT_SPEED*math.cos(self.__rad)
        self.player_sprite.center_y += MOVEMENT_SPEED*math.sin(self.__rad)
        self.player_sprite.angle = math.degrees(self.__rad) - 90

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """

        # Move the center of the player sprite to match the mouse x, y
        delta_x = x - self.player_sprite.center_x
        delta_y = y - self.player_sprite.center_y
        self.__rad = math.atan2(delta_y, delta_x)


def main():
    game = EvolenGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()