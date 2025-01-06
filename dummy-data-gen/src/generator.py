from activity import Activity, DayIterator
from datetime import date, datetime, time, timedelta
import argparse
import dummy_data

def main():
    parser = argparse.ArgumentParser(
        prog='Dummy data generator',
        description='Generates dummy data :)'
    )
    parser.add_argument('datatype', choices=['activities']) # currently only activities
    parser.add_argument('-s', '--size', type=int, default=1000, help='Specify size of dataset')

    args = parser.parse_args()

    day_iterator = DayIterator(date(2024, 10, 1), date(2024, 10, 31))   
    
    for day in day_iterator:
        for person in dummy_data.persons():
            current_time = datetime.combine(day, time(8, 0)) # should depend on person
            minutes_left = 720 # should also depend on person
            sum_minutes = 0

            current_activity: Activity = None
            while (minutes_left > 0): # Overtime allowed :)
                current_activity = dummy_data.rnd_activitiy(current_activity)
                duration = dummy_data.simple_duration_dist(current_activity)
                minutes_left -= duration
                sum_minutes += duration
                print(str(current_time) + ";" + person + ";" + current_activity.name + ";" + str(duration))
                current_time += timedelta(minutes=duration)

if __name__ == "__main__":
    main()