

import unittest

from .. import constants as c

from tt_logic.clans import constants as clans_constants


class ConstantsTest(unittest.TestCase):

    def test_constants_values(self):

        self.assertEqual(c.EMISSARY_POWER_HISTORY_WEEKS, 4)
        self.assertEqual(c.EMISSARY_POWER_HISTORY_LENGTH, 4 * 7 * 24)
        self.assertEqual(c.EMISSARY_POWER_RECALCULATE_STEPS, 672.0)
        self.assertEqual(c.EMISSARY_POWER_REDUCE_FRACTION, 0.9931704959660097)

        self.assertEqual(c.MAXIMUM_HEALTH, 5000)
        self.assertEqual(c.MAXIMUM_HEALTH_DELTA, 750)
        self.assertEqual(c.NORMAL_DAMAGE_TO_HEALTH, 1000)
        self.assertEqual(c.DAMAGE_TO_HEALTH_DELTA, 100)

        self.assertEqual(c.HEALTH_REGENERATION_MIN, 5)
        self.assertEqual(c.HEALTH_REGENERATION_MAX, 15)

        self.assertEqual(c.INITIAL_ATTRIBUTE_VALUE, 0)

        self.assertEqual(c.ATRIBUTE_MAXIMUM_DELTA, 2500)

        self.assertEqual(c.NORMAL_ATTRIBUTE_MAXIMUM, 10000)

        self.assertEqual(c.MAXIMUM_ATTRIBUTE_MAXIMUM, 12500)

        self.assertEqual(c.EXPECTED_LEVELING_TIME, 1 * 365)

        self.assertAlmostEqual(c._ATTRIBUT_INCREMENT_DELTA, 13.698630136986301)
        self.assertEqual(c.ATTRIBUT_INCREMENT_DELTA, 14)

        self.assertGreater(c.ATTRIBUT_INCREMENT_DELTA, 1)

        expected_leveling_days = ((c.NORMAL_ATTRIBUTE_MAXIMUM - c.INITIAL_ATTRIBUTE_VALUE) /
                                  (c.ATTRIBUT_INCREMENT_DELTA * clans_constants.SIMULTANEOUS_EMISSARY_EVENTS))

        self.assertAlmostEqual(expected_leveling_days, 357.14285714285717)

        self.assertEqual(c.ATTRIBUT_INCREMENT_BUFF, 7)

        self.assertEqual(c.BUFFED_ATTRIBUT_INCREMENT_DELTA, 21)
        self.assertEqual(c.DEBUFFED_ATTRIBUT_INCREMENT_DELTA, 7)

        self.assertGreater(c.DEBUFFED_ATTRIBUT_INCREMENT_DELTA, 0)

        self.assertEqual(c.QUEST_POWER_BONUS, 0.5)
        self.assertEqual(c.QUEST_EXPERIENCE_BUFF, 2.0)
        self.assertEqual(c.QUEST_EXPERIENCE_DEBUFF, 0.7)

        self.assertEqual(c.POSITIVE_TRAITS_NUMBER, 3)
        self.assertEqual(c.NEGATIVE_TRAITS_NUMBER, 2)

        self.assertEqual(c.EVENT_POWER_FRACTION, 0.5)

        self.assertEqual(c.EVENT_EXPERIENCE_BUFF, 0.25)
        self.assertEqual(c.EVENT_EXPERIENCE_DEBUFF, 0.25)

        self.assertEqual(c.MIN_EXPERIENCE_PER_EVENT, 21)
        self.assertEqual(c.MAX_EXPERIENCE_PER_EVENT, 84)

        self.assertEqual(c.MIN_ACTION_POINTS_PER_EVENT, 20)
        self.assertEqual(c.MAX_ACTION_POINTS_PER_EVENT, 62)

        self.assertEqual(c.PLACE_LEADERS_NUMBER, 3)

        self.assertEqual(c.RACE_PRESSURE_MODIFIER_MIN, 0.25)
        self.assertEqual(c.RACE_PRESSURE_MODIFIER_MAX, 2.00)

        self.assertEqual(c.TIME_FOR_PARTICIPATE_IN_PVP, 30)
        self.assertEqual(c.EXPECTED_ATTRIBUTES_INCREMENT_FROM_EVENT, 28)
        self.assertEqual(c.ATTRIBUTES_FOR_PARTICIPATE_IN_PVP, 840)

        self.assertEqual(c.TASK_BOARD_PLACES_NUMBER, 10)

        self.assertEqual(len(c.PROTECTORAT_BONUSES), clans_constants.MAXIMUM_EMISSARIES + 1)
        self.assertEqual(c.PROTECTORAT_BONUSES, [0,
                                                 0.50,
                                                 0.75,
                                                 0.95,
                                                 1.15,
                                                 1.35,
                                                 1.50,
                                                 1.65,
                                                 1.80,
                                                 1.90,
                                                 2.00])

        self.assertEqual(c.PLACE_EVENT_MIN_EFFECT_POWER, 0.25)
        self.assertEqual(c.PLACE_EVENT_MAX_EFFECT_POWER, 1.25)

    def test_health_regeneration__worst_for_attackers(self):
        # провека, что в худшем для нападающих случае
        # эмиссар проживёт не более N дней при постоянной потере здоровья

        N = 10

        # интервал — день
        max_regeneration = c.HEALTH_REGENERATION_MAX * 24
        min_damage = c.NORMAL_DAMAGE_TO_HEALTH - c.DAMAGE_TO_HEALTH_DELTA
        max_health = c.MAXIMUM_HEALTH + c.MAXIMUM_HEALTH_DELTA

        self.assertLess(max_regeneration, min_damage)
        self.assertAlmostEqual(max_health / (min_damage - max_regeneration), N, delta=1)

    def test_health_regeneration__worst_for_defenders(self):
        # провека, что в худшем для защищающихся случае
        # эмиссар проживёт более N дней при постоянной потере здоровья
        N = 4

        # интервал — день
        max_regeneration = c.HEALTH_REGENERATION_MIN * 24
        max_damage = c.NORMAL_DAMAGE_TO_HEALTH + c.DAMAGE_TO_HEALTH_DELTA
        max_health = c.MAXIMUM_HEALTH - c.MAXIMUM_HEALTH_DELTA

        self.assertLess(max_regeneration, max_damage)
        self.assertAlmostEqual(max_health / (max_damage - max_regeneration), N, delta=1)

    def test_health_regeneration__normal_state(self):
        # провека, как будут вести себя средние прокачанные эмиссары
        N = 8

        # интервал — день
        max_regeneration = c.HEALTH_REGENERATION_MAX * 24
        damage = c.NORMAL_DAMAGE_TO_HEALTH
        health = c.MAXIMUM_HEALTH

        self.assertLess(max_regeneration, damage)

        self.assertAlmostEqual(health / (damage - max_regeneration), N, delta=1)

    def test_health_regeneration__average_state(self):
        # провека, как будут вести себя средние непрокачанные эмиссары
        N = 6

        # интервал — день
        max_regeneration = (c.HEALTH_REGENERATION_MAX + c.HEALTH_REGENERATION_MIN) / 2  * 24
        damage = c.NORMAL_DAMAGE_TO_HEALTH
        health = c.MAXIMUM_HEALTH

        self.assertLess(max_regeneration, damage)
        self.assertAlmostEqual(health / (damage - max_regeneration), N, delta=1)
