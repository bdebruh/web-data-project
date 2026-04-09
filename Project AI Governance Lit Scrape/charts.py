import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv('/workspaces/web-data-project/cities_ai_governance_dataset.csv')

# Line Chart: Number of entries per year
year_counts = df['Year'].value_counts().sort_index()
plt.figure(figsize=(10, 6))
plt.plot(year_counts.index, year_counts.values, marker='o')
plt.title('Number of AI Governance Entries per Year')
plt.xlabel('Year')
plt.ylabel('Number of Entries')
plt.grid(True)
plt.savefig('line_chart.png')
plt.close()

# Category Dot Plot: Entries by Region over Years
plt.figure(figsize=(12, 8))
sns.stripplot(data=df, x='Year', y='Region', jitter=True, alpha=0.7)
plt.title('AI Governance Entries by Region and Year')
plt.xlabel('Year')
plt.ylabel('Region')
plt.savefig('category_dot_plot.png')
plt.close()