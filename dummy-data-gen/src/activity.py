from datetime import datetime, date, time, timedelta
from generator.data_generator import DataGenerator
import random

class ActivityDataGenerator(DataGenerator):

    def __init__(self, activities_from: date, activities_to: date, max_size: int):
        self.activities_from = activities_from
        self.activities_to = activities_to
        self.max_size = max_size


    def generate(self):
        day_iterator = DayIterator(self.activities_from, self.activities_to)   
    
        for day in day_iterator:
            # persons should be injected by constructur
            for person in persons():
                current_time = datetime.combine(day, time(8, 0)) # should depend on person
                minutes_left = 720 # should also depend on person
                sum_minutes = 0

                current_activity: Activity = None
                while (minutes_left > 0): # Overtime allowed :)
                    current_activity = rnd_activitiy(current_activity)
                    duration = simple_duration_dist(current_activity)
                    minutes_left -= duration
                    sum_minutes += duration
                    print(str(current_time) + ";" + person + ";" + current_activity.name + ";" + str(duration))
                    current_time += timedelta(minutes=duration)

class Activity:
    def __init__(self, name, minutes_min, minutes_max, has_focus):
        self.name = name
        self.minutes_min = minutes_min
        self.minutes_max = minutes_max
        self.has_focus = has_focus
    def __eq__(self, other):
        if not isinstance(other, Activity):
            return NotImplemented
        
        return self.name == other.name

class DayIterator:
    def __init__(self, start_date: date, end_date: date):
        self.current_date = start_date
        self.end_date = end_date
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.current_date > self.end_date):
            raise StopIteration
        else:
            next_date = self.current_date
            self.current_date += timedelta(days=1)
            return next_date
        



def activities():
    # i) recovery, focus attribute?
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