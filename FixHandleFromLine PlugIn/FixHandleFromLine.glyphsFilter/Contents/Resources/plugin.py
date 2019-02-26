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
				if contour.nodes[n+1].type == "offcurve" and contour.nodes[n].type == "line" and contour.nodes[n].connection == 100 :
	
					#calcular hipotenusa e angulo da recta
					AR = (contour.nodes[n].y - contour.nodes[n-1].y)
					BR = (contour.nodes[n].x - contour.nodes[n-1].x)
					HypotRecta = math.hypot(AR, BR)
					AngleRecta = math.degrees(math.asin(AR / HypotRecta))               
					
					#calcular hipotenusa e angulo do Handle
					AH = (contour.nodes[n+1].y - contour.nodes[n].y)
					BH = (contour.nodes[n+1].x - contour.nodes[n].x)
					HypotHandle = math.hypot(AH, BH)
					AngleHandle = math.degrees(math.asin(AH / HypotHandle))  
					
					#calcular lados corrigidos do tiangulo do Handle
					AHnew = math.cos(math.radians(AngleRecta))*HypotHandle
					BHnew = math.sin(math.radians(AngleRecta))*HypotHandle
    				
					#CorrigirPonto
					if abs(HypotRecta) > abs(HypotHandle)*0.75 :
						if BR > 0:
							contour.nodes[n+1].x = contour.nodes[n].x + abs(AHnew)
						if AR > 0:	
							contour.nodes[n+1].y = contour.nodes[n].y + abs(BHnew)
						if BR < 0:
							contour.nodes[n+1].x = contour.nodes[n].x + abs(AHnew)*-1
						if AR < 0:	
							contour.nodes[n+1].y = contour.nodes[n].y + abs(BHnew)*-1
						
				#urve to line
				if contour.nodes[n-1].type == "offcurve" and contour.nodes[n].type == "curve" and contour.nodes[n+1].type == "line" and contour.nodes[n].connection == 100 :
	
					#calcular hipotenusa e angulo da recta
					AR = (contour.nodes[n+1].y - contour.nodes[n].y)
					BR = (contour.nodes[n+1].x - contour.nodes[n].x)
					HypotRecta = math.hypot(AR, BR)
					AngleRecta = math.degrees(math.asin(AR / HypotRecta))               
					
					#calcular hipotenusa e angulo do Handle
					AH = (contour.nodes[n].y - contour.nodes[n-1].y)
					BH = (contour.nodes[n].x - contour.nodes[n-1].x)
					HypotHandle = math.hypot(AH, BH)
					AngleHandle = math.degrees(math.asin(AH / HypotHandle))  
					
					#calcular lados corrigidos do tiangulo do Handle
					AHnew = math.cos(math.radians(AngleRecta))*HypotHandle
					BHnew = math.sin(math.radians(AngleRecta))*HypotHandle
    				
					#CorrigirPonto
					if abs(HypotRecta) > abs(HypotHandle)*0.75 :
						if BR > 0:
							contour.nodes[n-1].x = contour.nodes[n].x + abs(AHnew)*-1
						if AR > 0:	
							contour.nodes[n-1].y = contour.nodes[n].y + abs(BHnew)*-1
						if BR < 0:
							contour.nodes[n-1].x = contour.nodes[n].x + abs(AHnew)
						if AR < 0:	
							contour.nodes[n-1].y = contour.nodes[n].y + abs(BHnew)
		
		
		print layer, inEditView, customParameters
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
	