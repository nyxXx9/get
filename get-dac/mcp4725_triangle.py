import mcp4725_driver as mcp4725
import signal_generator as sg

import time

amplitude = 1.5
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = mcp4725.MCP4725(2.6, 0x61 , False)

        t = 0.0
        dt = 1 / sampling_frequency
        while True:
            t += dt

            norm_amp = sg.get_triangle_wave_amplitude(signal_frequency, t)

            voltage = amplitude * norm_amp

            dac.set_voltage(voltage)

            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()
