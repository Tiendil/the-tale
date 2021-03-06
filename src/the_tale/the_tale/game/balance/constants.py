
import smart_imports

smart_imports.all()


TIME_TO_LVL_DELTA: float = 7  # разница во времени получения двух соседних уровней
TIME_TO_LVL_MULTIPLIER: float = 1.02  # множитель опыта, возводится в степень уровня

INITIAL_HP: int = 500  # начальное здоровье героя

HP_PER_LVL: int = 50  # бонус к здоровью на уровень

MOB_HP_MULTIPLIER: float = 0.25  # какой процент здоровье среднего моба составляет от здоровья героя
BOSS_HP_MULTIPLIER: float = 0.5  # какой процент здоровье среднего моба составляет от здоровья героя

TURN_DELTA: int = 10  # в секундах - задержка одного хода

TURNS_IN_HOUR: float = 60.0 * 60 / TURN_DELTA  # количество ходов в 1 часе

POWER_PER_LVL: int = 1  # значение "чистой" силы героя (т.е. без артефактов)

EQUIP_SLOTS_NUMBER: int = 11  # количество слотов экипировки

# за скорость получения артефактов принимаем скорость получения их из лута
# остальные способы получения (покупка, квесты) считаем флуктуациями
ARTIFACTS_LOOT_PER_DAY: float = 2.0  # количество новых артефактов, в реальный день
ARTIFACT_FOR_QUEST_PROBABILITY: float = 0.2  # вероятность получить артефакт в награда за квест

# Доли лута и артефактов в доходах героя. В артефакты влючены и награды за задания.
INCOME_LOOT_FRACTION: float = 0.6
INCOME_ARTIFACTS_FRACTION: float = 1.0 - INCOME_LOOT_FRACTION

# магическое число — ожидаемое количество выполненных героем квестов в день
EXPECTED_QUESTS_IN_DAY: float = 2.0

# количество поломок артефактов в день, расчитывается так, чтобы за 3 недели в идеальном случае была обновлена вся экипировка
ARTIFACTS_BREAKING_SPEED: float = EQUIP_SLOTS_NUMBER / (3 * 7.0)

EQUIPMENT_BREAK_FRACTION: float = 0.5  # доля артифактов в экипировке, которые могут сломаться
NORMAL_SLOT_REPAIR_PRIORITY: float = 1.0  # приоритет починки обычного слота
SPECIAL_SLOT_REPAIR_PRIORITY: float = 2.0  # приоритет починки слота из предпочтения

EXP_PER_HOUR: int = 10  # опыт в час
EXP_PER_QUEST_FRACTION: float = 0.33  # разброс опыта за задание

COMPANIONS_BONUS_EXP_FRACTION: float = 0.2  # доля бонусного опыта, которую могут приносить спутники

# с учётом возможных способностей (т.е. считаем, что при нужных абилках у премиума скорость получения опыта будет 1.0)
EXP_FOR_PREMIUM_ACCOUNT: float = 1.0  # модификатор опыта для премиум аккаунтов
EXP_FOR_NORMAL_ACCOUNT: float = 0.66  # модификатор опыта для обычных акканутов

HERO_MOVE_SPEED: float = 0.1  # базовая скорость героя расстояние в ход

BATTLE_LENGTH: int = 16  # ходов - средняя длительность одного боя (количество действий в бой)
INTERVAL_BETWEEN_BATTLES: int = 3  # ходов - время, между двумя битвами

BATTLES_BEFORE_HEAL: int = 8  # количество боёв в непрерывной цепочке битв

MOVE_TURNS_IN_ACTION_CYCLE: int = INTERVAL_BETWEEN_BATTLES * BATTLES_BEFORE_HEAL

DISTANCE_IN_ACTION_CYCLE: float = HERO_MOVE_SPEED * MOVE_TURNS_IN_ACTION_CYCLE

HEAL_TIME_FRACTION: float = 0.2  # доля времени от цепочки битв, которую занимает полный отхил героя
HEAL_STEP_FRACTION: float = 0.2  # разброс регенерации за один ход

HEALTH_IN_SETTLEMENT_TO_START_HEAL_FRACTION: float = 0.33  # если у героя здоровья меньше, чем указанная доля и он в городе, то он будет лечиться
HEALTH_IN_MOVE_TO_START_HEAL_FRACTION: float = 2 * (1.0 / BATTLES_BEFORE_HEAL)  # если у героя здоровья меньше, чем указанная доля и он в походе, то он будет лечиться

TURNS_TO_IDLE: int = 6  # количество ходов на уровень, которое герой бездельничает в соответствующей action
TURNS_TO_RESURRECT: int = TURNS_TO_IDLE * 3  # количество ходов на уровень, необходимое для воскрешения


GET_LOOT_PROBABILITY: float = 0.50  # вероятность получить добычу после боя, если не получен артефакт

# вероятности получить разный тип добычи

EPIC_ARTIFACT_PROBABILITY: float = 0.005
RARE_ARTIFACT_PROBABILITY: float = 0.05
NORMAL_ARTIFACT_PROBABILITY: float = 1 - RARE_ARTIFACT_PROBABILITY - EPIC_ARTIFACT_PROBABILITY

