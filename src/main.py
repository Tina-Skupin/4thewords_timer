
#constants
attack = 0
mob_strength = 0

#takes mob wordcount and attack value, returns words you actually have to type to defeat monster
def calculate_actual_battle_count (attack, mob_strength):
    attack_bonus = attack/100
    attack_factor = 1+ attack_bonus
    battle_count = mob_strength//attack_factor
    print (battle_count)
    return battle_count

#recalculates words you need to beat the mob to minutes
def words_to_minutes (battle_count):
    minutes = battle_count *(60/1000)
    print (minutes)
    return minutes

