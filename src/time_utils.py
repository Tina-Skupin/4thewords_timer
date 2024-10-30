#def update_battle_time(battle_time, increment):
#    new_battle_time = battle_time + increment
#    return new_battle_time

def update_battle_time(battle_time, increment):
    print(f"Current battle time: {battle_time}, Increment: {increment}")
    battle_time = battle_time + increment
    print(f"Updated battle time: {battle_time}")
    return battle_time