NORMAL_LOOT_COST: float = 1  # стоимость разной добычи на единицу уровня

MAX_BAG_SIZE: int = 12  # максимальный размер рюкзака героя
BAG_SIZE_TO_SELL_LOOT_FRACTION: float = 0.33  # процент заполненности рюкзака, после которого герой начнёт продавать вещи

# относительные размеры различных трат

BASE_EXPERIENCE_FOR_MONEY_SPEND: int = int(24 * EXP_PER_HOUR * 0.4)
EXPERIENCE_DELTA_FOR_MONEY_SPEND: float = 0.5

POWER_TO_LVL: float = EQUIP_SLOTS_NUMBER  # бонус к ожидаемой силе на уровнеь героя

# Разброс силы артефактов делаем от -ItemPowerDelta до +ItemPowerDelta.
# за базу берём количество слотов, т.е., теоретически, может не быть предметов с повторяющейся силой
# что бы не вводить дизбаланса, надо на маленьких уровнях уменьшать делту, что бу разница уровня предмета и дельты была неменьше единицы
ARTIFACT_POWER_DELTA: float = 0.2  # дельта, на которую может изменяться сила артифакта

ARTIFACT_BETTER_MIN_POWER_DELTA: int = 5  # минимальная дельта, на которую может изменятся сила лучшего артефакта (для магазина)

# ходов - длинна непрерывной цепочки боёв до остановки на лечение
BATTLES_LINE_LENGTH: int = BATTLES_BEFORE_HEAL * (BATTLE_LENGTH + INTERVAL_BETWEEN_BATTLES) - INTERVAL_BETWEEN_BATTLES

# количество битв в ход в промежутке непрерывных боёв
BATTLES_PER_TURN: float = 1.0 / (INTERVAL_BETWEEN_BATTLES + 1)
WHILD_BATTLES_PER_TURN_BONUS: float = 0.05

# максимально допустимое значение вероятности битв в час
MAX_BATTLES_PER_TURN: float = 0.9

COMPANIONS_DEFENDS_IN_BATTLE: float = 1.5  # среднее количество «защит» героя средним спутником за 1 бой
COMPANIONS_HEAL_FRACTION: float = 0.05  # доля действия уход за спутнкиком со средним количеством здоровья от всех действий героя

HEAL_LENGTH: int = math.floor(BATTLES_LINE_LENGTH * HEAL_TIME_FRACTION)  # ходов - длительность лечения героя

ACTIONS_CYCLE_LENGTH: int = math.ceil((BATTLES_LINE_LENGTH + HEAL_LENGTH) / (1 - COMPANIONS_HEAL_FRACTION))  # ходов - длинна одного "игрового цикла" - цепочка боёв + хил

MOVE_TURNS_IN_HOUR: float = MOVE_TURNS_IN_ACTION_CYCLE * (ACTIONS_CYCLE_LENGTH * TURN_DELTA / float(60 * 60))

# примерное количество боёв, которое будет происходить в час игрового времени
BATTLES_PER_HOUR: float = TURNS_IN_HOUR * (float(BATTLES_BEFORE_HEAL) / ACTIONS_CYCLE_LENGTH)

# вероятность выпаденя артефакта из моба (т.е. вероятноть получить артефакт после боя)
ARTIFACTS_PER_BATTLE: float = ARTIFACTS_LOOT_PER_DAY / (BATTLES_PER_HOUR * 24)

# вероятность сломать артефакт после боя
ARTIFACTS_BREAKS_PER_BATTLE: float = ARTIFACTS_BREAKING_SPEED / (BATTLES_PER_HOUR * 24)

ARTIFACT_FROM_PREFERED_SLOT_PROBABILITY: float = 0.25  # вероятность выбрать для покупки/обновления артефакт из предпочитаемого слота

ARTIFACT_INTEGRITY_DAMAGE_PER_BATTLE: int = 1  # уменьшение целостности артефактов за бой
ARTIFACT_INTEGRITY_DAMAGE_FOR_FAVORITE_ITEM: float = 0.5  # модификатор повреждений целостности любимого предмета

_INTEGRITY_LOST_IN_DAY = BATTLES_PER_HOUR * 24 * ARTIFACT_INTEGRITY_DAMAGE_PER_BATTLE

ARTIFACT_RARE_MAX_INTEGRITY_MULTIPLIER: float = 1.5  # коофициент увеличения максимальной целостности для редких артефактов
ARTIFACT_EPIC_MAX_INTEGRITY_MULTIPLIER: float = 2  # коофициент увеличения максимальной целостности для эпических артефактов
ARTIFACT_MAX_INTEGRITY_DELTA: float = 0.25  # разброс допустимой максимальной целостности

ARTIFACT_MAX_INTEGRITY: int = int(round(_INTEGRITY_LOST_IN_DAY * 30, -3))  # максимальная целостность обычного артефакта
ARTIFACT_SHARP_MAX_INTEGRITY_LOST_FRACTION: float = 0.04  # доля максимальной целостности, теряемая при заточке
ARTIFACT_INTEGRITY_SAFE_BARRIER: float = 0.2  # доля от максимальной целостности, артефакт не может сломаться, если его целостность отличается от максимальной меньше чем на эту долю
ARTIFACT_BREAK_POWER_FRACTIONS: Tuple[float, float] = (0.2, 0.3)  # на сколько артефакт может сломаться за раз
ARTIFACT_BREAK_INTEGRITY_FRACTIONS: Tuple[float, float] = (0.1, 0.2)  # на сколько артефакт может сломаться за раз

