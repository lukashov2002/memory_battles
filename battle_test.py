import unittest
import battle
import player


class BattleTest(unittest.TestCase):
    def test_alive_count1(self):
        self.assertEqual(battle.check_alive_count(
            [player.Cell(hp=0), player.Cell(hp=1)]), 1)

    def test_alive_count2(self):
        self.assertEqual(battle.check_alive_count(
            [player.Cell(hp=0), player.Cell(hp=0)]), 0)

    def test_alive_count3(self):
        self.assertEqual(battle.check_alive_count(
            [player.Cell(hp=0), player.Cell(hp=0), player.Cell(hp=1), player.Cell(hp=10)]), 2)

    def test_alive_count4(self):
        self.assertEqual(battle.check_alive_count(
            [player.Cell(hp=0), player.Cell(hp=0), player.Cell(hp=0), player.Cell(hp=0)]), 0)

    def test_check_blue_zone_three_stay_alive(self):
        cells = [player.Cell(hp=0), player.Cell(
            hp=10), player.Cell(hp=10), player.Cell(hp=5)]
        coord = [cl.position for cl in cells]
        t = battle.act_blue_zone(coord, 0, cells)
        self.assertEqual(battle.check_alive_count(cells), 3)

    def test_check_blue_zone_two_stay_alive(self):
        cells = [player.Cell(hp=0), player.Cell(
            hp=10), player.Cell(hp=10), player.Cell(hp=2, position=player.Position(9, 0))]
        coord = [cl.position for cl in cells]
        battle.act_blue_zone(coord, 7, cells)
        t = cells
        self.assertEqual(battle.check_alive_count(cells), 2)

    def test_check_blue_zone_all_die(self):
        cells = [player.Cell(hp=1), player.Cell(
            hp=1), player.Cell(hp=2), player.Cell(hp=2)]
        coord = [cl.position for cl in cells]
        battle.act_blue_zone(coord, 0, cells)
        t = cells
        self.assertEqual(battle.check_alive_count(cells), 0)

    def test_players_fight_first_wins(self):
        cell1 = player.Cell(hp=100)
        cell2 = player.Cell(hp=10)
        player.fight(cell1, cell2)
        self.assertEqual(cell2.hp, 0)

    def test_players_second_first_wins(self):
        cell1 = player.Cell(hp=10)
        cell2 = player.Cell(hp=100)
        player.fight(cell1, cell2)
        self.assertEqual(cell1.hp, 0)

    def test_check_fightings_1(self):
        cells = [player.Cell(hp=200, position=player.Position(9, 0)),
                 player.Cell(hp=12, position=player.Position(9, 0)),
                 player.Cell(hp=2, position=player.Position(10, 0))]
        coord = [cl.position for cl in cells]
        battle.check_fightings(coord, cells)
        self.assertEqual(battle.check_alive_count(cells), 2)

    def test_check_fightings_2(self):
        cells = [player.Cell(hp=2, position=player.Position(9, 0)),
                 player.Cell(hp=120, position=player.Position(9, 0)),
                 player.Cell(hp=5, position=player.Position(10, 0)),
                 player.Cell(hp=200, position=player.Position(10, 0)),
                 player.Cell(hp=5, position=player.Position(10, 1))]
        coord = [cl.position for cl in cells]
        battle.check_fightings(coord, cells)
        self.assertEqual(battle.check_alive_count(cells), 3)

    def test_check_fightings_three_fighting(self):
        cells = [player.Cell(hp=2, position=player.Position(9, 0)),
                 player.Cell(hp=120, position=player.Position(9, 0)),
                 player.Cell(hp=5, position=player.Position(10, 0)),
                 player.Cell(hp=200, position=player.Position(10, 0)),
                 player.Cell(hp=100, position=player.Position(10, 0))]
        coord = [cl.position for cl in cells]
        battle.check_fightings(coord, cells)
        self.assertEqual(battle.check_alive_count(cells), 2)

    def test_player_upgrade_force(self):
        t = player.Cell(hp=2, energy=105, position=player.Position(9, 0))
        t.upgrade_force()
        self.assertEqual(t.fight_level, 2)

    def test_player_upgrade_force_not_enough_energy(self):
        t = player.Cell(hp=2, energy=1, position=player.Position(9, 0))
        t.upgrade_force()
        self.assertEqual(t.fight_level, 1)\


    def test_player_upgrade_speed(self):
        t = player.Cell(hp=2, energy=105, position=player.Position(9, 0))
        t.upgrade_speed()
        self.assertEqual(t.speed_level, 2)

    def test_player_upgrade_speed_not_enough_energy(self):
        t = player.Cell(hp=2, energy=1, position=player.Position(9, 0))
        t.upgrade_speed()
        self.assertEqual(t.speed_level, 1)

    def test_player_upgrade_health(self):
        t = player.Cell(hp=2, energy=105, position=player.Position(9, 0))
        t.upgrade_health()
        self.assertEqual(t.hp, 4)

    def test_player_upgrade_healt_not_enough_energy(self):
        t = player.Cell(hp=2, energy=1, position=player.Position(9, 0))
        t.upgrade_health()
        self.assertEqual(t.hp, 2)


if __name__ == "__main__":
    unittest.main()
