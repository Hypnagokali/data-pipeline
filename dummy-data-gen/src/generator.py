from datetime import date
import distribution_rnd
from generator.data_generator import DataGenerator
import argparse
from activity import ActivityDataGenerator
import matplotlib.pyplot as plt
import numpy as np


def generate_data(generator: DataGenerator):
    generator.generate()
    


def main():
    x = np.linspace(0, 2 * np.pi, 200)
    y = np.sin(x)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()

    # parser = argparse.ArgumentParser(
    #     prog='Dummy data generator',
    #     description='Generates dummy data :)'
    # )
    # parser.add_argument('datatype', choices=['activities']) # currently only activities
    # parser.add_argument('-s', '--size', type=int, default=1000, help='Specify size of dataset')

    # args = parser.parse_args()

    # generator = ActivityDataGenerator(date(2024, 10, 1), date(2024, 10, 31), args.size)
    # generate_data(generator)

    # distribution_rnd.test()


if __name__ == "__main__":
    main()