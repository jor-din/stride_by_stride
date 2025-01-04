#!/usr/bin/env python
# coding: utf-8

# In[72]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[73]:


df = pd.read_csv('JordinHalfMarathonTr_DATA_LABELS_2024-12-30_0040.csv')
df.head()


# In[74]:


print(df.info())


# ###  Weekly Mileages

# In[75]:


# Convert the 'date' column to datetime for easier manipulation
df['Date'] = pd.to_datetime(df['Date'])

# Group data by week and calculate weekly mileage
df['week'] = df['Date'].dt.to_period('W')
weekly_mileage = df.groupby('week')['Distance'].sum()

# Prepare data for visualization
weeks = weekly_mileage.index.astype(str)
mileages = weekly_mileage.values

# Plot weekly mileage
plt.figure(figsize=(12, 6))
plt.plot(weeks, mileages, marker='o', linestyle='-', linewidth=2)
plt.title('Weekly Mileage Over Time', fontsize=16)
plt.xlabel('Week', fontsize=12)
plt.ylabel('Total Distance (miles)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()


# ### Weekly Average Pace Trends

# In[76]:


# Convert 'avg_pace' from string (e.g., '15:50') to total seconds for numerical analysis
def pace_to_seconds(pace):
    if isinstance(pace, str):
        minutes, seconds = map(int, pace.split(':'))
        return minutes * 60 + seconds
    return np.nan

df['avg_pace_seconds'] = df['Pace'].apply(pace_to_seconds)

# Calculate weekly average pace (in seconds)
weekly_avg_pace = df.groupby('week')['avg_pace_seconds'].mean()

# Prepare data for visualization
weeks = weekly_avg_pace.index.astype(str)
avg_paces = weekly_avg_pace.values

# Convert pace back to mm:ss format for labeling
def seconds_to_pace(seconds):
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    return f"{minutes}:{seconds:02d}"

# Plot weekly average pace
plt.figure(figsize=(12, 6))
plt.plot(weeks, avg_paces, marker='o', linestyle='-', linewidth=2, color='orange')
plt.title('Weekly Average Pace Trends', fontsize=16)
plt.xlabel('Week', fontsize=12)
plt.ylabel('Average Pace (mm:ss)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Annotate the pace values on the plot
for i, pace in enumerate(avg_paces):
    plt.text(i, pace, seconds_to_pace(pace), fontsize=9, ha='center', va='bottom')

plt.show()


# ### Average Cadence

# In[81]:


# Calculate weekly average cadence
weekly_avg_cadence = df.groupby('week')['Cadence'].mean()

# Prepare data for visualization
weeks = weekly_avg_cadence.index.astype(str)
avg_cadences = weekly_avg_cadence.values

# Plot weekly average cadence
plt.figure(figsize=(12, 6))
plt.plot(weeks, avg_cadences, marker='o', linestyle='-', linewidth=2, color='green')
plt.title('Weekly Average Cadence Trends', fontsize=16)
plt.xlabel('Week', fontsize=12)
plt.ylabel('Average Cadence (steps per minute)', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Annotate cadence values on the plot
for i, cadence in enumerate(avg_cadences):
    plt.text(i, cadence, f"{cadence:.1f}", fontsize=9, ha='center', va='bottom')

plt.show()


# In[ ]:






# In[ ]:





# In[ ]:





# In[ ]:




