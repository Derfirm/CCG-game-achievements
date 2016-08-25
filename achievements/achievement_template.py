#!usr/env/bin python
# -*- coding: utf-8 -*-

from modules.starhawks.const import Const, Modes, FactionList, Quality
from modules.starhawks.card import get_all_cards

from collections import namedtuple

battlenamedtuple = namedtuple('BattleAchievements', ['name', 'api_name', 'current', 'target', 'modes', 'faction', 'streak', 'rewards'])
Mtimenamedtuple = namedtuple('MatchTimeAcheievemtns', ['name', 'api_name', 'current', 'target', 'modes', 'faction', 'timedelta', 'rewards'])
CardCreatenamedtuple = namedtuple('CardCreateAchievements', 'name api_name current target rewards')
CardDiseanchantnamedtuple = namedtuple('CardCreateAchievements', 'name api_name current target rewards')
Donatenamedtuple = namedtuple('DonateAchievements', 'name api_name current target rewards')
BuyBoosters = namedtuple('BuyBoostersAchievements', ['name', 'api_name', 'current', 'target', 'rewards'])
Questnametuple = namedtuple('QuestAchievements', 'name api_name current target rewards')
CardCollectionnamedtuple = namedtuple('CardCollectionAchievements', 'name api_name current target rewards')

#pattern for cards reward {Const.CARDS: quality} if need  quality
#other {Const.CARDS: None} for random quality


#### match tuple
win_in_10_rating = battlenamedtuple(name='Winner 10', api_name='wins_total_10', current=0, target=10, modes=[Modes.RATING], faction=[],
                                   streak=False, rewards={Const.CARDS: Quality.CONSCRIPT})
win_in_50_rating = battlenamedtuple(name='Winner 50', api_name='wins_total_50', current=0, target=50, modes=[Modes.RATING], faction=[],
                                   streak=False, rewards={Const.CARDS: Quality.CONSCRIPT})
win_in_200_rating = battlenamedtuple(name='Veteran', api_name='wins_total_200', current=0, target=200, modes=[Modes.RATING], faction=[],
                                   streak=False, rewards={Const.CARDS: Quality.ELITE})

regular_win = battlenamedtuple(name='Good start', api_name='wins_total_3', current=0, target=3,
                               modes=[Modes.RATING, Modes.CASUAL, Modes.PLAY_WITH_BOT, Modes.RAID], faction=[],
                               streak=False, rewards={Const.CARDS: Quality.CONSCRIPT})
elite = battlenamedtuple(name='Elite', api_name='wins_10_row', current=0, target=10,
                               modes=[Modes.RATING], faction=[],
                               streak=True, rewards={Const.CARDS: Quality.ELITE})

hajir_100_faction_rating_win = battlenamedtuple(name='Honorific Torturer', api_name='wins_hajirgog_100', current=0, target=100, modes=[Modes.RATING],
                                                faction=[FactionList.HAJIRGOG], streak=False, rewards={Const.CARDS: Quality.ELITE})

annu_100_faction_rating_win = battlenamedtuple(name='Mystery Deity', api_name='wins_annunaki_100', current=0, target=100, modes=[Modes.RATING],
                                                faction=[FactionList.ANNUNAKI], streak=False, rewards={Const.CARDS: Quality.ELITE})

shanti_100_faction_rating_win = battlenamedtuple(name='Perficient Magister', api_name='wins_shanti_100', current=0, target=100, modes=[Modes.RATING],
                                                faction=[FactionList.SHANTI], streak=False, rewards={Const.CARDS: Quality.ELITE})

terrain_100_faction_rating_win = battlenamedtuple(name='Defender of Earth', api_name='wins_terrain_100', current=0, target=100, modes=[Modes.RATING],
                                                faction=[FactionList.TERRAN], streak=False, rewards={Const.CARDS: Quality.ELITE})

cons_100_faction_rating_win = battlenamedtuple(name='Big Man', api_name='wins_consortium_100', current=0, target=100, modes=[Modes.RATING],
                                                faction=[FactionList.CONSORTIUM], streak=False, rewards={Const.CARDS: Quality.ELITE})

hier_100_faction_rating_win = battlenamedtuple(name='Venerable Master', api_name='wins_hierarchy_100', current=0, target=100, modes=[Modes.RATING],
                                                faction=[FactionList.HIERARCHY], streak=False, rewards={Const.CARDS: Quality.ELITE})

### disenchant
first_disenchant = CardDiseanchantnamedtuple(name='First disenchanted', api_name='first_disenchant', current=0, target=1, rewards={Const.INGAME_DUST: 25})
disenchant_master = CardDiseanchantnamedtuple(name='Master disenchant', api_name='master_disenchant', current=0, target=10, rewards={Const.INGAME_DUST: 100})

