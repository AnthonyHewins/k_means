import pandas
import matplotlib.pyplot as plot
import random

r = lambda: random.uniform(0,100)
mu1 = [r(), r()]
mu2 = [r(), r()]
data_size = 100

def main():
	data = generate_data()
	converge(data)

def converge(data):
	mu1_points = []
	mu2_points = []
	for i in data:
		if distance(i,mu1) > distance(i,mu2):
			
	
def generate_data():
	data = []
	for i in range(data_size):
		data += [[r(), r()]]
	return pandas.DataFrame(data)

def distance(p0, p1):
	return math.sqrt((p0[0] - p1[0])**2 + (p0[1] - p1[1])**2)

main()
