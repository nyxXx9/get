import time

def get_sin_wave_amplitude(freq, time):
    from math import sin, pi
    raw = sin(2.0 * pi * freq * time)

    return raw

def wait_for_sampling_period(sampling_frequency):
    period = 1.0 / sampling_frequency
    time.sleep(period)
