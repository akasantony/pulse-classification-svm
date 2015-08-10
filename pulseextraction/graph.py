import matplotlib.pyplot as plt

class PlotGraph:
	def plot(self,dataSet):	
		lines = [line.strip() for line in open(dataSet)]
		plt.plot(lines)
		plt.ylabel('rate')
		plt.show()
		print lines
