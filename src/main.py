from timer import start_countdown
from time_utils import update_battle_time
import os



#constants
attack = 0
mob_strength = 0
battle_time = 0

def load_battle_time():
    battle_time = 0.0  # default value
    if os.path.exists("battle_time.txt"):
        with open("battle_time.txt", "r") as f:
            try:
                battle_time = float(f.read().strip())
            except ValueError as e:
                print("Error reading battle time:", e)
    return battle_time

def save_battle_time(battle_time):
    with open("battle_time.txt", "w") as f:
        f.write(f"{battle_time}\n")


#takes mob wordcount and attack value, returns words you actually have to type to defeat monster
def calculate_actual_battle_count (attack, mob_strength):
    attack_bonus = attack/100
    attack_factor = 1+ attack_bonus
    battle_count = mob_strength//attack_factor
    print (f"Adjusted wordcount: {battle_count} words")
    return battle_count

#builds a text for pasting into 4tw
def create_lorem_ipsum(battle_count):
    lorem = ""
    words = battle_count
    while battle_count > 0:
        lorem = lorem + "ipsum "
        battle_count -=1
    #print (lorem)
    with open(r'lorem_ipsum.txt', 'w') as file_object:
        file_object.write(lorem)
    print("File written to:", os.path.abspath('lorem_ipsum.txt'))
    return lorem


#recalculates words you need to beat the mob to minutes
def words_to_minutes (battle_count):
    minutes = battle_count *(60/1000)
    print (f"battle time is {minutes} minutes")
    print ("Let the battle begin!")
    print (" -------")
    return minutes

def on_countdown_finish(minutes, battle_count):
    global battle_time
    print ("Mob is down! Good job!")
    if battle_time is None:
        battle_time = 0
    increment = minutes
    #print (f"battle_timecheck: {battle_time}")
    battle_time = update_battle_time(battle_time, increment)
    print (f"Today's time spent in glorious battle: {battle_time} minutes")

    #establish the lorem ipsum
    create_lorem_ipsum(battle_count)


def main():
    global battle_time

    #loads saved battle time
    battle_time = load_battle_time()


    # HERE GO THE VALUES FOR YOUR INDIVIDUAL FIGHT
    attack = 117
    mob_strength = 350

    # Function calls in sequence
    battle_count = calculate_actual_battle_count(attack, mob_strength)
    minutes = words_to_minutes(battle_count)
    seconds = minutes * 60  # Convert minutes to seconds for the timer

    countdown_callback = lambda: on_countdown_finish(minutes, battle_count)

    # Start the countdown with the calculated seconds
    start_countdown(seconds, countdown_callback)

    # Save the updated battle time just before exiting
    save_battle_time(battle_time)

if __name__ == "__main__":
    main()