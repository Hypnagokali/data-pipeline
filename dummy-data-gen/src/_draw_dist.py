
# # #
# Just a test file to inspect the distributions
# # #
from activity import relaxing, concentrating
import distribution_rnd
import matplotlib.pyplot as plt
import numpy as np

def main():
    relaxing_fn = relaxing()
    concentrating_fn = concentrating()

    time_points = np.linspace(0, 24, 1000)

    pdf_rel = relaxing_fn(time_points)
    pdf_conc = concentrating_fn(time_points)

    plt.figure(figsize=(10, 6))

    plt.plot(time_points, pdf_rel, label="Relaxing Activity", color="blue")
    plt.plot(time_points, pdf_conc, label="Concentrated Activity", color="orange")

    plt.grid(alpha=0.3)
    plt.xlabel("Time", fontsize=14)
    plt.ylabel("Activity", fontsize=14)
    plt.legend(fontsize=12)
    plt.xticks(range(0, 24))

    plt.show()

if __name__ == "__main__":
    main()