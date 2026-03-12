import mcp4725_driver as mcp
import signal_generator as sg
import time

amplitude = 2.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = mcp.MCP4725(5.0, 0x61 , False)
        start_time = time.time()

        while True:
            current_time = time.time() - start_time

            norm_amp = sg.get_sin_wave_amplitude(signal_frequency, current_time)

            voltage = amplitude * norm_amp

            dac.set_voltage(voltage)

            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()
