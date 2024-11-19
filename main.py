import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')
print(df.info)
# - there are 70,000 patients in our data frame

# Add 'BMI' column & Caluclate BMI 
df['BMI'] = df['weight'] / (df['height'] / 100)**2  # kg / m^2

# Add 'overweight' column
# IF BMI > 25, overweight = 1
# IF BMI <= 25, overweight = 0 
# NOTE: np.where(condition, replacement value if TRUE, replacement value if FALSE)
# NOTE: "normalize" the data, taking something that has a lot of variation and making it into something that doesn't have a lot of variation
df['overweight'] = np.where(df['BMI'] > 25, 1, 0)

print(df.head())

# NOTE (to self): Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.

# Normalize cholestoral column  (1 -> 0) ( 2 or 3 -> 1)
df.loc[df['cholesterol']] = 0
df.loc[df['cholesterol']] = 1
# Normalize glucose column (1 -> 0) ( 2 or 3 -> 1)
df.loc[df['gluc']] = 0
df.loc[df['gluc']] = 1

# Function to draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  df_cat = None
  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat = None

  # Draw the catplot with 'sns.catplot()'

  # Get the figure for the output
  fig = None

  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig

# Function to draw Heat Map
def draw_heat_map():
  # Clean the data
  df_heat = None

  # Calculate the correlation matrix
  corr = None

  # Generate a mask for the upper triangle
  mask = None

  # Set up the matplotlib figure
  fig, ax = None

  # Draw the heatmap with 'sns.heatmap()'

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig


# RUN FUNCTIONS
draw_cat_plot()
draw_heat_map()

