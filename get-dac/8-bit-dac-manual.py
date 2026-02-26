import RPi. GPIO as G

leds = [16, 20, 21, 25, 26, 17, 27, 22]
leds = [22, 27, 17, 26, 25, 21, 20, 16]

G.setmode(G.BCM)
G.setup(leds, G. OUT)
G.output(leds, 0)
dynamic_range = 3.2

def voltage_to_number (voltage):
    if not (0.0<=voltage<=dynamic_range):
        print (f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
        print ("Устанавливаем 0.0 В")
        return 0
    return int(voltage/ dynamic_range *255)

def numder_to_dac (number):
    bits =  [int(element) for element in bin(number) [2:].zfill(8)]
    for i in range(8):
        G.output(leds[i], bits[7-i])
    return bits
try:
    while True:
        try:
            voltage = float(input("Введите напряжение в вольтах: "))
            number = voltage_to_number(voltage)
            numder_to_dac(number)

        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")
finally:
    G.output (leds, 0)
    G.cleanup()
