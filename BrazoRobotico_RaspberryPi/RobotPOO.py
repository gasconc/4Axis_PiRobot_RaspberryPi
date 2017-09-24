#!/usr/bin/python
class Robot:
#	Metodo Constructor
	def __init__(self,base,codo,hombro,garra):
		self.base = base
		self.codo = codo
		self.hombro = hombro
		self.garra = garra

	def setBase(self,base):
		self.base = base

	def getBase(self):
		return self.base


	def setCodo(self,codo):
		self.codo = codo

	def getCodo(self):
		return self.codo


	def setHombro(self,hombro):
		self.hombro = hombro

	def getHombro(self):
		return self.hombro


	def setGarra(self,garra):
		self.garra = garra

	def getGarra(self):
		return self.garra



	def mover(self,articulacion,d):
		self.setArticulacion(articulacion,self.getArticulacion(articulacion) + d)
		if self.getArticulacion(articulacion) < articulacion[2] and self.getArticulacion(articulacion) > articulacion[3]:
			articulacion[1].ChangeDutyCycle(self.getArticulacion(articulacion))
		else:
			self.setArticulacion(articulacion,self.getArticulacion(articulacion) - d)



	def getArticulacion(self,articulacion):

		if articulacion[0] == "base":
			return self.getBase()
		elif articulacion[0] == "codo":
			return self.getCodo()
		elif articulacion[0] == "hombro":
			return self.getHombro()
		elif articulacion[0] == "garra":
			return self.getGarra()

	def setArticulacion(self,articulacion,valor):

		if articulacion[0] == "base":
			self.setBase(valor)
		elif articulacion[0] == "codo":
			self.setCodo(valor)
		elif articulacion[0] == "hombro":
			self.setHombro(valor)
		elif articulacion[0] == "garra":
			self.setGarra(valor)
	