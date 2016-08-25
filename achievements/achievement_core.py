#!usr/env/bin python
# -*- coding: utf-8 -*-

import copy
import random
import datetime

from achievements.achievement_model import *
from achievements import *

get_all_cards = 300

class AchievementsController(object):
    ModelType = None

    @staticmethod
    def _push_to_analytics(user, rewards):
        for key, value in rewards.iteritems():
            pass

    @classmethod
    def is_process_available(cls, achievement_template, user, send_event, data=None):
        if achievement_template.api_name in user.unlocked_achievements:
            return False
        if achievement_template.target == 1:
            cls.fast_processing(achievement_template, user, send_event)
            return False
        return True

    @classmethod
    def fast_processing(cls, achievement_template, user, send_event):
        cls.finish_achievement(achievement_template, user, send_event)

    @classmethod
    def process(cls, achievement_template, user, points, send_event, *args, **kwargs):
        if not cls.is_process_available(achievement_template, user, send_event):
            return

        model_obj = cls.find(achievement_template.api_name, user) if achievement_template.api_name in user.achievements_in_progress \
            else cls.generate(achievement_template, user)
        model_obj.current += points
        # finished check for avoid duplicate rewards

        if model_obj.current >= achievement_template.target and not model_obj.finished:
            cls.finish_achievement(achievement_template, user, send_event, model_obj)
        model_obj.save()

    @classmethod
    def _populate_fields(cls, achievement_template):
        model_obj = cls.ModelType(**achievement_template._asdict())
        # TODO remove base flag
        model_obj.base = False
        return model_obj

    @classmethod
    def generate(cls, achievement_template, user):
        model_obj = cls._populate_fields(achievement_template)
        user.achievements.append(model_obj)
        user.achievements_in_progress.append(achievement_template.api_name)
        return model_obj

    @staticmethod
    def find(api_name, user):
        for achievement in user.achievements:
            if achievement.api_name == api_name:
                return achievement

    @staticmethod
    def get_rewards(rewards):
        prepared_rewards = copy.deepcopy(rewards)
        if Const.CARDS in prepared_rewards:
            quality = prepared_rewards[Const.CARDS]
            if quality:
                card = random.choice(get_all_cards(quality=[quality]))
            else:
                card = random.choice(get_all_cards())
            prepared_rewards[Const.CARDS] = {card.uniquestringid: 1}
        return prepared_rewards

    @classmethod
    def to_event(cls, ach_name, rewards):
        response = achievement.AchievementCall()
        response.name = prepare_translate(ach_name)
        for key, value in rewards.iteritems():
            if key == Const.INGAME_DUST:
                response.rewards.append({'type': "ScrapReward", "count": value})
            elif key == Const.INGAME_MONEY:
                response.rewards.append{'type': "MoneyReward", 'count': value})
            elif key == Const.BOOSTERS:
                response.rewards.append({'type': "BoosterReward", 'count': value})
            elif key == Const.CARDS:
                for uid, _ in rewards[Const.CARDS].iteritems():
                    response.rewards.append('type': "CardReward", 'uniquestringid': uid})
        return response

    @classmethod
    def finish_achievement(cls, achievement_template, user, send_event, model_obj=None):
        if model_obj:
            user.unlocked_achievement(model_obj)
        # fast unlocker, without create Document.
        else:
            user.fast_unlocked_achievement(achievement_template)
        prepared_rewards = cls.get_rewards(achievement_template.rewards)
        user.save_rewards(prepared_rewards)
        cls._push_to_analytics(user, prepared_rewards)
        send_event(cls.to_event(achievement_template.name, prepared_rewards), channel=user.uid)
        if model_obj:
            model_obj.finished = True


class CardCreate(AchievementsController):
    ModelType = CardCreateAchievements


class Quests(AchievementsController):
    ModelType = QuestAchievements



class Donate(AchievementsController):
    ModelType = DonateAchievements


class BuyBooster(AchievementsController):
    ModelType = BuyBoosterAchievements


