from harmonic_function import *
from drawing import *

X_LIST = []
Y_LIST = []


def main():
    print("X = X(t): ")
    x_t = Sin(0, 0, 0)
    x_t.amplitude = float(input("Input Amplitude --> "))
    x_t.frequency = float(input("Input Frequency --> "))
    x_t.phase_shift = float(input("Input Phase Shift --> "))
    print("\nY = Y(t): ")
    y_t = Sin(0, 0, 0)
    y_t.amplitude = float(input("Input Amplitude --> "))
    y_t.frequency = float(input("Input Frequency --> "))
    y_t.phase_shift = float(input("Input Phase Shift --> "))

    init_cord_list(x_t, X_LIST)
    init_cord_list(y_t, Y_LIST)

    draw(X_LIST, Y_LIST, x_t, y_t)


if __name__ == '__main__':
    main()
