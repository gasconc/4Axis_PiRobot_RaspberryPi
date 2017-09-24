#!/usr/bin/python
#Configuracion general de registros 
import time
import RPi.GPIO as GPIO
from Robot import Robot
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Configuracion de puertos por servomotor
inputList = (14,15,18,23,24,25,8,7)
outputList = (16,20,21,12)

for i in inputList: 
	GPIO.setup(i,GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in outputList:
	GPIO.setup(i,GPIO.OUT)

Jarvis = Robot(8,8.5,10.75,5)

#Definiendo subprogramas.
#Configuracion de pines para la generacion de PWM
#GPIO.PWM(#pin,FrecuenciaPWM)
#GPIO.PWM.start() inicia la generacion del PWM 

#Servomotor 1
p1 = GPIO.PWM(12, 50)
p1.start(Jarvis.getBase())

#Servomotor 2
p2 = GPIO.PWM(16, 50)
p2.start(Jarvis.getCodo())

#Servomotor 3
p3 = GPIO.PWM(20, 50)
p3.start(Jarvis.getHombro())

#Servomotor 4
p4 = GPIO.PWM(21, 50)
p4.start(Jarvis.getGarra())


d = 0.125
#Constantes que representan los limites superiores e inferiores del DutyCylce
ls1 = 13
li1 = 3

ls2 = 11
li2 = 6

ls3 = 13
li3 = 8.5

ls4 = 8
li4 = 3

try:
	while 1:

		#Control de Servomotor1
		if (GPIO.input(14) == 0) and Jarvis.getBase() < ls1:
			Jarvis.setBase(Jarvis.getBase() + d)
		elif (GPIO.input(15) == 0) and Jarvis.getBase() > li1:
			Jarvis.setBase(Jarvis.getBase() - d)

		if Jarvis.getBase() < ls1 and Jarvis.getBase() > li1:
			p1.ChangeDutyCycle(Jarvis.getBase())

		#Control de Servomotor2
		if (GPIO.input(18) == 0) and Jarvis.getCodo() < ls2:
			Jarvis.setCodo(Jarvis.getCodo() + d)
		elif (GPIO.input(23) == 0) and Jarvis.getCodo() > li2:
			Jarvis.setCodo(Jarvis.getCodo() - d)

		if Jarvis.getCodo() < ls2 and Jarvis.getCodo() > li2:
			p2.ChangeDutyCycle(Jarvis.getCodo())


		#Control de Servomotor3
		if (GPIO.input(24) == 0) and Jarvis.getHombro() < ls3:
			Jarvis.setHombro(Jarvis.getHombro() + d)
		elif (GPIO.input(25) == 0) and Jarvis.getHombro() > li3:
			Jarvis.setHombro(Jarvis.getHombro() - d)

		if Jarvis.getHombro() < ls3 and Jarvis.getHombro() > li3:
			p3.ChangeDutyCycle(Jarvis.getHombro())



		#Control de Servomotor4
		if (GPIO.input(8) == 0) and Jarvis.getGarra() < ls4:
			Jarvis.setGarra(Jarvis.getGarra() + d)
		elif (GPIO.input(7) == 0) and Jarvis.getGarra() > li4:
			Jarvis.setGarra(Jarvis.getGarra() - d)

		if Jarvis.getGarra() < ls4 and Jarvis.getGarra() > li4:
			p4.ChangeDutyCycle(Jarvis.getGarra())

		time.sleep(0.03)



except KeyboardInterrupt:
	print("Interrupcion por teclado")
p1.stop()
p2.stop()
p3.stop()
p4.stop()
GPIO.cleanup()

