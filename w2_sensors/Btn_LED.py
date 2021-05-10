#-*-coding:utf-8-*-

# 필요한 라이브러리를 불러옵니다.
import RPi.GPIO as GPIO 
import time

# 사용할 GPIO핀의 번호를 선정합니다.
button_pin = 15
led_pin = 4

# 불필요한 warning 제거
GPIO.setwarnings(False) 
# GPIO핀의 번호 모드 설정
GPIO.setmode(GPIO.BCM) 
# 버튼 핀의 INPUT설정 , PULL DOWN 설정 
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# LED 핀의 OUT설정
GPIO.setup(led_pin, GPIO.OUT)

        
while 1:  #무한반복 
    # 만약 버튼핀에 High(1) 신호가 들어오면, "Button pushed!" 을 출력합니다.
    if GPIO.input(button_pin) == GPIO.HIGH:
        print("Button pushed!")    
        GPIO.output(led_pin,1)   # LED ON 
    else:
        GPIO.output(led_pin,0)   # LED OFF
        
    time.sleep(0.1)    # 0.1초 딜레이 
