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

    # def set_number(self, number):
    #     bits = [int(element) for element in bin(number) [2:].zfill(8)]

    #     if number > 0:
    #         GPIO.output(self.gpio_bits, 1)
    #     else:
    #         GPIO.output(self.gpio_bits, 0)

    #     return bits

    def set_voltage(self, voltage):
        duty_cycle = (voltage / self.dynamic_range) * 100
        self.pwm.ChangeDutyCycle(duty_cycle)
        # if not (0.0 <= voltage <= self.dynamic_range):
        #     print(f"Напряжение {voltage:.3f} В выходит за диапазон 0.00 - {self.dynamic_range:.2f} В. Устанавливается 0 В.")
        #     print("Устанавливаем 0.0 В")
        #     number = 0
        # else:
        #     number = int(voltage / self.dynamic_range * 255)

        # self.set_number(number)
        # return number

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