PREFERED_MOB_LOOT_PROBABILITY_MULTIPLIER: float = 2.0  # множитель вероятности получения лута из любимой добычи

DAMAGE_TO_HERO_PER_HIT_FRACTION: float = 1.0 / (BATTLES_BEFORE_HEAL * (BATTLE_LENGTH / 2 - COMPANIONS_DEFENDS_IN_BATTLE))  # доля урона, наносимого герою за удар
DAMAGE_TO_MOB_PER_HIT_FRACTION: float = 1.0 / (BATTLE_LENGTH / 2)  # доля урона, наносимого мобу за удар
DAMAGE_DELTA: float = 0.2  # разброс в значениях урона [1-DAMAGE_DELTA, 1+DAMAGE_DELTA]

DAMAGE_CRIT_MULTIPLIER: float = 2.0  # во сколько раз увеличивается урон при критическом ударе

# таким образом, напрашиваются следующие параметры мобов:
# - здоровье, в долях от среднемобского - чем больше его, тем  дольше моб живёт
#  - инициатива, в долях относительно геройской - чем больше, тем чаще моб ходит
#  - урон, в долях от среднемобского - чем больше, тем больнее бьёт
#  - разброс урона, в долях от среднего - декоративный параметр, т.к. в итоге будет средний урон наноситься
# так как все параметры измеряются в долях, то сложность моба можно высчитать как hp * initiative * damage = 1 для среднего моба
# моб со всеми парамтрами, увеличеными на 10% будет иметь сложность 1.1^3 ~ 1.33
# соответственно, вводня для каждого параметра шаг в 0.1 и скалируя от 0.5 до 1.5, получим 11^3 вариантов параметров (и, соответственно поведения)
# сложность мобов в этом случае будет изменяться от 0.5^3 до 1.5^3 ~ (0.125, 3.375)
#
# возникает проблема обеспечения равномерности прокачки героев на разных территориях - для полностью честных условий необходимо обеспечить одинаковую сложность мобов,
# альтернативный вариант - изменять количесво опыта, даваемого за моба, в зависимости от его сложности, этот вариант кажется как более логичным с точки зрения игрока, так и простым в реализации, на нём и остановимся
#
# расчёт прочей добычи и золота: добыча/трата

# считаем, что если герой не выбил артефакт, то у него есть вероятность выбить добычу
# добычу делим на обычную, редкую и очень редкую
# добыча является основным источником дохода, вырученное за его продажу золото является функцией от уровня и редкости - т.е. есть три фунции от уровня
# добыча, как и мобы, организован в список, отсортированый по уровню, на котором он становится доступным, это позволит открывать игрокам новый контент, а так же сделать разброс цен

##########################
# разные левые "неприкаянные" константы
##########################

DESTINY_POINT_IN_LEVELS: int = 5  # раз в сколько уровней давать очко абилок
SPEND_MONEY_FOR_HEAL_HEALTH_FRACTION: float = 0.75  # герой будет тратить деньги на лечение, когда его здоровье будет меньше этого параметра

######################################
# зависимость изменения скорости от изменения безопасности
# при фиксированном количестве боёв за цикл движения, изменение скорости эквивалентное изменению вероятности боя
# можно получить исходя из того, что пройденные пути должны быть равными (т.к. количество ходов движения пренебрежительно мало по сравнению с прочими ходами)
# так же можно пренебречь количеством отдыха
# уравнение:
#   y — изменение скорости
#   x — изменение вероятности
#   1 / battle_probability - 1 — количество ходов на одну битву
#   (1 + y) * speed * (1 / battle_probability - 1) = speed * (1 / (battle_probability - x) - 1)
#
#   y = -x / ((battle_probability + x)*(1 - battle_probability))
#
# Так как полученный коофициент зависит от вероятности боя и дельты, а они варьируется, нам необходимо выбрать для «наиболее общего случая»:
# - фиксированную вероятность
# - фиксированную дельту
# которые послужит базой для расчёта коофициента пересчёта безопасности в транспорт

def speed_from_safety(danger: float, battles_per_turn: float) -> float:
    return -danger / ((battles_per_turn + danger) * (1 - battles_per_turn))


_SAFETY_TO_TRANSPORT: float = round(-speed_from_safety(0.01, BATTLES_PER_TURN) / 0.01)

##########################
# Карта
##########################

MINIMUM_QUESTS_REGION_SIZE: int = 15
DEFAULT_QUESTS_REGION_SIZE: int = 25

MAP_SYNC_TIME_HOURS: int = 1
MAP_SYNC_TIME: int = int(TURNS_IN_HOUR * MAP_SYNC_TIME_HOURS)  # синхронизируем карту раз в N часов

CELL_SAFETY_MIN: float = 0.05
CELL_SAFETY_MAX: float = 0.95

