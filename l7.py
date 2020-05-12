import numpy as np
import matplotlib.pyplot as plt
try:	
	data=np.loadtxt ("result.txt")
	plt.plot(data[:,0], data[:,1],color='green', label='y (x)')
	plt.gcf().canvas.set_window_title("Zadacha Koshi")
	plt.plot(data[:,0], data[:,2],color='red',label="y' (x)")
	plt.plot(data[:,1], data[:,2],color='orange',label="y' (y)")
	plt.legend()
	plt.title("Zadacha Koshi")
	plt.minorticks_on()
	plt.grid(color="blue", which="major", linewidth=1)
	plt.grid(color="blue", which="minor", linestyle=":", linewidth=0.5)
	plt.show()
except BaseException:
	print("fail ne naiden")
