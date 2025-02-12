"""
Name: Jose Torres
File Name: boardDisplay.py
Description: Contains all information regarding visuals of the game.
"""

import pygame
from preferences import Preferences

class BoardDisplay:
    def __init__(self):
        # The display where the board is drawn
        self.__display = pygame.display.set_mode((Preferences.GAME_BOARD_WIDTH, Preferences.GAME_BOARD_HEIGHT))
        # Image to show as the "head"
        self.headImage = pygame.image.load(Preferences.HEAD_IMAGE)

    def updateGraphics(self, gameData):
        """ Re-draws the board, food, and snake based
            on the current state of the board """

        self.clear()

        # Draw the board 2D 
        for row in range(0,Preferences.NUM_CELLS_TALL):
            for col in range(0,Preferences.NUM_CELLS_WIDE):
                self.drawSquare(gameData.getCell(row,col))

        # Draw the game over message, if appropriate
        if gameData.getGameOver():
            self.displayGameOver()
        else: 
            # Display Live Score if Game is not over
            self.displayLiveScore(gameData.getSnakeCellLength())

        # Update the display
        pygame.display.update()

    def clear(self):
        """ Resets the background of the display """
        self.__display.fill(Preferences.COLOR_BACKGROUND)

    def drawSquare(self, cell):#row, col, cellColor):
        """ Draws a cell-sized square at the given location.
            Inputs: row - row coordinate of the square to draw
                    col - column coordinate of the square to draw
                    cellColor - color of the square to draw """
        row = cell.getRow()
        col = cell.getCol()

        if cell.isHead() and self.headImage:
            self.drawImage(row, col, self.headImage)
        else:
            cellColor = cell.getCellColor()
            pygame.draw.rect(self.__display, cellColor, [col*Preferences.CELL_SIZE, row*Preferences.CELL_SIZE, 
                                                     Preferences.CELL_SIZE, Preferences.CELL_SIZE])

    def drawImage(self, row, col, image):
        """ Displays an image at the given cell location.
            Inputs: row - row coordinate to draw the image at
                    col - column coordinate to draw the image at
                    image - the pygame image to draw """

        # First, convert the image to a Surface type (with transparent background)
        image = image.convert_alpha()
        # You will want to uncomment the below line if you want your image to fit within one cell
        #image = pygame.transform.scale(image, (Preferences.CELL_SIZE, Preferences.CELL_SIZE))
        # Grab the dimensions of the image
        imageRect = image.get_rect()
        # Place the image in the center of the given cell coordinates
        imageRect.center = ((col*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2),
                            (row*Preferences.CELL_SIZE) + (Preferences.CELL_SIZE / 2))
        # Place the image on the display
        self.__display.blit(image, imageRect)

    def displayGameOver(self):
        """ Displays the game over message """

        # Get the font
        font = Preferences.GAME_OVER_FONT
        # Create the text
        text = font.render(Preferences.GAME_OVER_TEXT, True, Preferences.GAME_OVER_COLOR)
        # Get the dimensions of the text box
        textRect = text.get_rect()
        # Specify the location of the text
        textRect.center = (Preferences.GAME_OVER_X, Preferences.GAME_OVER_Y)
        # Place the game over text on the display
        self.__display.blit(text, textRect)

    def displayLiveScore(self, snakeCellsLength):
        font = Preferences.LIVE_SCORE_FONT
        stringT = "Score: " + str(snakeCellsLength - 1)
        text = font.render(stringT, True, Preferences.LIVE_SCORE_COLOR)
        textRect = text.get_rect()
        textRect.center = (Preferences.LIVE_SCORE_X, Preferences.LIVE_SCORE_Y)
        self.__display.blit(text, textRect)
