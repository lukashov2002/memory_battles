'''
===========
This script draws the main window of the game and updates it calling other functions
===========
You need to install arcade library t run this script
'''
import arcade
import PySimpleGUI as sg
from dataclasses import dataclass
from typing import Any
from collections import namedtuple as nt
import random
import player
import os
import time
from importlib import import_module
import battle
ROW_COUNT = 21
COLUMN_COUNT = 21

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 32
HEIGHT = 32

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN
SCREEN_TITLE = 'Array Backed Grid Example'
field = [[random.randint(0, 4) for i in range(21)] for j in range(21)]
players = [import_module('player_one'), import_module('player_two')]
cells = [player.Cell(position=player.Position(5, 5), hp=15, player_clan=0),
         player.Cell(position=player.Position(-5, -5), hp=15, player_clan=1)]
#STEP = 0


class MyGame(arcade.Window):
    '''Main application class.'''
    STEP = 0

    def __init__(self, width, height, title):
        '''Set up the application.'''
        super().__init__(width, height, title, update_rate=1)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append((0, 0))  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        '''Render the screen.'''
        arcade.start_render()
        blue_zone = max(12 - self.STEP // 4, 0)
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                color = arcade.color.WHITE
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2
                if abs(row - 10) >= blue_zone or abs(column - 10) >= blue_zone:
                    arcade.draw_rectangle_filled(
                        x, y, WIDTH, HEIGHT, arcade.color.BABY_BLUE_EYES)
                else:
                    arcade.draw_rectangle_filled(
                        x, y, WIDTH, HEIGHT, arcade.color.WHITE)

                if self.grid[row][column] == (1, 0) or self.grid[row][column] == (1, 1):
                    arcade.draw_circle_filled(
                        x - WIDTH // 4, y - HEIGHT // 4, WIDTH // 4, arcade.color.RED)
                if self.grid[row][column] == (0, 1) or self.grid[row][column] == (1, 1):
                    arcade.draw_circle_filled(
                        x + WIDTH // 4, y + HEIGHT // 4, WIDTH // 4, arcade.color.BLUE)

    def on_update(self, delta_time):
        '''updates logic for redrawing'''
        coord = [cl.position for cl in cells]
        # DELETE PREVIOUS PAGE
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                self.grid[row][column] = (0, 0)

        for i in range(len(coord)):
            if cells[i].player_clan == 1:
                self.grid[coord[i][0] + 10][coord[i][1] +
                                            10] = (self.grid[coord[i][0] + 10][coord[i][1] + 10][0], 1)
            else:
                self.grid[coord[i][0] + 10][coord[i][1] +
                                            10] = (1, self.grid[coord[i][0] + 10][coord[i][1] + 10][1])
        res = battle.perform_next_step(field, players, cells, self.STEP)
        if res == 0:
            time.sleep(1)
            arcade.finish_render()
            count_alive = 0
            for i in range(len(cells)):
                if cells[i].hp > 0:
                    count_alive += 1
            if count_alive > 0:
                for i in range(len(cells)):
                    if cells[i].hp > 0:
                        raise Exception(f'Cell #{i + 1} won this game')
            else:
                raise Exception('All cells are dead. It`s a draw')
        self.STEP += 1


def main():
    #os.system('kwrite ./player_one.py')
    #os.system('kwrite ./player_two.py')
    try:
        MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.run()
        arcade.close_window()
    except Exception as result:
        print(result.args)
        layout = [[sg.Text(result.args[0], justification='center')],
                  [sg.Exit(size=(100, 100))]]

        window = sg.Window('RESULTS', layout, size=(500, 80))

        while True:                             # The Event Loop
            event, values = window.read()
            print(event, values)
            if event in (None, 'Exit'):
                break
        window.close()


if __name__ == '__main__':
    main()
