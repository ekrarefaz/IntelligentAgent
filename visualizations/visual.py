import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

"""Read CSV data"""
df = pd.read_csv('results.csv')

"""Create a figure for subplots"""
fig, axes = plt.subplots(2, 2, figsize=(15, 10))
fig.suptitle('Search Algorithm Performance')

"""Bar chart for execution time"""
sns.barplot(ax=axes[0, 0], x='algorithm', y='execution_time', data=df)
axes[0, 0].set_title('Execution Time by Algorithm')
axes[0, 0].set_ylabel('Execution Time (seconds)')

"""Line chart for peak memory usage"""
sns.lineplot(ax=axes[0, 1], x='algorithm', y='peak_memory_usage', data=df, marker='o')
axes[0, 1].set_title('Peak Memory Usage by Algorithm')
axes[0, 1].set_ylabel('Peak Memory Usage (bytes)')

"""Scatter plot for nodes explored"""
sns.scatterplot(ax=axes[1, 0], x='algorithm', y='nodes_explored', data=df)
axes[1, 0].set_title('Nodes Explored by Algorithm')
axes[1, 0].set_ylabel('Nodes Explored')

"""Box plot for path length"""
sns.stripplot(ax=axes[1, 1], x='algorithm', y='path_length', data=df)
axes[1, 1].set_title('Path Length by Algorithm')
axes[1, 1].set_ylabel('Path Length')

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
