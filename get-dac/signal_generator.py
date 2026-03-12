import numpy as np
import time

def get_sin_wave_amplitude(freq, t):
    raw = (np.sin(2 * np.pi * freq * t) + 1)/2

    return raw

def wait_for_sampling_period(sampling_frequency):
    period = 1 / sampling_frequency
    time.sleep(period)
