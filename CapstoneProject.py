import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Penguins Data.csv")
df.isnull().count()
df = df.dropna()
sns.pairplot(data=df, x="culmen_depth_mm", y="Body Mass (g)",
             hue="species")
plt.show()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.show()
sns.boxplot(data=df,x=np.array(df["species"]),
            y=np.array(df["Body Mass (g)"]))
plt.show()
sns.countplot(data=df,x="species", hue="sex")
plt.show()