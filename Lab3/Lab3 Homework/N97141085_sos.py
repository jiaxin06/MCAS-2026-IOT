import time
import RPi.GPIO as GPIO

LED_PIN = 37
BUZZER_PIN = 35

FREQ = 523
DUTY_CYCLE = 50
T = 0.2

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)

# 初始化 PWM 實例
buzzer_pwm = GPIO.PWM(BUZZER_PIN, FREQ)

def emit(duration: float):
    GPIO.output(LED_PIN, GPIO.HIGH)
    buzzer_pwm.start(DUTY_CYCLE)
    time.sleep(duration)

    
    GPIO.output(LED_PIN, GPIO.LOW)
    buzzer_pwm.stop()
    time.sleep(T)

def send_letter(pattern: str):
    for symbol in pattern:
        if symbol == '.':
            emit(T)
        elif symbol == '-':
            emit(T * 3)
            
    time.sleep(T * 2)

try:
    
    while True:
        send_letter("...")
        send_letter("---")
        send_letter("...")

        time.sleep(T * 4)

except KeyboardInterrupt:
    pass

finally:
    buzzer_pwm.stop()
    GPIO.cleanup()