class Battle(AchievementsController):
    ModelType = BattleAchievements

    @classmethod
    def is_process_available(cls, achievement_template, user, send_event, data=None):
        result = super(Battle, cls).is_process_available(achievement_template, user, send_event)
        if achievement_template.faction and data.hero_unit.hero.faction.uniquestringid not in achievement_template.faction:
            result = False
        return result

    @classmethod
    def process(cls, achievement_template, user, points, send_event, gamemode, position, data, *args, **kwargs):

        if not cls.is_process_available(achievement_template, user, send_event, data):
            return

        if gamemode in achievement_template.modes:
            model_obj = cls.find(achievement_template.api_name, user) if achievement_template.api_name in user.achievements_in_progress \
                else cls.generate(achievement_template, user)
            if position == 'winner':
                model_obj.current += points

                if model_obj.current >= achievement_template.target and not model_obj.finished:
                    cls.finish_achievement(achievement_template, user, send_event, model_obj)

            elif position == 'looser' and achievement_template.streak:
                model_obj.current = 0
            model_obj.save()


class AllCards(AchievementsController):
    ModelType = AllCardsWithDuplicate

    @classmethod
    def process(cls, achievement_template, user, points, send_event, *args, **kwargs):
        if not cls.is_process_available(achievement_template, user, send_event):
            return

        if user.available_cards:
            model_obj = cls.find(achievement_template.api_name, user) if achievement_template.api_name in user.achievements_in_progress \
                else cls.generate(achievement_template, user)
            model_obj.current = sum(user.available_cards.values())
            if model_obj.current >= achievement_template.target and not model_obj.finished:
                cls.finish_achievement(achievement_template, user, send_event, model_obj)
            model_obj.save()


class UniqueCards(AchievementsController):
    ModelType = AllCardsWithoutDuplicate

    @classmethod
    def process(cls, achievement_template, user, points, send_event, *args, **kwargs):

        if not cls.is_process_available(achievement_template, user, send_event):
            return

        if user.available_cards:
            model_obj = cls.find(achievement_template.api_name, user) if achievement_template.api_name in user.achievements_in_progress \
                else cls.generate(achievement_template, user)

            model_obj.current = len(user.available_cards)
            if model_obj.current >= model_obj.target and not model_obj.finished:
                cls.finish_achievement(achievement_template, user, send_event, model_obj)
            model_obj.save()

class AllQuest(AchievementsController):
    ModelType = AllQuestAchievements

    @classmethod
    def process(cls, achievement_template, user, points, send_event, *args, **kwargs):
        if not cls.is_process_available(achievement_template, user, send_event):
            return

        # finish all quests for today
        model_obj = cls.find(achievement_template.api_name, user) if achievement_template.api_name in user.achievements_in_progress \
            else cls.generate(achievement_template, user)
        if not user.quests or (len(user.quests) == 1 and user.quests[0].progress >= user.quests[0].necessary):
            cls.finish_achievement(achievement_template, user, send_event, model_obj)
            model_obj.save()


class MatchTime(AchievementsController):
    ModelType = MatchTimeAchievements

    @classmethod
    def is_process_available(cls, achievement_template, user, send_event, data=None):
        result = super(MatchTime, cls).is_process_available(achievement_template, user, send_event)
        if achievement_template.faction and data.hero_unit.hero.faction.uniquestringid not in achievement_template.faction:
            result = False
        return result

    @classmethod
    def _populate_fields(cls, achievement_template):
        model_obj = super(MatchTime, cls)._populate_fields(achievement_template)
        model_obj.date_start = datetime.datetime.utcnow()
        return model_obj

    @classmethod
    def process(cls, achievement_template, user, mtime, send_event, gamemode, position, data):
        if not cls.is_process_available(achievement_template, user, send_event, data):
            return

        if gamemode in achievement_template.modes:
            model_obj = cls.find(achievement_template.api_name,
                                 user) if achievement_template.api_name in user.achievements_in_progress \
                else cls.generate(achievement_template, user)

            model_obj.current += int(mtime())
            if model_obj.current >= achievement_template.target and model_obj.alloted_time >= datetime.datetime.utcnow() and not model_obj.finished:
                cls.finish_achievement(achievement_template, user, send_event, model_obj)
            elif model_obj.alloted_time < datetime.datetime.utcnow():
                model_obj.current = 0
                model_obj.date_start = datetime.datetime.utcnow()
            model_obj.save()

__all__ = (CardCreate, MatchTime, Quests,  CardCreate, AllCards, Battle, Donate, BuyBooster)
