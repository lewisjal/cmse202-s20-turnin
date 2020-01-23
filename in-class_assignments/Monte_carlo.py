#Monte Carlo.py
import random
import math
import matplotlib.pyplot as plt
N = 16
inside = 0
total_area = 4
actual_area = .75*math.pi


x = []
y = []
for i in range(0,N):
	x_pos = random.random()*2
	y_pos = random.random()*2
	point_inside = math.sqrt(x_pos+y_pos)
	if point_inside > 0.5 and point_inside < 1.0:
		inside += 1
	x.append(x_pos)
	y.append(y_pos)
area =total_area *(N/inside)
error = (abs(area - actual_area)/actual_area)
print(error)


plt.plot(x,y)
plt.title("MonteCarlo")
