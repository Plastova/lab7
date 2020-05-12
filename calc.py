import matplotlib.pyplot as plt
import numpy as np

try:	

	plt.gcf().canvas.set_window_title("Priblizhennoe i tochnoe reshenie (calculator)")
	data=np.loadtxt ("result.txt")
	plt.plot(data[:,0], data[:,1],color='purple',linewidth=4,label='y (x) priblizh')
	plt.plot(data[:,0], data[:,2],color='red',linewidth=4,label="y' (x) priblizh")
	plt.plot(data[:,1], data[:,2],color='orange',linewidth=4,label="y' (y) priblizh")
	print("Tochnoe reshenie:")
	print("")
	print("y=0.5*exp(-x)*(2*x+exp(x/5)*sin(2*x/5)-2*exp(x/5)*cos(2*x/5)+4)")
	print("")
	print("y'=(0.5*exp(x/5)*sin(0.4*x)+1)*exp(-x)-(x+0.5*exp(x/5)*sin(0.4*x)-exp(x/5)*cos(0.4*x)+2)*exp(-x)")
	def tochn_resh(x):
		return 0.5*np.exp(-x)*(2*x+np.exp(x/5)*np.sin(2*x/5)-2*np.exp(x/5)*np.cos(2*x/5)+4)
	dx = 0.025
	xlist = np.arange (0, 2, dx)
	ylist = [tochn_resh(x) for x in xlist]
	plt.plot (xlist, ylist, color='yellow',linewidth=2, label='y (x) tochnoe')	
	def tochn_resh_proizv(x):
		return (0.5*np.exp(x/5)*np.sin(0.4*x)+1)*np.exp(-x)-(x+0.5*np.exp(x/5)*np.sin(0.4*x)-np.exp(x/5)*np.cos(0.4*x)+2)*np.exp(-x)

	
	dx = 0.025
	xlist2 = np.arange (0, 2, dx)
	ylist2 = [tochn_resh_proizv(x) for x in xlist]
	
	plt.plot (xlist2, ylist2, color='black',linewidth=2,label="y' (x) tochnoe")		
	plt.plot (ylist, ylist2, color='blue',linewidth=2,label="y' (y) tochnoe")	

	plt.legend()
	plt.title("Priblizhennoe i tochnoe reshenie (calculator)")
	plt.minorticks_on()
	plt.grid(color="blue", which="major", linewidth=1)
	plt.grid(color="blue", which="minor", linestyle=":", linewidth=0.5)
	plt.show()
	
	plt.gcf().canvas.set_window_title("Priblizhennoe i tochnoe reshenie (calculator)")
	plt.title("Raznostnye funktsii (calculator)")
	plt.plot(data[:,0], data[:,1]-tochn_resh(data[:,0]),color='blue',linewidth=2,label='y (x)')
	plt.plot(data[:,0], data[:,2]-tochn_resh_proizv(data[:,0]),color='green',linewidth=2,label="y' (x)")
	plt.plot(data[:,1], data[:,2]-tochn_resh_proizv(data[:,0]),color='orange',linewidth=2,label="y' (y)")
	plt.legend()
	plt.minorticks_on()
	plt.grid(color="blue", which="major", linewidth=1)
	plt.grid(color="blue", which="minor", linestyle=":", linewidth=0.5)
	plt.show()
except BaseException:
	print("fail ne naiden")


