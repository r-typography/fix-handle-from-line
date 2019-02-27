# encoding: utf-8

###########################################################################################################
#
#
#	Filter without dialog Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Filter%20without%20Dialog
#
#
###########################################################################################################

import objc
from GlyphsApp import *
from GlyphsApp.plugins import *
import math

class FixHandleFromLine(FilterWithoutDialog):
	
	def settings(self):
		self.menuName = Glyphs.localize({'en': u'Fix Handle From Line', 'de': u'Fix Handle From Line'})
		self.keyboardShortcut = None # With Cmd+Shift

	def filter(self, layer, inEditView, customParameters):
		
		# Apply your filter code here
		for contour in layer.paths:
			numeroDePontos = len(contour.nodes)
			for n in range(-1,numeroDePontos-1):
								
				#line to Curve
				if contour.nodes[n+1].type == "offcurve" and contour.nodes[n].type == "line":			
				#calcular hipotenusa e angulo da recta
					AR = (contour.nodes[n].x - contour.nodes[n-1].x)
					BR = (contour.nodes[n].y - contour.nodes[n-1].y)				
					HypotRecta = math.hypot(BR, AR)
					AngleRecta = 0
					if AR >= 0 and BR > 0:
						AngleRecta = math.degrees(math.asin(BR / HypotRecta))
					if AR < 0 :
						AngleRecta = math.degrees(math.asin(BR / HypotRecta))*-1+180	
					if AR >= 0 and BR < 0:
						AngleRecta = math.degrees(math.asin(BR / HypotRecta))+360						
				#calcular hipotenusa e angulo do Handle
					AH = (contour.nodes[n+1].x - contour.nodes[n].x)
					BH = (contour.nodes[n+1].y - contour.nodes[n].y)
					HypotHandle = math.hypot(BH, AH)
					AngleHandle = 0
					if AH >= 0 and BH > 0:
						AngleHandle = math.degrees(math.asin(BH / HypotHandle))
					if AH < 0 :
						AngleHandle = math.degrees(math.asin(BH / HypotHandle))*-1+180	
					if AH >= 0 and BH < 0:
						AngleHandle = math.degrees(math.asin(BH / HypotHandle))+360
					
				#CorrigirPonto
					if abs(HypotRecta) > abs(HypotHandle)*0.75:
						if AngleRecta - AngleHandle > 355 and AngleRecta - AngleHandle < 360 or abs(AngleRecta - AngleHandle) < 5 or contour.nodes[n].connection == 100 :
							contour.nodes[n+1].x = contour.nodes[n].x + math.cos(math.radians(AngleRecta))*HypotHandle
							contour.nodes[n+1].y = contour.nodes[n].y + math.sin(math.radians(AngleRecta))*HypotHandle
				
				#Curve to Line
				if contour.nodes[n-1].type == "offcurve" and contour.nodes[n].type == "curve" and contour.nodes[n+1].type == "line":
				#calcular hipotenusa e angulo da recta
					AR = (contour.nodes[n].x - contour.nodes[n+1].x)
					BR = (contour.nodes[n].y - contour.nodes[n+1].y)				
					HypotRecta = math.hypot(BR, AR)
					AngleRecta = 0
					if AR >= 0 and BR > 0:
						AngleRecta = math.degrees(math.asin(BR / HypotRecta))
					if AR < 0 :
						AngleRecta = math.degrees(math.asin(BR / HypotRecta))*-1+180	
					if AR >= 0 and BR < 0:
						AngleRecta = math.degrees(math.asin(BR / HypotRecta))+360						
				#calcular hipotenusa e angulo do Handle
					AH = (contour.nodes[n-1].x - contour.nodes[n].x)
					BH = (contour.nodes[n-1].y - contour.nodes[n].y)
					HypotHandle = math.hypot(BH, AH)
					AngleHandle = 0
					if AH >= 0 and BH > 0:
						AngleHandle = math.degrees(math.asin(BH / HypotHandle))
					if AH < 0 :
						AngleHandle = math.degrees(math.asin(BH / HypotHandle))*-1+180	
					if AH >= 0 and BH < 0:
						AngleHandle = math.degrees(math.asin(BH / HypotHandle))+360
					
				#CorrigirPonto
					if abs(HypotRecta) > abs(HypotHandle)*0.75:
						if AngleRecta - AngleHandle > 355 and AngleRecta - AngleHandle < 360 or abs(AngleRecta - AngleHandle) < 5 or contour.nodes[n].connection == 100 :
							contour.nodes[n-1].x = contour.nodes[n].x + math.cos(math.radians(AngleRecta))*HypotHandle
							contour.nodes[n-1].y = contour.nodes[n].y + math.sin(math.radians(AngleRecta))*HypotHandle
						
		
		
		print layer, inEditView, customParameters
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	