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
        plotnum = 231
        if mode == 'A':
            fig1 = plt.figure(figsize=(20, 10))
            outPdf = "Part A.pdf"
            pdf = matplotlib.backends.backend_pdf.PdfPages(outPdf)
            rng = np.arange(-5.0, 5.1, 0.05)

            plt.figure(1)
            y1 = A.uStep(rng)
            plt.subplot(plotnum)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Unit Step: U(t)")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y1)

            plotnum += 1
            plt.subplot(plotnum)
            y2 = A.triangle(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Triangle: (1 - |t|) in [-1,1]")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y2)

            plotnum += 1
            plt.subplot(plotnum)
            y3 = A.rect(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Rectangle: (1) in [-0.5,0.5]")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y3)

            plotnum += 1
            plt.subplot(plotnum)
            y4 = A.rTriangle(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Triangle: (2 - 2/3 * |t|) in [-3,3]")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y4)

            plotnum += 1
            plt.subplot(plotnum)
            rng = np.arange(-4., 3.1, 0.05)
            y5 = A.signal(rng)
            plt.ylabel('X(t)')
            plt.xlabel('t')
            plt.title("Signal: e^-3t * sin(8π*t/5) * U(t+2)")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y5)

            pdf.savefig(fig1)
            pdf.close()
            break

        elif mode == 'B':
            outPdf = "Part B.pdf"
            pdf = matplotlib.backends.backend_pdf.PdfPages(outPdf)
            rng = np.arange(-5., 5.1, 0.05)

            fig2 = plt.figure(1, figsize=(20, 10))
            fig2.suptitle("y(t) = e^(-|t|/5) * [U(t+1) - U(t-3)]", fontsize=16)
            y = B.y(rng)
            y1 = B.y1(rng)
            y2 = B.y2(rng)
            y3 = B.y3(rng)

            plotnum = 221
            plt.subplot(plotnum)
            plt.ylabel('y(t)')
            plt.xlabel('t')
            plt.title("y(t)")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y)

            plotnum += 1
            plt.subplot(plotnum)
            plt.ylabel('y1(t)')
            plt.xlabel('t')
            plt.title("y1(t) = y(3t)")
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y1)

            plotnum += 1
            plt.subplot(plotnum)
            plt.ylabel('y2(t)')
            plt.xlabel('t')
            plt.title('y2(t) = y(t + 2)')
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y2)

            plotnum += 1
            plt.subplot(plotnum)
            plt.ylabel('y3(t)')
            plt.xlabel('t')
            plt.title('y3(t) = y(4t - 2)')
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            plt.plot(rng, y3)

            pdf.savefig(fig2)
            pdf.close()
            break

        elif mode == 'C':
            outPdf = "Part C.pdf"
            pdf = matplotlib.backends.backend_pdf.PdfPages(outPdf)
            rng = np.arange(-15., 15.1, 0.05)
            fig3 = plt.figure(1, figsize=(10, 10))
            plt.title("Z(t) = e^(-|t|/3) * sin(4πt) * [U(t) - U(t-5)]  In Periodic time (T = 6)")
            plt.xlabel('t')
            plt.ylabel('Z(t)')
            plt.xticks(np.arange(min(rng), max(rng), 1.0))
            z = C.z(rng)
            plt.plot(rng, z)

            pdf.savefig(fig3)
            pdf.close()
            print("Energy of Z(t) = ", C.EnergyZ())
            print("Power of Z(t) = ", C.PowerZ())
            break

        elif mode == 'D':
            outPdf = "Part D.pdf"
            

        elif mode == 'E':
            outPdf = "Part E.pdf"


        elif mode == 'Q':
            break

        else:
            continue


if __name__ == "__main__":
    main()
