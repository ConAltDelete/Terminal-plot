import math
def grafh(funk, a, b):
	def ret_funk(t):
		return [a+(b-a)*t,funk(a+(b-a)*t)]
	return ret_funk

def sirkel(d=1):
	def r_sirkel(t):
		return [d*0.5*math.cos(2*math.pi * t), d*0.5*math.sin(2*math.pi * t)]
	return r_sirkel


def spiral(d=1, dekrement=2):
	def r_sirkel(t):
		return [t*d*0.5*math.cos(2*math.pi * dekrement * t), t*d*0.5*math.sin(2*math.pi * dekrement * t)]
	return r_sirkel