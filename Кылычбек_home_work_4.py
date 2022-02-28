from random import randint

class Killtheboss:
    def __init__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value

    def hit(self, boss, heroes):
        pass

    def __str__(self):
        return f'{self.__name} health: {self.health} [{self.damage}]'


class Boss(Killtheboss):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def hit(self, boss, heroes):
        for hero in heroes:
            if boss.health > 0 and hero.health > 0:
                hero.health = hero.health - boss.damage


class Hero(Killtheboss):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        self.__super_ability = super_ability

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_ability(self, boss, heroes):
        pass

    def hit(self, boss):
        if boss.health > 0 and self.health > 0:
            boss.health = boss.health - self.damage


#-------------Персонажы-------------------------------------------------------------
class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "CRITICAL_DAMAGE")

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            coef =  randint(2, 4)
            boss.health = boss.health - self.damage * coef


class Medic(Hero):
    def __init__(self, name, health, damage, heal_points):
        super().__init__(name, health, damage, "HEAL")
        self.__heal_points = heal_points

    def apply_super_ability(self, boss, heroes):
        if boss.health > 0 and self.health > 0:
            for hero in heroes:
                if hero.health > 0 and self != hero:
                    hero.health = hero.health + self.__heal_points


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "BOOST")

    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                hero.damage = hero.damage + 5


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "REFUND")
# Berserk должен получать от босса урон, затем при ударе наносить ему свой урон,
#  плюс часть накопленного урона полученного от босса
    def apply_super_ability(self, boss, heroes):
        if self.health - boss.damage:
            self.damage = self.damage + (boss.damage / 10)
        else:
            boss.damage = boss.damage


class Thor(Hero):
    def __init__(self, name, health, damage, stan = 0):
        super().__init__(name, health, damage, "STAN")
        self.__stan = stan
# Thor, удар по боссу имеет шанс оглушить босса на 1 раунд,
#  вследствие чего босс пропускает 1 раунд и не наносит урон героям
    def apply_super_ability(self, boss, heroes):
        if self.health > 0:
            self.damage = self.__stan
        elif self.damage == self.__stan:
            boss.damage = 50
        else:
            boss.damage = 0


class Golem(Hero):
    def __init__(self, name, health, damage, protection = 0):
        super().__init__(name, health, damage, "SHIELD")
        self.__shield = protection
# Golem, который имеет увеличенную жизнь но слабый удар.
# Может принимать на себя 1/5 часть урона исходящего от босса по другим игрокам
    def apply_super_ability(self, boss, heroes):
        for hero in heroes:
            if hero.health > 0:
                self.__shield = boss.damage // 5
                if boss.damage >= 1:
                    hero.health = hero.health + self.__shield
                else:
                    hero.health = hero.health - boss.damage


class Witcher(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "SAVIOR")
# Witcher, не наносит урон боссу, но получает урон от босса.
# Имеет 1 шанс оживить первого погибшего героя, отдав ему свою жизнь, при этом погибает сам
    def apply_super_ability(self, boss, heroes):
        self.damage = 0
        for hero in heroes:
            if hero.health >= 0:
                self.health = hero.health
                self.health = 0
            else:
                self.health = 0

class Avrora(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "INVISIBLE")
# Avrora, которая может входить в режим невидимости на 2 раунда (т.е не получает урон от босса),
# в тоже время полученный урон в режиме невидимости возвращает боссу в последующих раундах. 
# Она может исчезать только один раз за игру
    def apply_super_ability(self, boss, heroes):
        pass


class Druid(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "HELLPER CALL")
# Druid, который имеет способность рандомно призывать помощника ангела героям или же
# ворона боссу на 1 раунд за всю игру. "Ангел" увеличивает способность медика лечить героев на  n кол-во.
#  А ворон прибавляет  агрессию (увеличивается урон на 50%), боссу если его жизнь менее 50%.
    def apply_super_ability(self, boss, heroes):
        pass


class Hacker(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, "HACKER")
# Hacker, который будет через раунд забирать у Босса N-ое количество здоровья и 
# переводить его одному из героев
    def apply_super_ability(self, boss, heroes):
        rnd = randint(10, 30)
        for hero in heroes:
            boss.health - rnd
            hero.health + rnd


class TrickyBastard(Hero):
    def __init__(self, name, health, damage):
        super(TrickyBastard, self).__init__(name, health, damage, "PLAY DEAD")
# TrickyBastard,  способность которого будет состоять в том, 
# чтобы притвориться мертвым в определенном раунде(из случайного выбора), 
# но в следующем раунде он снова вступает в бой. При этом он не получает урон и не бьет босса 
# когда притворился мертвым
    def apply_super_ability(self, boss, heroes):
        pass
    
class AntMan(Hero):
    def __init__(self, name, health, damage):
        super(AntMan, self).__init__(name, health, damage, "ANT MAN")
# AntMan, в каждом раунде он может увеличиться или же уменьшится на N-ный размер, 
# также увеличиваются/уменьшаются жигаются жизнь и урон, после раунда он возвращается в исходный размер
    def apply_super_ability(self, boss, heroes):
        pass


round_number = 0


def print_statistics(boss, heroes):
    print(" ")
    print(f'{round_number} ROUND -----------------')
    print(boss)
    print("---------VS--------")
    for hero in heroes:
        print(hero)


def is_game_finished(boss, heroes):
    if boss.health <= 0:
        print(">>>>>>>>><<<<<<<<<<")
        print("Heroes won!!!")
        print(">>>>>>>>><<<<<<<<<<")
        return True
    all_heroes_dead = True
    for hero in heroes:
        if hero.health > 0:
            all_heroes_dead = False
            break
    if all_heroes_dead:
        print(">>>>>>>>><<<<<<<<<<")
        print("Boss won!!!")
        print(">>>>>>>>><<<<<<<<<<<")
    return all_heroes_dead


def round(boss, heroes):
    global round_number
    round_number += 1
    boss.hit(boss, heroes)
    for hero in heroes:
        hero.hit(boss)
        hero.apply_super_ability(boss, heroes)
    print_statistics(boss, heroes)


def start():
    boss = Boss("OverLord", randint(3500, 4000), 50)
    warrior = Warrior("Dragon", randint(250, 300), 10)
    medic_1 = Medic("Dazzle", randint(220, 240), 5, 15)
    medic_2 = Medic("Paladin", randint(270, 300), 10, 5)
    magic = Magic("Rashta", randint(250, 300), 20)
    berserk = Berserk("Ursa", randint(250, 320), 30)
    thor = Thor("Raiden", randint(230, 340), 20)
    # golem = Golem("Rohan", randint(500, 800), 2)
    # witcher = Witcher("Lina", randint(400, 500), 0)
    # avrora =  Avrora("Bonik", randint(230, 300), 15)
    # hacker = Hacker("Tinker", randint(220, 300), 20)
    # tricky  = TrickyBastard("Opossum", randint(230, 3100), 15)
    # antMan = AntMan("Sullybear", randint(250, 350), 20)

    heroes = [warrior, medic_1, medic_2, magic, berserk,]

    print_statistics(boss, heroes)

    while not is_game_finished(boss, heroes):
        round(boss, heroes)


start()