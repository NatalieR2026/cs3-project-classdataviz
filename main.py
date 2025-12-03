import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np

# Set style theme
plt.style.use('seaborn-v0_8-deep')


# Read CSV into DataFrame
df = pd.read_csv('class-data-v1.csv')
df = df.head(8) # Limit to first 8 rows for our class

# NOTE: some cols need type converted (object -> boolean, datetime)

# Flavor Pie Chart

flavor_counts = df['Flavor'].value_counts()
colors = ["#F0B08B", "#F2A2A2", "#E8D074"]
plt.pie(flavor_counts.values, labels=flavor_counts.index, colors=colors)
plt.title('Favorite Flavor Profile Breakdown')
plt.savefig('piechart_flavor.png')
plt.close()

# Temperature Preference to Hair Length Scatterplot

plt.scatter(df['Hair Length Inches'], df['Temperature Preference'])
plt.xlabel('Hair Length')
plt.ylabel('Temperature Preference')
plt.title('Hair Length vs. Temp Pref')
plt.savefig('scattterplot_hairtemp.png')
plt.close()

df_big5 = df[['BigFive Neuroticism', 'BigFive Extraversion', 'BigFive Openness', 'BigFive Conscientious', 'BigFive Agreeableness']]
print(df_big5)
corr_matrix = df_big5.corr()
sns.heatmap(corr_matrix, cmap='PuOr')
plt.savefig('BigFiveHeatMap.png')
plt.close()
# change to a half map
# fix labels