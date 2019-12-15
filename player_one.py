import player
import random


def act(cell: player.Cell, step: int):
    where = ['d', 'u', 'l', 'r']
    cell.upgr_order = 'hhhhh'
    if cell.energy >= 10*(2**(cell.num_to_upgrade - 1)):
        cell.upgrade_health()
    cell.move(where[random.randint(0, 3)])
