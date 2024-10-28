
#constants
attack = 0
mob_strength = 0

def calculate_actual_battle_count (attack, mob_strength):
    attack_bonus = attack/100
    attack_factor = 1+ attack_bonus
    battle_count = mob_strength//attack_factor
    print (battle_count)
    return battle_count



calculate_actual_battle_count (100, 1000)
calculate_actual_battle_count (10, 1000)