import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Penguins Data.csv")
plt.scatter(df["Culmen Length (mm)"], df["Body Mass (g)"])
plt.show()
plt.scatter(df["Culmen Depth (mm)"], df["Body Mass (g)"])
plt.show()
sns.pairplot(df, x="culmen_depth_mm", y="Body Mass (g)")
plt.show()
sns.pairplot(df, x="culmen_length_mm", y="Body Mass (g)",
             hue="species")
plt.show()