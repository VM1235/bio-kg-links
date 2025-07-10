import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV
df = pd.read_csv('baseline/transE_hits_summary.csv')

# Melt the dataframe to long-form
df_long = df.melt(id_vars=['Split', 'View'], 
                  value_vars=['Hits@1', 'Hits@3', 'Hits@5', 'Hits@10'],
                  var_name='Metric', value_name='Score')

# Ensure Score is float
df_long['Score'] = df_long['Score'].astype(float)

# Plot
sns.set(style="whitegrid")
plt.figure(figsize=(12, 6))
sns.barplot(data=df_long, x='Split', y='Score', hue='View', ci=None, palette="muted", dodge=True)

# Add separate bars for each metric
g = sns.catplot(data=df_long, x='Split', y='Score', hue='View',
                col='Metric', kind='bar', height=5, aspect=0.9, palette="Set2")

g.set_titles("{col_name}")
g.set_axis_labels("Split", "Hits@k Score")
g._legend.set_title("View")
plt.tight_layout()
plt.savefig("baseline/transE_hits_plot.png")
plt.show()
