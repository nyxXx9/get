import pwm_dac as pwm
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        dac = pwm.PWM_DAC(12, 500, 3.290, False)
        start_time = time.time()

        while True:
            current_time = time.time() - start_time

            norm_amp = sg.get_sin_wave_amplitude(signal_frequency, current_time)

            voltage = amplitude * norm_amp

            dac.set_voltage(voltage)

            sg.wait_for_sampling_period(sampling_frequency)

    finally:
        dac.deinit()
