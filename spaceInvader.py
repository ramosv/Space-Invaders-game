import sys
import pygame
from settings import Settings
from spaceShip import Ship


#Main class that manages the game
class spaceInvader:
    def __init__(self):
        #start the game 
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screenWidth, self.settings.screenHeight))
        pygame.display.set_caption("Space Invader")

        self.ship = Ship(self)

        #Background color
        self.bgColor = self.settings.bgColor

    def runGame(self):
        #Main loop for the game
        while True:
            #Keybord and mouse events
            self._checkEvents()
            self.ship.update()
            self._updateScreen()      
        
    def _checkEvents(self):
        #Responds to mouse and keyboard events
        for event in pygame.event.get():
                #Executed when we close the game
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                     self._checkKeyDownEvents(event)
                elif event.type == pygame.KEYUP:
                     self._checkKeyUpEvents(event)

                #Keydown/pressdown Keyup/letgo
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moveRight = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moveLeft = True
                    elif event.key == pygame.K_UP:
                         self.ship.moveUp = True
                    elif event.key == pygame.K_DOWN:
                         self.ship.moveDown = True
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moveRight = False
                    elif event.key == pygame.K_LEFT:
                        self.ship.moveLeft = False
                    elif event.key == pygame.K_UP:
                        self.ship.moveUp = False
                    elif event.key == pygame.K_DOWN:
                        self.ship.moveDown = False
                    

    def _updateScreen(self):
         #Fills background color after each iteration
            self.screen.fill(self.settings.bgColor)
            self.ship.blitme()

            #Update the screen with new elements and updates
            pygame.display.flip()
         

if __name__ == "__main__":
    #Making a game instance to run the game
    game = spaceInvader()
    game.runGame()