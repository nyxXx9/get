import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.3
signal_frequency = 1
sampling_frequency = 1000

if __name__ == "__main__":
    dac = r2r.R2R_DAC([22, 27, 17, 26, 25, 21, 20, 16], 3.3, False)
    try:
        start_time = time.time()
        
        while True:
            current_time = time.time() - start_time
            norm_amp = sg.get_sin_wave_amplitude(signal_frequency, current_time)

            voltage = amplitude * norm_amp

            dac.set_voltage(voltage)

            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()