CELL_SAFETY_DELTA: float = 0.01

CELL_SAFETY_NO_PATRULES: float = -0.5

CELL_TRANSPORT_MIN: float = CELL_SAFETY_MIN * _SAFETY_TO_TRANSPORT
CELL_TRANSPORT_DELTA: float = CELL_SAFETY_DELTA * _SAFETY_TO_TRANSPORT

CELL_TRANSPORT_MAGIC: float = -CELL_TRANSPORT_DELTA

CELL_TRANSPORT_HAS_MAIN_ROAD: float = 0.5
CELL_TRANSPORT_HAS_OFF_ROAD: float = CELL_TRANSPORT_HAS_MAIN_ROAD / 2

# дорога по клетке без штрафов и модификаторов должна давать 100% скорость
CELL_TRANSPORT_BASE: float = 1.0 - CELL_TRANSPORT_HAS_MAIN_ROAD

PATH_MODIFIER_MINOR_DELTA: float = 0.05
PATH_MODIFIER_NORMAL_DELTA: float = 0.15
PATH_MODIFIER_MAJOR_DELTA: float = 0.3

PATH_MINIMUM_COST_MULTIPLIER: float = 0.25

##########################
# Задания
##########################

QUESTS_PILGRIMAGE_FRACTION: float = 0.025  # вероятность отправить героя в паломничество

##########################
# споособности
##########################

ABILITIES_ACTIVE_MAXIMUM: int = 5
ABILITIES_PASSIVE_MAXIMUM: int = 2

ABILITIES_BATTLE_MAXIMUM: int = ABILITIES_ACTIVE_MAXIMUM + ABILITIES_PASSIVE_MAXIMUM
ABILITIES_NONBATTLE_MAXIMUM: int = 4
ABILITIES_COMPANION_MAXIMUM: int = 4

ABILITIES_OLD_ABILITIES_FOR_CHOOSE_MAXIMUM: int = 2
ABILITIES_FOR_CHOOSE_MAXIMUM: int = 4

##########################
# Черты
##########################

HABITS_NEW_HERO_POINTS: int = 200

HABITS_BORDER: int = 1000  # модуль максимального значения черты
HABITS_RIGHT_BORDERS: List[int] = [-700, -300, -100, 100, 300, 700, 1001]  # правые границы черт
HABITS_ACTIVE_DELTA: float = 20.0  # за выбор в задании игроком
HABITS_PASSIVE_DELTA: float = 0.05 * HABITS_ACTIVE_DELTA  # за неверный выбор героем

HABITS_QUEST_ACTIVE_PREMIUM_MULTIPLIER: float = 1.5  # бонус к начисляемому влиянию за выбор игрока для подписчиков

KILL_BEFORE_BATTLE_PROBABILITY: float = 0.05  # вероятность убить мобы в начале боя
PICKED_UP_IN_ROAD_TELEPORT_LENGTH: float = 1.0
# бонус к скорости передвижения, эквивалентный вероятности убить моба
PICKED_UP_IN_ROAD_SPEED_BONUS: float = BATTLES_PER_TURN * KILL_BEFORE_BATTLE_PROBABILITY * _SAFETY_TO_TRANSPORT
PICKED_UP_IN_ROAD_PROBABILITY: float = PICKED_UP_IN_ROAD_SPEED_BONUS / PICKED_UP_IN_ROAD_TELEPORT_LENGTH

HABIT_QUEST_PRIORITY_MODIFIER: float = 1.0  # модификатор приоритета выбора заданий от предпочтений

MONSTER_TYPE_BATTLE_CRIT_MAX_CHANCE: float = 0.02  # вероятность крита по типу монстра, если все монстры этого типа

HABIT_QUEST_REWARD_MAX_BONUS: float = 1.0  # максимальный бонус к награде за задание при выборе, совпадающем с чертой
HABIT_LOOT_PROBABILITY_MODIFIER: float = 1.2  # бонус к вероятности получить любой лут

PEACEFULL_BATTLE_PROBABILITY: float = 0.05  # вероятность мирно разойтись с монстром, если все можно расходиться со всеми типами монстров

EXP_FOR_KILL: int = 10  # средний опыт за убийство монстра
EXP_FOR_KILL_DELTA: float = 0.3  # разброс опыта за убийство

_KILLS_IN_HOUR: float = TURNS_IN_HOUR / ACTIONS_CYCLE_LENGTH * BATTLES_BEFORE_HEAL

# вероятность получить опыт за убийство моба
EXP_FOR_KILL_PROBABILITY: float = (0.1 * EXP_PER_HOUR) / (EXP_FOR_KILL * _KILLS_IN_HOUR)

###########################
# события для черт
###########################

HABIT_EVENTS_IN_DAY: float = 1.33  # количество событий в сутки
HABIT_EVENTS_IN_TURN: float = HABIT_EVENTS_IN_DAY / 24 / TURNS_IN_HOUR  # вероятность события в ход

