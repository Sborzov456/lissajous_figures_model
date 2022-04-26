from math import sin

ACCURACY = 0.01
TIME = 7


class Sin:

    def __init__(self, amplitude, frequency, phase_shift):
        self.amplitude = amplitude
        self.frequency = frequency
        self.phase_shift = phase_shift

    def calculate(self, t):
        return self.amplitude * sin(t * self.frequency + self.phase_shift)


def init_cord_list(f_t, f_t_list):
    t = 0
    while t < TIME:
        f_t_list.append(f_t.calculate(t))
        t += ACCURACY
