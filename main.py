from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import numpy as np
import icepool as ip
from icepool import Die, d


def dieGraph(fig, die: Die, x: int, y: int, i: int) -> None:
    """Graph the probablity of a dice roll"""
    ax = fig.add_subplot(x, y, i)
    # Plot some data on the Axes.
    ax.bar(die.keys(), [value / die.denominator() for value in die.values()])
    ax.set_ylim(0, 1)


def drawGraphs(graphs: list[list[Die | None]]) -> None:
    fig = plt.figure()  # Create a figure containing a single Axes.
    y: int = len(graphs)
    index: int = 0
    for i in range(y):
        x: int = len(graphs[i])
        for j in range(x):
            index += 1
            if graphs[i][j] is None:
                continue
            dieGraph(fig, graphs[i][j], x, y, index)
    plt.show()


def outcomes(
    count: int, play: int = 4, exhaustion: int = 0, *, winloss: bool = False
) -> Die:
    die = ip.d(12).map(lambda x: ip.vectorize(x == 1, x <= play - exhaustion))

    # Interpret the number of dice that rolled the above.
    def results(outcome):
        ones, successes = outcome

        if ones >= 1 and not winloss:
            return "3. Crit"
        elif successes >= 1:
            return "2. Success"
        else:
            return "1. Failure"

    # Roll and interpret the result.
    return (count @ die).map(results)


def main() -> None:
    drawGraphs(
        [
            [
                outcomes(2, 6, 0, winloss=True),
                outcomes(2, 6, 1, winloss=True),
            ],
            [
                outcomes(2, 6, 2, winloss=True),
                outcomes(2, 6, 3, winloss=True),
            ],
            [
                outcomes(2, 6, 4, winloss=True),
                outcomes(2, 6, 5, winloss=True),
            ],
        ]
    )

    # drawGraphs(
    #     [
    #         [outcomes(1, winloss=True), outcomes(2, winloss=True)],
    #         [outcomes(3, winloss=True), None],
    #     ]
    # )


if __name__ == "__main__":
    main()
