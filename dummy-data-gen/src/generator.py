from datetime import date
from generator.data_generator import DataGenerator
import argparse
from activity import ActivityDataGenerator

def generate_data(generator: DataGenerator):
    data = generator.generate()

def main():
    parser = argparse.ArgumentParser(
        prog='Dummy data generator',
        description='Generates dummy data :)'
    )
    parser.add_argument('datatype', choices=['activities']) # currently only activities
    parser.add_argument('-s', '--size', type=int, default=1000, help='Specify size of dataset')

    args = parser.parse_args()

    generator = ActivityDataGenerator(date(2024, 10, 1), date(2024, 10, 31), args.size)
    generate_data(generator)

if __name__ == '__main__':
    main()