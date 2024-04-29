import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
data_file = np.genfromtxt("./rihanna_beyonce.txt", delimiter=",", dtype="float64", skip_header=True)

epochs=data_file[:,0]
accuracy=data_file[:,3]
conf=data_file[:,4]
plt.plot(epochs, accuracy, color="blue", marker="x")
plt.plot(epochs, conf, color="red", marker="x")
red_patch=mpatches.Patch(color='red', label="confidence")
blue_patch=mpatches.Patch(color='blue', label="accuracy")
plt.legend(handles=[blue_patch, red_patch])
plt.xlabel("Epochs of Training")
plt.ylabel("Test Accuracy, Avg. Pr(Favored Artist)")
plt.title("Rihanna vs. Beyonce (5 run averages)")
plt.gcf().savefig("rihanna_beyonce_pairwise.png", dpi=100)