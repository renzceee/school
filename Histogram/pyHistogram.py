import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

df = pd.read_csv('Data.csv')

date_columns = ['date_announced', 'date_recovered', 'date_of_death', 
                'date_announced_as_removed', 'date_of_onset_of_symptoms']
                
for col in date_columns:
    df[col] = pd.to_datetime(df[col], errors='coerce')


plt.figure(figsize=(10, 6))
plt.hist(df['age'].dropna(), bins=20, edgecolor='black', alpha=0.7)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(alpha=0.3)
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='age', bins=20, kde=True)
plt.title('Distribution of Age with Density Curve')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(alpha=0.3)
plt.show()

plt.figure(figsize=(12, 6))
sns.histplot(data=df, x='age', hue='sex', multiple='stack', bins=20)
plt.title('Age Distribution by Sex')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(alpha=0.3)
plt.show()

plt.figure(figsize=(14, 6))
date_counts = df['date_announced'].dt.date.value_counts().sort_index()
plt.bar(date_counts.index, date_counts.values, alpha=0.7)
plt.title('Number of Cases by Announcement Date')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(alpha=0.3)
plt.show()

plt.figure(figsize=(10, 6))
status_counts = df['status'].value_counts()
plt.bar(status_counts.index, status_counts.values)
plt.title('Distribution of Case Status')
plt.xlabel('Status')
plt.ylabel('Count')
plt.grid(alpha=0.3)
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

sns.histplot(data=df, x='age', ax=axes[0, 0], bins=20)
axes[0, 0].set_title('Age Distribution')

sns.countplot(data=df, x='sex', ax=axes[0, 1])
axes[0, 1].set_title('Sex Distribution')

sns.countplot(data=df, y='age_group', ax=axes[1, 0])
axes[1, 0].set_title('Age Group Distribution')

sns.countplot(data=df, y='health_status', ax=axes[1, 1])
axes[1, 1].set_title('Health Status Distribution')

plt.tight_layout()
plt.show()

import plotly.express as px
import plotly.graph_objects as go

fig = px.histogram(df, x='age', color='sex', marginal='box', 
                   title='Interactive Age Distribution by Sex')
fig.show()

top_provinces = df['province'].value_counts().nlargest(5).index
province_df = df[df['province'].isin(top_provinces)]

plt.figure(figsize=(12, 8))
sns.histplot(data=province_df, x='age', hue='province', multiple='stack', bins=15)
plt.title('Age Distribution in Top 5 Provinces')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title='Province')
plt.grid(alpha=0.3)
plt.show()
