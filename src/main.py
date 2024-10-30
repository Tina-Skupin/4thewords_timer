
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

from timer import start_countdown



def main():
    # Constants or inputs for this example
    attack = 100
    mob_strength = 1000

    # Function calls in sequence
    battle_count = calculate_actual_battle_count(attack, mob_strength)
    minutes = words_to_minutes(battle_count)
    seconds = minutes * 60  # Convert minutes to seconds for the timer

    # Start the countdown with the calculated seconds
    start_countdown(seconds)

if __name__ == "__main__":
    main()