### card create
begginer_enchantment = CardCreatenamedtuple(name='Fusion Apprentice', api_name='fusion_apprentice', current=0, target=1, rewards={Const.INGAME_DUST: 10})
master_enchantment = CardCreatenamedtuple(name='Fusion Journeysman', api_name='fusion_journeysman', current=0, target=10, rewards={Const.INGAME_DUST: 20})
sunt_engeneer = CardCreatenamedtuple(name='Fusion Engineer', api_name='fusion_engineer', current=0, target=100, rewards={Const.INGAME_DUST: 30})


#donate
premium = Donatenamedtuple(name='Premium', api_name='premium', current=0, target=1, rewards={Const.INGAME_DUST: 50})
vip = Donatenamedtuple(name='VIP', api_name='vip', current=0, target=50, rewards={Const.INGAME_DUST: 250})

#boosters buy
boosters = BuyBoosters(name='VIP', api_name='vip', current=0, target=500, rewards={Const.INGAME_DUST: 250})

#mtime
min_ingame_100 = Mtimenamedtuple(name='ZEAL', api_name='zeal_1', current=0, target=60*100, modes=[Modes.RATING, Modes.CASUAL, Modes.RAID, Modes.PLAY_WITH_BOT],
                                 faction=[], timedelta=60*60*24*7, rewards={Const.INGAME_MONEY: 10})
min_ingame_300 = Mtimenamedtuple(name='ZEAL II', api_name='zeal_2', current=0, target=60*300, modes=[Modes.RATING, Modes.CASUAL, Modes.RAID, Modes.PLAY_WITH_BOT],
                                 faction=[], timedelta=60*60*24*7, rewards={Const.INGAME_MONEY: 35})
min_ingame_500 = Mtimenamedtuple(name='ZEAL III', api_name='zeal_3', current=0, target=60*500, modes=[Modes.RATING, Modes.CASUAL, Modes.RAID, Modes.PLAY_WITH_BOT],
                                 faction=[], timedelta=60*60*24*7, rewards={Const.INGAME_MONEY: 50})

#quests
all_quests_today = Questnametuple(name='Bounty Hunter', api_name='bounty_hunter_1', current=0, target=0, rewards={Const.INGAME_DUST: 5})
quests_30 = Questnametuple(name='Bounty Hunter II', api_name='bounty_hunter_2', current=0, target=30, rewards={Const.INGAME_DUST: 15})
quests_100 = Questnametuple(name='Bounty Hunter', api_name='bounty_hunter_3', current=0, target=100, rewards={Const.INGAME_DUST: 25})

# TOTAL_CARDS_INGAME = StarHawksCard.objects(standalone=True, clone=False).count()
TOTAL_CARDS_INGAME = len(get_all_cards(standalone=True))

#card with duplicates
card10_with_duplicate = CardCollectionnamedtuple(name='Squirel', api_name='squirel', current=0, target=10, rewards={Const.INGAME_MONEY: 10})
card30_with_duplicate = CardCollectionnamedtuple(name='Collector', api_name='collector', current=0, target=30, rewards={Const.INGAME_MONEY: 10})

card35_without_duplicate = CardCollectionnamedtuple(name='Completist', api_name='completist', current=0, target=int(0.35*TOTAL_CARDS_INGAME), rewards={Const.INGAME_MONEY: 25})
card50_without_duplicate = CardCollectionnamedtuple(name='Respectable Completist', api_name='respectable_completist', current=0, target=int(0.50*TOTAL_CARDS_INGAME), rewards={Const.INGAME_MONEY: 50})
card80_without_duplicate = CardCollectionnamedtuple(name='Great Completist', api_name='great_completist', current=0, target=int(0.80*TOTAL_CARDS_INGAME), rewards={Const.INGAME_MONEY: 50})
card100_without_duplicate = CardCollectionnamedtuple(name='PARAGONIST', api_name='paragonist', current=0, target=int(1*TOTAL_CARDS_INGAME), rewards={Const.INGAME_MONEY: 100})



class AchievementsTemplate(object):

    match_achievements = [
        win_in_10_rating, win_in_50_rating, win_in_200_rating, regular_win,
        hajir_100_faction_rating_win, hier_100_faction_rating_win, annu_100_faction_rating_win,
        shanti_100_faction_rating_win, terrain_100_faction_rating_win, cons_100_faction_rating_win, elite
    ]

    disenchant_achievements = [first_disenchant, disenchant_master]

    cardcreate_achievements = [begginer_enchantment, master_enchantment, sunt_engeneer]
    donate_achievements = [premium]
    shop = [boosters]
    match_times = [min_ingame_100, min_ingame_300, min_ingame_500]
    quests = [quests_30, quests_100]
    all_quest = [all_quests_today]
    card_with_dupl = [card10_with_duplicate, card30_with_duplicate]
    card_without_dupl = [card35_without_duplicate, card50_without_duplicate, card80_without_duplicate, card100_without_duplicate]

    list_common_tuples = match_achievements + cardcreate_achievements + donate_achievements + shop + \
                         match_times + quests + all_quest + card_with_dupl + card_without_dupl