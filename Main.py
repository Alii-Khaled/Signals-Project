import PartA as A
import PartB as B
import PartC as C
import PartD as D
import PartE as E
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
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
    while 1:
        mode = input(UI)
        if mode == 'A':
            fig = plt.figure(figsize=(20, 10))
            outPdf = "Part A.pdf"
            pdf = matplotlib.backends.backend_pdf.PdfPages(outPdf)
            rng = np.arange(-5.0, 5.1, 0.05)

            plt.figure(1)
            y1 = A.uStep(rng)
            plt.subplot(231)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Unit Step: U(t)")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y1)

            plt.subplot(232)
            y2 = A.triangle(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Triangle: (1 - |t|) in [-1,1]")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y2)

            plt.subplot(233)
            y3 = A.rect(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Rectangle: (1) in [-0.5,0.5]")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y3)

            plt.subplot(234)
            y4 = A.rTriangle(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Triangle: (2 - 2/3 * |t|) in [-3,3]")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y4)

            plt.subplot(235)
            rng = np.arange(-4., 3.1, 0.05)
            y5 = A.signal(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Signal: e^-3t * sin(8π*t/5) * U(t+2)")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y5)

            pdf.savefig(fig)
            pdf.close()

        elif mode == 'B':
            outPdf = "Part B"
            rng = np.arange(-5., 5.1, 0.05)


        elif mode == 'C':
            outPdf = "Part C"


        elif mode == 'D':
            outPdf = "Part D"


        elif mode == 'E':
            outPdf = "Part E"


        elif mode == 'Q':
            break

        else:
            continue


if __name__ == "__main__":
    main()
