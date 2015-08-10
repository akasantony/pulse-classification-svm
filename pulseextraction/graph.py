import matplotlib.pyplot as plt

__author__ = "Akas Antony"
__version__ = "1.0.0"
__maintainer__ = "Akas Antony"
__email__ = "antony.akas@gmail.com"

class PlotGraph:
	def plot(self,dataSet):
		lines = [line.strip() for line in open(dataSet)]
		plt.plot(lines)
		plt.ylabel('rate')
		plt.show()
		print lines
