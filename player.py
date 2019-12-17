from dataclasses import dataclass
from typing import Any
from collections import namedtuple as nt
import random
import math
Position = nt('position', ['x', 'y'])


@dataclass
class Cell:
    '''
===============
defenition of class Cell and function fight
===============
class Cell:
    describes the abilities and characteristics of Cell:
        hp - hitpoints of Cell
        energy - quantity of energy of the Cell
        speed_level - how fast the Cell is
        num_to_upgrade - number of quality in upgr_order string to upgrade
        upgr_order - string, which contains the order how to upgrade the Cell
        position - where the Cell is located
        player_clan - variable which tells to what player this Cell belongs

================
def fight:
================
    make a fight between two Cells
'''
    hp: int = 35
    energy: int = 1
    speed_level: int = 1
    fight_level: int = 1
    force: int = 10
    num_to_upgrade: int = 0
    upgr_order: str = ''  # 'sssff'
    position: Position = Position(0, 0)
    player_clan: int = 0

    def upgrade_speed(self):
        '''Upgrades speed of chosen Cell. You need to have
        3 * (2**(speed_level - 1)) energy to upgrade'''
        if self.energy >= 3 * (2**(self.speed_level - 1)) and self.speed_level < 3:
            self.speed_level += 1
            self.energy -= 3 * (2**(self.speed_level - 1))

    def upgrade_force(self):
        '''Upgrades force of chosen Cell. You need to have
        3 * (2**(fight_level - 1)) energy to upgrade'''
        if self.energy >= 3 * (2**(self.fight_level - 1)) and self.fight_level < 3:
            self.fight_level += 1
            self.force += 5
            self.energy -= 3 * (2**(self.fight_level - 1))

    def upgrade_in_order(self):
        '''upgrades current Cell in the order from self.upgr_order
        if there`s not enough energy, the Cell doesn`t do anything
        to upgrade your cell characteristic to i level ypu need 3*(2**(i - 1)) energy'''
        upgr = self.upgr_order[self.num_to_upgrade: self.num_to_upgrade+1]
        cur_upgr_count = self.upgr_order[:self.num_to_upgrade+1].count(upgr)
        cost_of_upgr = 3*(2**(cur_upgr_count - 1))
        if self.energy > cost_of_upgr:
            if (upgr == '' or cur_upgr_count > 3):
                return
            if upgr == 's':
                self.speed_level += 1
            elif upgr == 'f':
                self.fight_level += 1
                self.force += 5
            else:
                self.upgrade_health()
                return
            self.num_to_upgrade += 1
            self.energy -= cost_of_upgr

    def upgrade_health(self):
        '''upgrades health. You need 8 energy to upgrade'''
        if self.energy > 8:
            self.hp += 2
            self.energy -= 8

    def move(self, direction: str):
        '''moves current cell
        direction: u - up, d - down, l - left, r - right'''
        cur_pos = self.position
        new_pos = cur_pos
        if direction == 'u':
            new_pos = (cur_pos[0] + (2**(self.speed_level-1)), cur_pos[1])
        elif direction == 'd':
            new_pos = (cur_pos[0] - (2**(self.speed_level-1)), cur_pos[1])
        elif direction == 'r':
            new_pos = (cur_pos[0], cur_pos[1] + (2**(self.speed_level-1)))
        elif direction == 'l':
            new_pos = (cur_pos[0], cur_pos[1] - (2**(self.speed_level-1)))
        if(abs(new_pos[0]) <= 10 and abs(new_pos[1]) <= 10):
            self.position = new_pos
        else:
            self.hp -= 5


def fight(first: Cell, second: Cell):
    '''makes a fight between two cells. As a result one of them or both will have 0 hp'''
    while first.hp > 0 and second.hp > 0:
        probable = [i for i in range(0, 12)]
        probable.append(7)
        probable.append(8)
        probable.append(9)
        probable.append(8)
        first.hp -= second.force * probable[random.randint(0, 15)] // 10
        second.hp -= first.force * probable[random.randint(0, 15)] // 10
        first.hp, second.hp = max(0, first.hp), max(0, second.hp)
