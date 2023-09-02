import serial
import time

arduino_port = '/dev/ttyACM0'  # Substitua pelo nome da porta do seu Arduino (pode variar)
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

while True:
    print("Digite o número do LED (1, 2, 3) para acender ou 0 para desligar:")
    led_num = input()
    
    if led_num in ['0', '1', '2', '3']:
        ser.write(led_num.encode())  # Envia o comando para o Arduino
    else:
        print("Entrada inválida. Use 0, 1, 2 ou 3 para controlar os LEDs.")
    
    time.sleep(0.5)