HABIT_MOVE_EVENTS_IN_TURN: float = HABIT_EVENTS_IN_TURN / (BATTLES_BEFORE_HEAL * INTERVAL_BETWEEN_BATTLES / float(ACTIONS_CYCLE_LENGTH))  # вероятность события при движении
HABIT_IN_PLACE_EVENTS_IN_TURN: float = HABIT_MOVE_EVENTS_IN_TURN * 10  # вероятность события в городе (с учётом имплементации)

# приоритеты событий с разными эффектами
HABIT_EVENT_NOTHING_PRIORITY: float = 4.0
HABIT_EVENT_MONEY_PRIORITY: float = 4.0
HABIT_EVENT_ARTIFACT_PRIORITY: float = 2.0
HABIT_EVENT_EXPERIENCE_PRIORITY: float = 1.0

# получаемые деньги могут быть эквиваленты цене продажи артефакта
# артефакт может создаваться обычным (как при луте)
# считаем, что можем позволить ускорить прокачку на 5%
_HABIT_EVENT_TOTAL_PRIORITY: float = HABIT_EVENT_NOTHING_PRIORITY + HABIT_EVENT_MONEY_PRIORITY + HABIT_EVENT_ARTIFACT_PRIORITY + HABIT_EVENT_EXPERIENCE_PRIORITY
HABIT_EVENT_EXPERIENCE: int = int(0.05 * (24.0 * EXP_PER_HOUR) / (HABIT_EVENTS_IN_DAY * HABIT_EVENT_EXPERIENCE_PRIORITY / _HABIT_EVENT_TOTAL_PRIORITY))
HABIT_EVENT_EXPERIENCE_DELTA: float = 0.5  # разброс опыта

###########################
# pvp
###########################

DAMAGE_PVP_ADVANTAGE_MODIFIER: float = 0.5  # на какую долю изменяется урон при максимальной разнице в преимуществе между бойцами
DAMAGE_PVP_FULL_ADVANTAGE_STRIKE_MODIFIER: float = 5.0  # во сколько раз увеличится урон удара при максимальном преимушестве

PVP_MAX_ADVANTAGE_STEP: float = 0.25

PVP_ADVANTAGE_BARIER: float = 0.95
PVP_EFFECTIVENESS_EXTINCTION_FRACTION: float = 0.1

PVP_EFFECTIVENESS_STEP: float = 10
PVP_EFFECTIVENESS_INITIAL: float = 300

###########################
# города
###########################

PLACE_MIN_PERSONS: int = 2
PLACE_MAX_PERSONS: List[int] = [0, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6]
PLACE_ABSOLUTE_MAX_PERSONS: int = PLACE_MAX_PERSONS[-1]

PLACE_MIN_STABILITY: float = 0.0
PLACE_MIN_CULTURE: float = 0.2

PLACE_BASE_STABILITY: float = 1.0

PLACE_MAX_SIZE: int = 10
PLACE_MAX_ECONOMIC: int = 10
PLACE_MAX_FRONTIER_ECONOMIC: int = 5

PLACE_NEW_PLACE_LIVETIME: int = 2 * 7 * 24 * 60 * 60

PLACE_MONEY_HISTORY_WEEKS: int = 6  # количество недель, которое хранится влияние города
PLACE_MONEY_HISTORY_LENGTH: int = int(PLACE_MONEY_HISTORY_WEEKS * 7 * 24 * TURNS_IN_HOUR)  # в ходах
PLACE_MONEY_RECALCULATE_STEPS: float = PLACE_MONEY_HISTORY_LENGTH / MAP_SYNC_TIME
PLACE_MONEY_REDUCE_FRACTION: float = math.pow(0.01, 1.0 / PLACE_MONEY_RECALCULATE_STEPS)

PLACE_TYPE_NECESSARY_BORDER: int = 75
PLACE_TYPE_ENOUGH_BORDER: int = 50

PLACE_GOODS_BONUS: int = 100  # в час, соответственно PLACE_GOODS_BONUS * LEVEL — прирост/убыль товаров в городе
PLACE_GOODS_TO_LEVEL: int = int(PLACE_GOODS_BONUS * (1 + 3.0 / 2) * 24)  # 1 город + 3 средних жителя за 24 часа
PLACE_GOODS_AFTER_LEVEL_UP: float = 0.25  # процент товаров, остающихся при увеличении размера города
PLACE_GOODS_AFTER_LEVEL_DOWN: float = 0.75  # процент товаров, возвращающихся при уменьшении размера города

PLACE_GOODS_FROM_BEST_PERSON: int = PLACE_GOODS_BONUS // 2

PLACE_GOODS_FOR_BUILDING_SUPPORT: int = PLACE_GOODS_FROM_BEST_PERSON * 3 // 5

# поскольку наибольшая статья расходов на стабилизацию ландшафта  — дороги, то расчёт делаем исходя из них
# здания и города будут вкладывать значительно меньше в эту статью трат (потому что меньше клеток занимают)
#
# во ремя введения стабилизации магии средний город имел дорог ~ 26 клеток, т.е. по 13, если делить поровну между двумя точками
# округлим до 15
PLACE_AVERAGE_TOTAL_ROADS_PRICE: int = int(1.5 * PLACE_GOODS_BONUS)  # средняя стоимость поддержки дорог для города
CELL_STABILIZATION_PRICE: int = PLACE_AVERAGE_TOTAL_ROADS_PRICE // 15

