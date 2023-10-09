def roll_call_dwarves(dwarves):
    _ = 1
    for dwarf in dwarves:
        print(f'{_}. {dwarf}')
        _ += 1


def summon_captain_planet(calls):
    return [call.title() + '!' for call in calls]


def long_planeteer_calls(calls):
    for call in calls:
        if (len(call) > 4):
            return True
    return False


def find_the_cheese(list_cheese):
    cheeses = ['cheddar', 'gouda', 'camembert']
    for cheese in list_cheese:
        if (cheese in cheeses):
            return cheese
    return None
