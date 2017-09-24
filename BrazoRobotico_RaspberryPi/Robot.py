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

