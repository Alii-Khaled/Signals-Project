import PartA as A
import PartB as B
import PartC as C
import PartD as D
import PartE as E
import matplotlib.pyplot as plt
import math
import numpy as np


UI = " ---------------------------------\n" \
     "|Enter ' A ' to get Mode A.       |\n" \
     "|Enter ' B ' to get Mode B.       |\n" \
     "|Enter ' C ' to get Mode C.       |\n" \
     "|Enter ' D ' to get Mode D.       |\n" \
     "|Enter ' E ' to get Mode E.       |\n" \
     "|Enter ' Q ' to Quit Program.     |\n" \
     " ---------------------------------\n" \
     ">>> "
##################
# Main Function ##
##################


def main():
    # Mode A : Plotting the 3 Main Functions in Range [-5,5], Plotting r(t), Plotting the Signal X(t).
    # Mode B :
    # Mode C :
    # Mode D :
    # Mode E :
    while(1):
        mode = input(UI)
        if mode == 'A':
            rng = np.arange(-5, 5.1, 0.05)
            y1 = A.uStep(rng)
            plt.ylabel('Output Signal')
            plt.xlabel('Input Signal')
            plt.plot(rng, y1)
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.show()

            y2 = A.triangle(rng)
            plt.ylabel('Output Signal')
            plt.xlabel('Input Signal')
            plt.plot(rng, y2)
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.show()

            y3 = A.rect(rng)
            plt.ylabel('Output Signal')
            plt.xlabel('Input Signal')
            plt.plot(rng, y3)
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.show()

            y4 = A.rTriangle(rng)
            plt.ylabel('Output Signal')
            plt.xlabel('Input Signal')
            plt.plot(rng, y4)
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.show()

            rng = np.arange(-4., 3.1, 0.05)
            y5 = A.signal(rng)
            plt.ylabel('Output Signal')
            plt.xlabel('Input Signal')
            plt.plot(rng, y5)
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.show()

        elif mode == 'B':
            rng = np.arange(-5., 5.1, 0.05)

        elif mode == 'Q':
            break

        else:
            continue


if __name__ == "__main__":
    main()