ROAD_LENGTH_PRICE_MULTIPLIER: List[Tuple[int, float]] = [(10, 1.0),
                                                         (20, 1.5),
                                                         (10**9, 2.0)]

# если размер города равен 1 (минимальный) и производство отрицательное
# то в городе вводят пошлину в размере "недостающее производство" * PLACE_TAX_PER_ONE_GOODS
PLACE_TAX_PER_ONE_GOODS: float = 0.1 / PLACE_GOODS_BONUS

# максимальное производство от пошлины фиксируется статически, а не динамически (например как 1/PLACE_TAX_PER_ONE_GOODS)
# поскольку последнее:
# - либо сделает пошлину крайне невыгодной в книге судеб
# - либо позволит поддерживать город максимального размера при, ожидаемом минимальном размере
MAX_PRODUCTION_FROM_TAX: int = int(PLACE_GOODS_BONUS * 2.5)

# исходим из того, что в первую очередь надо балансировать вероятность нападения монстров как самый важный параметр
PLACE_SAFETY_FROM_BEST_PERSON: float = 0.025
PLACE_TRANSPORT_FROM_BEST_PERSON: float = PLACE_SAFETY_FROM_BEST_PERSON * _SAFETY_TO_TRANSPORT

# хотя на опыт свобода и не влияет, но на город оказывает такое-же влияние как и транспорт
PLACE_FREEDOM_FROM_BEST_PERSON: float = PLACE_TRANSPORT_FROM_BEST_PERSON

PLACE_CULTURE_FROM_BEST_PERSON: float = 0.15

PLACE_RACE_CHANGE_DELTA_IN_DAY: float = 0.1
PLACE_RACE_CHANGE_DELTA: float = (PLACE_RACE_CHANGE_DELTA_IN_DAY * MAP_SYNC_TIME) / (24 * TURNS_IN_HOUR)

PLACE_STABILITY_UNIT: float = 0.1  # базовая единица изменения стабильности

PLACE_STABILITY_MAX_PRODUCTION_PENALTY: float = -PLACE_GOODS_BONUS * 2
PLACE_STABILITY_MAX_SAFETY_PENALTY: float = -0.15
PLACE_STABILITY_MAX_TRANSPORT_PENALTY: float = PLACE_STABILITY_MAX_SAFETY_PENALTY * _SAFETY_TO_TRANSPORT
PLACE_STABILITY_MAX_FREEDOM_PENALTY: float = -PLACE_STABILITY_MAX_TRANSPORT_PENALTY
PLACE_STABILITY_MAX_CULTURE_PENALTY: float = -1.0

PLACE_STABILITY_PENALTY_FOR_MASTER: float = -0.15
PLACE_STABILITY_PENALTY_FOR_RACES: float = -0.5  # штраф к стабильности за 100% разницы в давлении рас
PLACE_STABILITY_PENALTY_FOR_SPECIALIZATION: float = -0.5  # штраф за полное несоответствие специализации (когда 0 очков)


# считаем на сколько условных единиц бонусов от Мастеров влияет нулевая стабильность
_STABILITY_PERSONS_POINTS: float = (abs(PLACE_STABILITY_MAX_PRODUCTION_PENALTY) / PLACE_GOODS_FROM_BEST_PERSON +
                                    abs(PLACE_STABILITY_MAX_SAFETY_PENALTY) / PLACE_SAFETY_FROM_BEST_PERSON +
                                    abs(PLACE_STABILITY_MAX_TRANSPORT_PENALTY) / PLACE_TRANSPORT_FROM_BEST_PERSON +
                                    -abs(PLACE_STABILITY_MAX_FREEDOM_PENALTY) / PLACE_FREEDOM_FROM_BEST_PERSON +  # на свободу отсутствие стабильности влияет положительно
                                    abs(PLACE_STABILITY_MAX_CULTURE_PENALTY) / PLACE_CULTURE_FROM_BEST_PERSON)

# считаем максимальную стабильность от Мастера
PLACE_STABILITY_FROM_BEST_PERSON: float = 1.0 / _STABILITY_PERSONS_POINTS

WHILD_TRANSPORT_PENALTY: float = 0.1  # штраф к скорости в диких землях и на фронтире
TRANSPORT_FROM_PLACE_SIZE_PENALTY: float = 0.05  # штраф к скорости от размера города

PLACE_HABITS_CHANGE_SPEED_MAXIMUM: float = 10
PLACE_HABITS_CHANGE_SPEED_MAXIMUM_PENALTY: float = 10
PLACE_HABITS_EVENT_PROBABILITY: float = 0.025


RESOURCE_EXCHANGE_COST_PER_CELL: int = int(math.floor(PLACE_GOODS_BONUS / 40))

# время жизни взято «на глаз», чтобы:
# - с одной стороны, обеспечить значимость эффекта для города
# - с другой, предотвратить скопление одинаковых эффектов (от проектов Мастеров, например)
PLACE_STANDARD_EFFECT_LENGTH: int = 15  # в днях


###########################
# мастера
###########################

