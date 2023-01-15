import matplotlib.pyplot as plt # import matplotlib library 
import numpy as np # import numpy library

U = np.random.uniform(0,1,1000) # generates a list of 1000 samples

E = list()

for x in U:

    # substitutes each sample, x, into the inverse function -(1/lambda)*(ln(1-x)), where lamdbda = 1/4, 
    # and adds the result into the list E
    E.append(-4*np.log(1-x))

x_values = np.linspace(0,30,2000) # obtains x value plots for pdf of exp distribution

def exp_pdf(lam,x):

    return lam * np.exp(-lam*x)

# iterates through values in x_values through the function exp_pdf for lam = 1/4, when t = 4, to obtain the corresponding y values
# and stores them in the variable y_values as a list
y_values = np.array([exp_pdf(1/4,x) for x in x_values])

figure, axis = plt.subplots(figsize=(10,6))
axis.plot(x_values, y_values, label='Actual') # plots values of y_values against x_values for lambda = 1/4
axis.set_title("Probability Density Function") # labels title of plot
axis.set_xlabel('x') # labels X-axis of plot 
axis.set_ylabel('Probability Density') # labels Y-axis of plot

plt.hist(E, bins=50, density=True, label='Samples') # plots generated sample histogram with the PDF when lambda = 1/4
plt.legend () # adds respective legends for different plots 
plt.show() # displays our PDF plots in popup window
