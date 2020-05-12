import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

try:	

	plt.gcf().canvas.set_window_title("Priblizhennoe i tochnoe reshenie (scipy)")
	data=np.loadtxt ("result.txt")
	plt.plot(data[:,0], data[:,1],color='purple',linewidth=4,label='y (x) priblizh')
	plt.plot(data[:,0], data[:,2],color='red',linewidth=4,label="y' (x) priblizh")
	plt.plot(data[:,1], data[:,2],color='blue',linewidth=4,label="y' (y) priblizh")
	
	def dU_dx(U, x):
		return [U[1], -1.6*U[1] - 0.8*U[0] + 0.2*x*np.exp(-x)]
	
	U0 = [1, 0]
	xs = np.linspace(0, 2, 200)
	Us = odeint(dU_dx, U0, xs)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.plot(xs,Us[:,0],color='yellow',label="y(x), y'(x), y'(y) tochnye" )
	plt.plot(xs,Us[:,1],color='yellow')
	plt.plot(Us[:,0],Us[:,1],color='yellow')
	
	plt.legend()
	plt.title("Priblizhennoe i tochnoe reshenie (scipy)")
	plt.minorticks_on()
	plt.grid(color="blue", which="major", linewidth=1)
	plt.grid(color="blue", which="minor", linestyle=":", linewidth=0.5)
	plt.show()
	
	plt.gcf().canvas.set_window_title("Priblizhennoe i tochnoe reshenie (scipy)")
	plt.title("Raznostnye funktsii (scipy)")
	
	Us2 = odeint(dU_dx, U0, data[:,0])
	plt.plot(data[:,0], data[:,1]-Us2[:,0],color='blue',linewidth=2,label='y (x)')
	plt.plot(data[:,0], data[:,2]-Us2[:,1],color='green',linewidth=2,label="y' (x)")
	plt.plot(data[:,1], data[:,2]-Us2[:,1],color='orange',linewidth=2,label="y' (y)")
	plt.legend()
	plt.minorticks_on()
	plt.grid(color="blue", which="major", linewidth=1)
	plt.grid(color="blue", which="minor", linestyle=":", linewidth=0.5)
	plt.show()
except BaseException:
	print("fail ne naiden")
