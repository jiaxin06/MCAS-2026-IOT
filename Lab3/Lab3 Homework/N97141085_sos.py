import time
import RPi.GPIO as GPIO

# 硬體實體腳位定義 (Physical Board Pins)
LED_PIN = 37
BUZZER_PIN = 35

# 聲學與摩斯密碼時序常數
FREQ = 523          # 音調頻率 (C5, 523Hz)
DUTY_CYCLE = 50     # PWM 佔空比 50%
T = 0.2             # 基準時間單位 (Unit Time, 秒)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.LOW)

# 初始化 PWM 實例
buzzer_pwm = GPIO.PWM(BUZZER_PIN, FREQ)

def emit(duration: float):
    """
    同步觸發 LED 與蜂鳴器發聲，並維持單一符號間隔 (1T)
    """
    GPIO.output(LED_PIN, GPIO.HIGH)
    buzzer_pwm.start(DUTY_CYCLE)
    time.sleep(duration)
    
    # 關閉發信並保留符號內間隔
    GPIO.output(LED_PIN, GPIO.LOW)
    buzzer_pwm.stop()
    time.sleep(T)

def send_letter(pattern: str):
    """
    依字元陣列發送短音 (.) 或長音 (-)，並於字母結束時補足字母間隔 (3T)
    """
    for symbol in pattern:
        if symbol == '.':
            emit(T)
        elif symbol == '-':
            emit(T * 3)
            
    time.sleep(T * 2)

try:
    print("[INFO] SOS 訊號傳輸中，中斷請按 Ctrl+C...")
    while True:
        send_letter("...")
        send_letter("---")
        send_letter("...")

        time.sleep(T * 4)

except KeyboardInterrupt:
    pass

finally:
    # 釋放 PWM 與 GPIO 資源，防止腳位殘留 HIGH 電位
    buzzer_pwm.stop()
    GPIO.cleanup()