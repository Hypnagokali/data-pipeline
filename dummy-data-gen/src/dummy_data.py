import random
from activity import Activity

def activities():
    # i) recovery, focus attribute?
    # ii) a distribution over the day (Day class): rnd_activity(prev, day)
    return [
        Activity("Project A", 30, 240, True),
        Activity("Learn Python", 30, 180, True),
        Activity("Watching series or movie", 30, 240, False), 
        Activity("Cleaning flat", 30, 120, False), 
        Activity("Learn about architecture", 60, 120, True) 
    ]

def simple_duration_dist(activity: Activity):
    return random.randint(activity.minutes_min, activity.minutes_max)

def rnd_activitiy(prev_activity):
    act = activities()

    while True: 
        i = random.randint(0, len(act) - 1)
        next = act[i]
        if (prev_activity is None or next != prev_activity):
            return next

def rnd_focus(activity: Activity):
    if not activity.has_focus:
        return 0
    return random.randint(1, 4)


def persons():
    return ["Alex", "Sandra", "Claire", "Hans"]