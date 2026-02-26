import RPi.GPIO as GPIO

def dec2bin(value):
    return [int(bit) for bit in bin(value)[2:].zfill(8)]

class PWM_DAC:
    def __init__(self, gpio_bits, pwm_frequency, dynamic_range, verbose=False):
        self.gpio_bits = gpio_bits
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial=0)

        self.pwm = GPIO.PWM(gpio_bits, pwm_frequency)
        self.pwm.start(0)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            print(f"Напряжение {voltage:.3f} В выходит за диапазон 0.00 - {self.dynamic_range:.2f} В. Устанавливается 0 В.")
            duty_cycle = 0
            number = 0
         else:
             duty_cycle = (voltage / self.dynamic_range) * 100
             number = int(voltage / self.dynamic_range * 255)

        self.pmw.ChangeDutyCycle(duty_cycle)
        return number

        self.pmw.ChangeDutyCycle(duty_cycle)

        bits = dec2bin(number)
        for i, pin in enumerate(self.gpio_bits):
            GPIO.output(pin, bits[i])

        return number
        

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")
    finally:
        dac.deinit()
