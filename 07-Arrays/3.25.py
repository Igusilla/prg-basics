import matplotlib.pyplot as plt

x = []
y = []

# create x values
for n in range(-100, 101):  # Generate x values from -100 to 100
   x = x + [n]

# create y values based on f(x) = x^2 - 3
for n in x:
   y = y + [n**2 - 3]

# plot the chart
plt.plot(x, y)
plt.show()  # Show the plot