PERSON_MOVE_DELAY_IN_WEEKS: int = 2
PERSON_MOVE_DELAY: int = int(TURNS_IN_HOUR * 24 * 7 * PERSON_MOVE_DELAY_IN_WEEKS)  # минимальная задержка между переездами Мастера

PERSON_SOCIAL_CONNECTIONS_LIMIT: int = 3

PERSON_SOCIAL_CONNECTIONS_MIN_LIVE_TIME_IN_WEEKS: int = 2
PERSON_SOCIAL_CONNECTIONS_MIN_LIVE_TIME: int = int(TURNS_IN_HOUR * 24 * 7 * PERSON_SOCIAL_CONNECTIONS_MIN_LIVE_TIME_IN_WEEKS)

###########################
# здания
###########################

BUILDING_POSITION_RADIUS: int = 2

BUILDING_TERRAIN_POWER_MULTIPLIER: float = 0.5  # building terrain power is percent from city power

###########################
# Спутники
###########################

# под средним спутником понимается спутник со
# - средним здоровьем
# - средней самоотверженностью
# - средней слаженностью

# рост слаженности огранизуется так, чтобы она росла сначала быстро, потом ооооооочень долго
# в качестве опыта идёт 1 выполненного задания
# для получения слаженности N требуется N опыта

COMPANIONS_MIN_COHERENCE: int = 0   # минимальный уровень слаженности
COMPANIONS_MAX_COHERENCE: int = 100  # максимальный уровень слаженности

# опыта к слаженности за выполненный квест
# подбирается так, чтобы слаженность росла до максимума примерно за 9 месяцев
EXPECTED_FULL_COHERENCE_TIME = 9 * 30 * 24 * 60 * 60

COMPANIONS_MEDIUM_COHERENCE: float = (COMPANIONS_MIN_COHERENCE + COMPANIONS_MAX_COHERENCE) / 2

COMPANIONS_MIN_HEALTH: int = 300  # минимальное максимальное здоровье спутника
COMPANIONS_MAX_HEALTH: int = 700  # максимальное максимальное здоровье спутника

COMPANIONS_MEDIUM_HEALTH: float = (COMPANIONS_MIN_HEALTH + COMPANIONS_MAX_HEALTH) / 2

# TODO: при удалении кнопки помощи, этот параметр увеличили (прошлое значение было 9),
#       чтобы сгладить возможные проблемы с падежом спутников из-за изменений подхода к их лечению
#       в будущем надо надо сделать это значение более соответствующим балансу (скорее всего вернуть 9)
_COMPANIONS_MEDIUM_LIFETYME: int = 12  # ожидаемое время жизни среднего спутника со средним здоровьем без лечения в днях

# дельты мультипликатора вероятности блока для
COMPANIONS_BLOCK_MULTIPLIER_COHERENCE_DELTA: float = 0.2  # слаженность (от среднего)
COMPANIONS_BLOCK_MULTIPLIER_COMPANION_DEDICATION_DELTA: float = 0.2  # самоотверженности спутника
COMPANIONS_BLOCK_MULTIPLIER_HERO_DEDICATION_DELTA: float = 0.2  # самоотверженность героя

COMPANIONS_HABITS_DELTA: float = 0.5  # дельта изменения черт от среднего в зависимости от предпочтения

COMPANIONS_DEFEND_PROBABILITY: float = COMPANIONS_DEFENDS_IN_BATTLE / (BATTLE_LENGTH / 2)


COMPANIONS_HEALS_IN_HOUR: float = 1.0  # частота действия уход за спутником в час

COMPANIONS_HEALTH_PER_HEAL: int = 2  # лечение спутника за одно действие ухода за спутником
COMPANIONS_DAMAGE_PER_WOUND: int = 10  # урон спутнику за ранение

# частота ранений героя
COMPANIONS_WOUNDS_IN_HOUR_FROM_HEAL: float = COMPANIONS_HEALS_IN_HOUR * COMPANIONS_HEALTH_PER_HEAL / COMPANIONS_DAMAGE_PER_WOUND
COMPANIONS_WOUNDS_IN_HOUR_FROM_WOUNDS: float = COMPANIONS_MEDIUM_HEALTH / COMPANIONS_DAMAGE_PER_WOUND / (_COMPANIONS_MEDIUM_LIFETYME * 24)
COMPANIONS_WOUNDS_IN_HOUR: float = COMPANIONS_WOUNDS_IN_HOUR_FROM_WOUNDS + COMPANIONS_WOUNDS_IN_HOUR_FROM_HEAL

COMPANIONS_WOUND_ON_DEFEND_PROBABILITY_FROM_WOUNDS: float = COMPANIONS_WOUNDS_IN_HOUR_FROM_WOUNDS / (BATTLES_PER_HOUR * COMPANIONS_DEFENDS_IN_BATTLE)

COMPANIONS_HEAL_AMOUNT: int = 20

# вероятность того, что спутник использует способность во время боя
# на столько же должны увеличивать инициативу особенности спутника с боевыми способностями
COMPANIONS_BATTLE_STRIKE_PROBABILITY: float = 0.05


COMPANIONS_EXP_PER_MOVE_GET_EXP: int = 1  # получаемый героем опыт за одно «действие получения опыта во время движения героя»

