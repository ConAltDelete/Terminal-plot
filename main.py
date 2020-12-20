import math

# funksjoner

from sample_funk import *

def even(x):
	return x % 2 == 0


# konstanter og bestemt funksjon

def create_points(k,n : int):
	"""
	genererer en dict med entydige punkter fra en funksjon k med enkel parameter t som går fra 0 til 1 med n intervaller.
	"""
	y = {}
	# create points
	for t in range(0, n):
		f = [round(t) for t in k(t/n)]
		if f[1] not in y:
			y[f[1]] = set([f[0]])
		else:
			y[f[1]].add(f[0])
	#print(y)
	return y

def temp_create_grid(N : int, y : dict):
	# create grid
	y_defalt = "·"*N

	coor = []

	## plot in grid
	for y_coor in range(-N, N+1):
		y_temp = y_defalt
		if y_coor in y:
			for x_coor in y[y_coor]:
				x_coor += round(N/2)
				y_temp = y_temp[:x_coor] + "⁎" + y_temp[x_coor+1:]
			coor.insert(0, y_temp)
	return coor

def create_grid(len_x,len_y, add_axis = True):
	"""
	Denne funksjonen genererer en 2D liste med [len_y + 1 * len_x + 1] punkter.
	"""
	#len_x += 1 #! undersøk kutting av graf, disse er for å få det fram
	#len_y += 1

	grid = []
	for y in range(len_y+1):
		grid.append("·"*(len_x+1))
	
	grid = add_axis_zero(grid) if add_axis else grid

	return grid

def normalize(points: dict):
	"""
	Denne funksjonen finner senter til en gruppe punkter også justerer 
	absolutt koordiantene til relative koordinater basert på sentrum av gruppen.
	:param points: en ordbok som har y koordianter som nøkkel og x koordinater som verdi i en iterabel type (list, set, etc)
	:return: en ordbok med justerte verdier. dict[y] = set(x)
	"""
	x_min = min([min(l) for l in points.values()])
	x_max = max([max(l) for l in points.values()])
	y_min = min([k for k in points.keys()])
	y_max = max([k for k in points.keys()])

	x_len = (x_max + x_min)//2
	y_len = (y_max + y_min)//2

	new_points = {}

	for key in points:
		new_points[key - y_min] = set(map(lambda x: x - x_min , points[key]))
	
	return new_points

def plot_points(points, add_axis = True):
	"""
	plot points in terminal.
	"""
	points = normalize(points)

	x_min = min([min(l) for l in points.values()])
	x_max = max([max(l) for l in points.values()])
	y_min = min([k for k in points.keys()])
	y_max = max([k for k in points.keys()])

	x_avg = (x_max+x_min)//2
	y_avg = (y_max+y_min)//2

	grid: list = create_grid(x_max,y_max, add_axis)

	new_grid = []

	for y_coor in range(len(grid)):
		y_temp = grid[y_coor]
		if y_coor in points:
			for x_coor in points[y_coor]:
				y_temp = y_temp[:x_coor] + "⁎" + y_temp[x_coor+1:]
		new_grid.insert(0, y_temp)

	return new_grid

def add_axis_zero(grid: list):
	"""
	Denne funksjonen legger til akser som er sentrert til beste evne.
	:param grid: en liste med string.
	:return: en liste med string med karakterene '|' og '⎯'
	"""
	len_y = len(grid)
	len_x = len(grid[0])

	if not even(len_x): # en skjekk for x-akse istedet for å skjekke alle individuelt
		for y_level in range(len_y):
			y_now = grid[y_level]
			grid[y_level] = y_now[:math.floor(len_x/2)] + "|" + y_now[math.floor(len_x/2)+1:]
	else:
		for y_level in range(len_y):
			y_now = grid[y_level]
			grid[y_level] = y_now[:int(len_x/2-1)] + "||" + y_now[int(len_x/2+1):]
	
	if not even(len_y):
		grid[math.floor(len_y/2)] = "⎯"*len_x
	else:
		grid[int(len_y/2)] = "─"*len_x
		grid[int(len_y/2-1)] = "─"*len_x
	
	return grid

if __name__ == "__main__":
	k = spiral(N := 30)
	k2 = sirkel(N)
	k3 = grafh(lambda x: 10*math.sin(0.25*x),0,50)
	n = 1000

	P: dict = create_points(k,n) # k(t), t ∈ [0,1)
	P2 = create_points(k2,n)
	P3 = create_points(k3,n)

	grid: list = temp_create_grid(N,P)

	grid2 = plot_points(P)

	grid3 = plot_points(P3)
	
	# [print(l) for l in add_axis_zero(["·····","·····","·····","·····","·····","·····"])]

	#for l in grid:
	#	print(l)
	for l in grid2:
		print(l)
	for l in grid3:
		print(l)