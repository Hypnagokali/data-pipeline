from datetime import date, timedelta

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
        
            