# количество получений опыта от спутника в час
COMPANIONS_GET_EXP_MOVE_EVENTS_PER_HOUR: float = EXP_PER_HOUR * COMPANIONS_BONUS_EXP_FRACTION / COMPANIONS_EXP_PER_MOVE_GET_EXP
COMPANIONS_EXP_PER_MOVE_PROBABILITY = COMPANIONS_GET_EXP_MOVE_EVENTS_PER_HOUR / MOVE_TURNS_IN_HOUR

# количество опыта за каждое лечение спутника (при наличии нужной способности)
COMPANIONS_EXP_PER_HEAL: int = int(EXP_PER_HOUR * COMPANIONS_BONUS_EXP_FRACTION / COMPANIONS_HEALS_IN_HOUR)

COMPANIONS_HEAL_BONUS: float = 0.25  # доля отлечиваемого способностями спутников или героя

# количество вылеченного здоровья в час для спутников с лечебной способностью (рассчитывается исходя только из ранений, не компенсирующих лечение действием ухода)
COMPANIONS_REGEN_PER_HOUR: float = COMPANIONS_WOUNDS_IN_HOUR_FROM_WOUNDS * COMPANIONS_DAMAGE_PER_WOUND * COMPANIONS_HEAL_BONUS

COMPANIONS_EATEN_CORPSES_HEAL_AMOUNT: int = 1
COMPANIONS_REGEN_ON_HEAL_AMOUNT: int = 1
COMPANIONS_REGEN_BY_HERO: int = 1
COMPANIONS_REGEN_BY_MONEY_SPEND: int = 1

COMPANIONS_EATEN_CORPSES_PER_BATTLE: float = COMPANIONS_REGEN_PER_HOUR / BATTLES_PER_HOUR / COMPANIONS_EATEN_CORPSES_HEAL_AMOUNT
COMPANIONS_REGEN_ON_HEAL_PER_HEAL: float = COMPANIONS_REGEN_PER_HOUR / COMPANIONS_HEALS_IN_HOUR / COMPANIONS_REGEN_ON_HEAL_AMOUNT
COMPANIONS_HERO_REGEN_ON_HEAL_PER_HEAL: float = COMPANIONS_REGEN_PER_HOUR / COMPANIONS_HEALS_IN_HOUR / COMPANIONS_REGEN_BY_HERO

COMPANIONS_GIVE_COMPANION_AFTER: int = 24  # выдавать спутника герою без спутника примерно раз в N часов

COMPANIONS_LEAVE_IN_PLACE: float = 1.0 / 20  # вероятность того, что нелюдимый спутник покинет героя в городе

COMPANIONS_BONUS_DAMAGE_PROBABILITY: float = 0.25  # вероятность спутника получить дополнительный урон

COMPANIONS_FLY_DISTANCE: float = 1.0


##############################
# Bills
##############################

PLACE_MAX_BILLS_NUMBER: int = 3

ACCOUNT_MAX_ACTIVE_BILLS: int = 4


#################################
# Fame
#################################

HERO_FAME_PER_HELP: int = 1000  # стандартное количество известности, которое получает герой за помощь городу

PLACE_FAME_HISTORY_WEEKS: int = 6  # количество недель, которое хранится влияние города
PLACE_FAME_HISTORY_LENGTH: int = int(PLACE_FAME_HISTORY_WEEKS * 7 * 24 * TURNS_IN_HOUR)  # в ходах
PLACE_FAME_RECALCULATE_STEPS: float = PLACE_FAME_HISTORY_LENGTH / MAP_SYNC_TIME
PLACE_FAME_REDUCE_FRACTION: float = math.pow(0.01, 1.0 / PLACE_FAME_RECALCULATE_STEPS)

BILLS_FAME_BORDER: int = HERO_FAME_PER_HELP

##################
# проекты Мастеров
##################

JOB_MIN_LENGTH: int = 4  # минимальная длительность занятия мастера в днях

JOB_MIN_POWER: float = 0.5
JOB_MAX_POWER: float = 2.0

JOB_NEGATIVE_POWER_MULTIPLIER: float = 2.0  # множитель награды для противников: ломать — не строить

JOB_PRODUCTION_BONUS: int = PLACE_GOODS_BONUS
JOB_SAFETY_BONUS: float = PLACE_SAFETY_FROM_BEST_PERSON
JOB_TRANSPORT_BONUS: float = PLACE_TRANSPORT_FROM_BEST_PERSON
JOB_FREEDOM_BONUS: float = PLACE_FREEDOM_FROM_BEST_PERSON
JOB_STABILITY_BONUS: float = PLACE_STABILITY_UNIT
JOB_CULTURE_BONUS: float = PLACE_CULTURE_FROM_BEST_PERSON


##############################
# действие «религиозный обряд»
##############################

ACTION_RELIGION_EXPERIENCE: int = 1  # сколько опыта за раз даём
ACTION_RELIGION_PERIOD: int = int(0.5 * TURNS_IN_HOUR)  # раз в сколько ходов
ACTION_RELIGION_TIME: int = 3  # сколько ходов будет идти генерация единицы опыта
