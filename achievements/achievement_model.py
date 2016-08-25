#!usr/env/bin python
# -*- coding: utf-8 -*-

import datetime

from mongoengine import *
from modules.starhawks import db

class StarHawksAchievements(db.ContentDocument):
    meta = {
        'allow_inheritance': True,
        'indexes': ['base', 'api_name']
    }

    name = StringField()
    current = IntField(default=0)
    target = IntField()
    api_name = StringField()

    base = BooleanField(default=True)
    rewards = DictField()
    finished = BooleanField(default=False)


class BattleAchievements(StarHawksAchievements):
    modes = ListField(StringField())
    streak = BooleanField()
    faction = ListField(StringField())


class MatchTimeAchievements(StarHawksAchievements):
    # there can be top 100 seven days

    modes = ListField(StringField())
    streak = BooleanField()
    faction = ListField(StringField())
    date_start = DateTimeField()
    timedelta = IntField()

    @property
    def alloted_time(self):
        return self.date_start + datetime.timedelta(seconds=self.timedelta)


class CardCreateAchievements(StarHawksAchievements):
    pass


class CardDisenchantAchievements(StarHawksAchievements):
    pass


class DonateAchievements(StarHawksAchievements):
    pass


class AllQuestAchievements(StarHawksAchievements):
    pass


class QuestAchievements(StarHawksAchievements):
    pass


class AllCardsWithDuplicate(StarHawksAchievements):
    pass


class AllCardsWithoutDuplicate(StarHawksAchievements):
    pass


class BuyBoosterAchievements(StarHawksAchievements):
    pass
