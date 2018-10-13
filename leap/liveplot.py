import numpy as np
import matplotlib.pyplot as plt
import time

class livePlot():
	# Initialize with the maximum values for the x and y axes
	def __init__(self, maxx, maxy):
		self.maxx = maxx
		self.maxy = maxy

		# Start with both arrays with one element (0)
		self.x = np.zeros(1)
		self.y = np.zeros(1)

		# Start plt in interactive mode for live updates
		plt.ion()

		# Setup a new figure with a subplot
		self.fig = plt.figure()
		self.ax = self.fig.add_subplot(111)
		
		# Set the maximum values for the axes
		self.ax.set_xlim([0, maxx])
		self.ax.set_ylim([0, maxy])
		
		# Create the line item (will be modified later for updated data)
		self.line1, = self.ax.plot(self.x, self.y, 'r-')

	# Call this function to update the data in the chart with a given y point
	# the x points are updated automatically
	def update(self, point):
		# Add the y point to the list
		self.y = np.insert(self.y, len(self.y), point)
		
		# If it's under the maximum number, add a new point to the x lists
		if(len(self.x) < self.maxx):
			self.x = np.insert(self.x, len(self.x), self.x[-1]+1)
		
		# If the length exceeded the max length, cut the first element to keep on screen (Scroll)
		if(len(self.y) > self.maxx):
			self.y = np.delete(self.y, 0)
			
		# Update the chart with the new data
		self.line1.set_xdata(self.x)
		self.line1.set_ydata(self.y)
		self.fig.canvas.draw()




