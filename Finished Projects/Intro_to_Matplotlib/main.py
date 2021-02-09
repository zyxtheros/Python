import matplotlib.pyplot as plt

# Full data set
years_full = [1, 1000, 1500, 1600, 1700, 1750, 1800, 1850, 1900, 1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
population_full = [200, 400, 458, 580, 682, 791, 1000, 1262, 1650, 2525, 2578, 3018, 3322, 3682, 4061, 4440, 4853, 5310, 5735, 6127, 6520, 6930, 7349]

# Appended data set
years = [1950, 1955, 1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015]
population = [2.5, 2.7, 3.0, 3.3, 3.6, 4.0, 4.4, 4.8, 5.3, 5.7, 6.1, 6.5, 6.9, 7.3]
deaths = [1.2, 1.7, 1.8, 2.2, 2.5, 2.7, 2.9, 3.0, 3.1, 3.3, 3.5, 3.8, 4.0, 4.3]


def example1():
	plt.plot(years, population, color=(255 / 255, 100 / 255, 100 / 255))# Give Matlpotlib the data to show on each axis, this makes the line
																		# The 'color' keyword targets the color of the line being drawn.
																		# It takes in 3 values, each of which must be between 0 and 1
	plt.plot(years, deaths, '--', color=(100 / 255, 255 / 255, 100 / 255))  # '--' makes it a dashed line, rather than a solid line

	plt.ylabel("Population (Billions)")  		# label for the Y-axis
	plt.xlabel("Years")  						# label for the X-axis
	plt.title("Population Growth Over Time")  	# label for the graph
	plt.grid(True)  							# Show the grid in the background
	plt.show()  								# send the plot created as output


# example1()	# Run example #1 by uncommenting


def example2():
	lines = plt.plot(years, population, years, deaths)
	plt.grid(True)  # Show the grid in the background

	plt.setp(lines, color=(1, .4, .4), marker='o')  # the 'marker' keyword sets the style for points/indicators

	plt.show()


# example2()	# Run example #2 by uncommenting


def example3():
	labels = 'Python', 'C++', 'Ruby', 'Java', 'PHP', 'Pearl'
	sizes = [33, 52, 12, 17, 62, 48]
	separated = (.11, 0, 0, 0, 0.15,
				 0)  # This variable will show how separated each slice of pie is from the center, with 0 meaning no separation

	plt.pie(sizes, labels=labels, autopct='%1.1f%%',
			explode=separated)  # 'autopct' makes text indicators to show the numerical data, the text formatted as the format from the input
	# 'explode'indicates how much each slice will be separated from the center
	plt.axis('equal')  # Makes sure the pies is always a circle

	plt.show()

# example3()	# Run example #3 by uncommenting

