#!/usr/bin/python
#Configuracion general de registros 
import time
import RPi.GPIO as GPIO
from RobotPOO import Robot
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#Configuracion de puertos por servomotor
inputList = (14,15,18,23,24,25,8,7)
outputList = (16,20,21,12)

for i in inputList: 
	GPIO.setup(i,GPIO.IN, pull_up_down=GPIO.PUD_UP)

for i in outputList:
	GPIO.setup(i,GPIO.OUT)

#Objeto de la clase Robot
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


#Tuplas que describen las articulaciones
#articulacion = ("nombre",PWM,limite superior PWM, limite inferior PWM)
base = ("base",p1,13,3)
codo = ("codo",p2,11,6)
hombro = ("hombro",p3,13,8.5)
garra = ("garra",p4,8,3)

d = 0.125
#Constantes que representan los limites superiores e inferiores del DutyCylce

try:
	while 1:

		#Control de Servomotor1
		if (GPIO.input(14) == 0):
			Jarvis.mover(base,d)
		elif (GPIO.input(15) == 0):
			Jarvis.mover(base,-d)

		#Control de Servomotor2
		if (GPIO.input(18) == 0):
			Jarvis.mover(codo,d)
		elif (GPIO.input(23) == 0):
			Jarvis.mover(codo,-d)

		#Control de Servomotor3
		if (GPIO.input(24) == 0):
			Jarvis.mover(hombro,d)
		elif (GPIO.input(25) == 0):
			Jarvis.mover(hombro,-d)

		#Control de Servomotor4
		if (GPIO.input(8) == 0):
			Jarvis.mover(garra,d)
		elif (GPIO.input(7) == 0):
			Jarvis.mover(garra,-d)

		time.sleep(0.03)

except KeyboardInterrupt:
	print("Interrupcion por teclado")
p1.stop()
p2.stop()
p3.stop()
p4.stop()
GPIO.cleanup()

