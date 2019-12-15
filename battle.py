'''This script performs battle of given cells'''
import player
import math
import random
from importlib import import_module
from numpy import random as rand


def act_players(players: list, cells: list, coord: list, step: int):
    '''calls functions from files for each player'''
    for i in range(len(players)):
        if cells[i].hp > 0:
            players[i].act(cells[i], step)
            coord[i] = cells[i].position


def get_field_energy(cells: list, coord: list, field: list):
    '''gives energy to cell in current position'''
    for i in range(len(cells)):
        cells[i].energy += field[coord[i][0] + 10][coord[i][1] + 10]
        field[coord[i][0] + 10][coord[i][1] + 10] = 0


def check_alive_count(cells: list) -> int:
    '''checks how many cells are still alibe'''
    count_alive = 0
    for pers in cells:
        if pers.hp > 0:
            count_alive += 1
    return count_alive


def act_blue_zone(coord: list, blue_zone: int, cells: list):
    '''hurt players who are in blue zone'''
    for i in range(len(cells)):
        if abs(coord[i][0]) >= blue_zone or abs(coord[i][1]) >= blue_zone:
            cells[i].hp -= (3 + rand.choice([0, 0, 1]))
            cells[i].hp = max(cells[i].hp, 0)


def check_fightings(coord: list, cells: list):
    '''this function checks if any cells are in the same point and make them fight if it is true'''
    for i in range(len(cells)):
        for j in range(i):
            if coord[i][0] == coord[j][0] and coord[i][1] == coord[j][1]:
                player.fight(cells[i], cells[j])


def simulate_battle(cells: list, players: list, field: list):
    '''simulates full battle of cells. The result is the same as if you simulate 
    battle by steps'''
    step = 0
    blue_zone = 15
    count_alive = len(cells)
    while count_alive > 1:
        coord = [cl.position for cl in cells]

        count_alive = check_alive_count(cells)
        get_field_energy(cells, coord, field)
        act_players(players, cells, coord, step)
        check_fightings(coord, cells)
        if blue_zone > 0:
            blue_zone -= 1
        step += 1

        act_blue_zone(coord, blue_zone, cells)


def perform_next_step(field: list, players: list, cells: list, step: int = 0) -> int:
    '''performs next step of battle for graphical library by variables of players'''
    count_alive = check_alive_count(cells)
    if count_alive < 2:
        return 0
    blue_zone = max(12 - step // 4, 0)
    coord = [cl.position for cl in cells]

    count_alive = check_alive_count(cells)
    get_field_energy(cells, coord, field)
    act_players(players, cells, coord, step)
    coord = [cl.position for cl in cells]
    check_fightings(coord, cells)
    if blue_zone > 0:
        blue_zone -= 1
    step += 1
    act_blue_zone(coord, blue_zone, cells)
    return 1


def main() -> str:
    '''performs the battle for specific variables. But it`s better to use simulate_battle 
    functions for this purpose'''
    print('this is main of BATTLE')
    field = [[random.randint(0, 4) for i in range(21)] for j in range(21)]
    players = [import_module('player_one'), import_module('player_two')]
    cells = [player.Cell(position=player.Position(6, 5), hp=5),
             player.Cell(position=player.Position(4, 5))]

    simulate_battle(cells, players, field)
    #perform_next_step(field, players, cells)
    # print(cells)
    #perform_next_step(field, players, cells)
    # print(cells)

    for i in range(len(cells)):
        if cells[i].hp > 0:
            return f'Cell #{i+1} won this game. Our congratulations!'
    return 'None of cells won the game. They all died :('


# def fight(cell_left: player.Cell, cell_right: player.Cell):
#    while True:
#        cell_left.hp -= cell_right.fight_level
#        cell_right.hp -= cell_left.fight_level


if __name__ == '__main__':
    main()
