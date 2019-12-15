import player
import random


def act(cell: player.Cell, step: int):
    where = ['d', 'u', 'l', 'r']
    cell.move(where[random.randint(0, 3)])
    # cell.move('u')
