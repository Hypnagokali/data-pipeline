import dummy_data
import argparse

def main():
    parser = argparse.ArgumentParser(
        prog='Dummy data generator',
        description='Generates dummy data :)'
    )
    parser.add_argument('datatype', choices=['activities']) # currently only activities
    parser.add_argument('-s', '--size', type=int, default=1000, help='Specify size of dataset')

    args = parser.parse_args()
        
    current_activity = None
    for el in range(args.size):
        current_activity = dummy_data.rnd_activitiy(current_activity)
        print(str(el + 1) + ". activity: " + current_activity[0])

if __name__ == "__main__":
    main()