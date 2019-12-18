import player
import random


def act(cell: player.Cell, blue_zone: int):
    pos = cell.position
    if pos[0] == 10:
        cell.move('d')
    elif pos[0] == -10:
        cell.move('u')
    if pos[1] == 10:
        cell.move('l')
    elif pos[0] == -10:
        cell.move('r')
    elif pos[0] + 1 >= blue_zone:
        cell.move('d')
    elif -pos[0] + 1 >= blue_zone:
        cell.move('u')
    elif pos[1] + 1 >= blue_zone:
        cell.move('l')
    elif -pos[1] + 1 >= blue_zone:
        cell.move('r')
    else:
        where = ['d', 'u', 'l', 'r']
        cell.move(where[random.randint(0, 3)])

    if blue_zone % 2 == 0:
        if cell.energy > 3 * 2 ** (cell.fight_level - 1):
            cell.upgrade_force
    else:
        if cell.energy > 8:
            cell.upgrade_health
