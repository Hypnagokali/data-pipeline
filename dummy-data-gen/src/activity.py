from datetime import datetime, date, time, timedelta
from typing import List
from distribution_rnd import *
from generator.data_generator import DataGenerator
import random
import numpy as np

class ActivityDataGenerator(DataGenerator):

    def __init__(self, activities_from: date, activities_to: date, max_size: int):
        self.activities_from = activities_from
        self.activities_to = activities_to
        self.max_size = max_size


    def generate(self):
        f = open('test_data.csv', 'w')
        day_iterator = DayIterator(self.activities_from, self.activities_to)
        f.write('datetime;person;activity;duration_in_minutes\n')
        for day in day_iterator:
            # persons should be injected by constructur
            for person in persons():
                current_time = datetime.combine(day, time(8, 0)) # should depend on person
                minutes_left = 720 # should also depend on person
                sum_minutes = 0

                current_activity: Activity = None
                while (minutes_left > 0): # Overtime allowed :)
                    current_activity = rnd_activitiy(current_activity, current_time)
                    duration = simple_duration_dist(current_activity)
                    minutes_left -= duration
                    sum_minutes += duration
                    f.write(str(current_time) + ';' + person + ';' + current_activity.name + ';' + str(duration) + '\n')
                    current_time += timedelta(minutes=duration)

class Activity:
    def __init__(self, name, minutes_min, minutes_max, has_focus, distribution):
        self.name = name
        self.minutes_min = minutes_min
        self.minutes_max = minutes_max
        self.has_focus = has_focus
        self.distribution = distribution
        
    def __eq__(self, other):
        if not isinstance(other, Activity):
            return NotImplemented
        
        return self.name == other.name
    
    def __hash__(self):
        return hash(self.name)

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
        

def relaxing():
    return distribution(7.5, 1, 1, 20, 1, 1)

def concentrating():
    return distribution(10, 3, 1, 16, 3, 1)

def simple_duration_dist(activity: Activity):
    return random.randint(activity.minutes_min, activity.minutes_max)

def create_activities():
    return [
        Activity("Project A", 30, 240, True, concentrating()),
        Activity("Learn Python", 30, 180, True, concentrating()),
        Activity("Watching series or movie", 30, 240, False, relaxing()), 
        Activity("Cleaning flat", 30, 120, False, concentrating()), # might be another distribution  
        Activity("Learn about architecture", 60, 120, True, concentrating()) 
    ]

def rnd_activitiy(prev_activity: Activity, time: datetime):
    activities: List[Activity] = create_activities()

    if (prev_activity is not None):
        # never do the same activity twice
        activities = [a for a in activities if a.name != prev_activity.name]

    probs = []

    for i in range(0, len(activities)):
        probs.append(activities[i].distribution(time.hour))
    total = sum(probs)
    normalized = [p / total for p in probs]

    return np.random.choice(activities, p=normalized)


def rnd_focus(activity: Activity):
    if not activity.has_focus:
        return 0
    return random.randint(1, 4)


def persons():
    return ["Alex", "Sandra", "Claire", "Hans"]