import pygame
from breakout.screens import WelcomeScreen, GameOverScreen, GameScreen


class Game:
    """Main class for the application"""

    def __init__(self):
        # Creates the window
        self.window = pygame.display.set_mode((800, 400))

    def run(self):
        """Main method, manages interaction between screens"""

        # These are the available screens
        screens = {
            "welcome": WelcomeScreen,
            "game": GameScreen,
            "game_over": GameOverScreen,
        }

        score = None
        # Start the loop
        running = True
        current_screen = "welcome"
        while running:
            # Obtain the screen class
            screen_class = screens.get(current_screen)
            if not screen_class:
                raise RuntimeError(f"Screen {current_screen} not found!")

            # Create a new screen object, "connected" to the window

            if current_screen == "game_over":
                screen = screen_class(self.window, score)
            else:
                screen = screen_class(self.window)

            # Run the screen
            screen.run()
            if screen.score is not None:
                score = screen.score
            # When the `run` method stops, we should have a `next_screen` setup
            if screen.next_screen is False:
                running = False
            # Switch to the next screen
            current_screen = screen.next_screen


if __name__ == "__main__":
    game = Game()
    game.run()
