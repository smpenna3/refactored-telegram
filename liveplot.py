import numpy as np
import matplotlib.pyplot as plt
import time

class livePlot():
	def __init__(self, maxx, maxy):
		self.maxx = maxx
		self.maxy = maxy

		self.x = np.zeros(1)
		self.y = np.zeros(1)

		plt.ion()

		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)
		self.ax.set_xlim([0, maxx])
		self.ax.set_ylim([0, maxy])
		self.line1, = self.ax.plot(self.x, self.y, 'r-')

	def update(self, point):
		self.y = np.insert(self.y, len(self.y), point)
		if(len(self.x) < self.maxx):
			self.x = np.insert(self.x, len(self.x), self.x[-1]+1)
		if(len(self.y) > self.maxx):
			self.y = np.delete(self.y, 0)
		self.line1.set_xdata(self.x)
		self.line1.set_ydata(self.y)
		self.fig.canvas.draw()

lp = livePlot(100, 100)
for i in range(100):
	lp.update(i)

for i in range(100):
	lp.update(100-i)
