import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd


# plt.plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Simple Plot')
#plt.show()

# plt.scatter
plt.scatter([1, 2, 3], [4, 5, 6])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Scatter Plot')
#plt.show()

# plt.bar
plt.bar([1, 2, 3], [4, 5, 6])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Bar Plot')
#plt.show()

# plt.hist
plt.hist([1, 2, 3, 4, 5, 6], bins=3)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Histogram')
#plt.show()


# sns.heatmap()
# Create a sample DataFrame
data = {
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
}
df = pd.DataFrame(data)
# Create a heatmap using seaborn
sns.heatmap(df, annot=True, cmap='coolwarm')
plt.title('Heatmap')
#plt.show()


# sns.pairplot()
sns.set(style="ticks")
# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)
sns.pairplot(df, diag_kind='kde')
plt.title('pairplot')
plt.show()