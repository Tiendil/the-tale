# coding: utf-8
import datetime
from game.quests.prototypes import QuestPrototype


class QuestsContainer(object):

    __slots__ = ('updated', 'quests_list')

    def __init__(self):
        self.updated = False
        self.quests_list = []

    def serialize(self):
        return {'quests': [quest.serialize() for quest in self.quests_list]}

    @classmethod
    def deserialize(cls, hero, data):
        obj = cls()
        obj.quests_list = [QuestPrototype.deserialize(data=quest_data) for quest_data in data.get('quests', [])]
        return obj

    def ui_info(self, hero):
        return {'quests': [quest.ui_info(hero) for quest in self.quests_list]}

    def push_quest(self, quest):
        self.updated = True
        self.quests_list.append(quest)

    def pop_quest(self):
        self.updated = True
        return  self.quests_list.pop()

    @property
    def current_quest(self): return self.quests_list[-1]

    @property
    def min_quest_created_time(self):
        if self.has_quests:
            return min(quest.created_at for quest in self.quests_list)
        return datetime.datetime.now()

    @property
    def has_quests(self): return len(self.quests_list)

    @property
    def number(self): return len(self.quests_list)