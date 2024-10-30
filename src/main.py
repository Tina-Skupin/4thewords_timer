from timer import start_countdown
from time_utils import update_battle_time


#constants
attack = 0
mob_strength = 0
battle_time = 0

#takes mob wordcount and attack value, returns words you actually have to type to defeat monster
def calculate_actual_battle_count (attack, mob_strength):
    attack_bonus = attack/100
    attack_factor = 1+ attack_bonus
    battle_count = mob_strength//attack_factor
    print (f"Adjusted wordcount: {battle_count} words")
    return battle_count

#recalculates words you need to beat the mob to minutes
def words_to_minutes (battle_count):
    minutes = battle_count *(60/1000)
    print (f"battle time is {minutes} minutes")
    print ("Let the battle begin!")
    return minutes

def on_countdown_finish(minutes):
    global battle_time
    print ("Mob is down! Good job!")
    if battle_time is None:
        battle_time = 0
    increment = minutes
    print (f"battle_timecheck: {battle_time}")
    battle_time = update_battle_time(battle_time, increment)
    print (f"time spent in glorious battle today: {battle_time}")


def main():
    global battle_time
    # Constants or inputs for this example
    attack = 100
    mob_strength = 10

    # Function calls in sequence
    battle_count = calculate_actual_battle_count(attack, mob_strength)
    minutes = words_to_minutes(battle_count)
    seconds = minutes * 60  # Convert minutes to seconds for the timer

    countdown_callback = lambda: on_countdown_finish(minutes)

    # Start the countdown with the calculated seconds
    start_countdown(seconds, countdown_callback)

if __name__ == "__main__":
    main()