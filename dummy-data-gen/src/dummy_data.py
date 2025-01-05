import random

def activities():
    # i) use a class
    # ii) recovery, focus attribute?
    # iii) a distribution over the day (Day class): rnd_activity(prev, day)
    return [
        ("Project A", 30, 240, True), 
        ("Learn Python", 30, 180, True),
        ("Watching series or movie", 30, 240, False), 
        ("Cleaning flat", 30, 120, False), 
        ("Learn about architecture", 60, 120, True) 
    ]

def rnd_activitiy(prev_activity):
    act = activities()

    while True: 
        i = random.randint(0, len(act) - 1)
        next = act[i]
        if (prev_activity is None or next != prev_activity):
            return next


def rnd_focus(activity):
    if not activity[2]:
        return 0
    return random.randint(1, 4)


def persons():
    return ["Alex", "Sandra", "Claire", "Hans"]