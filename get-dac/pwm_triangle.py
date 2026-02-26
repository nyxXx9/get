import pwm_dac
import signal_generator as sg
import time

amplitude = 3.0
signal_frequency = 10
sampling_frequency = 500

if __name__ == "__main__":
    try:
        dac = pwm_dac.PWM_DAC(12, sampling_frequency, 3.290, False)
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
