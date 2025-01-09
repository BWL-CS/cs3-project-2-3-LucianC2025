import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#sns.color_palette("mako")

# Import data
df = pd.read_csv('medical_examination.csv')
print(df.info())
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
# In the data 1=normal, 2=above normal, 3=very above normal
# We are reassining everything with a 1 to 0 (good) and everything with a 2 or 3 to 1 (bad)
# **** HOW TO REPLACE VALUES CONIDTIONALLY ****
df.loc[df['cholesterol'] == 1,'cholesterol'] = 0  # select all the rows in the cholestoral column that have a value of 1 and set that equal to 0
df.loc[df['cholesterol'] > 1, 'cholesterol'] = 1
# Normalize glucose column (1 -> 0) ( 2 or 3 -> 1)
df.loc[df['gluc'] == 1, 'gluc'] = 0
df.loc[df['gluc'] > 1, 'gluc'] = 1

print(df['cholesterol'])
print(df['gluc'])

# Function to draw Categorical Plot
def draw_cat_plot():
  # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
  # NOTE: pd.melt(df) gathers columns into rows
  # NOTE: id_vars='' the column we want to use as the identifier labels 
  # NOTE: value_vars=[''] is a list of the values we want in the columns
  df_cat = pd.melt(df, id_vars='cardio', value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight']) # taking the columns and making them rows

  # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
  df_cat['total'] = 0
  # variable is 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'
  # value is the value of the variables
  df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()
  print(df_cat)

  # Draw the catplot with 'sns.catplot()'
  plot = sns.catplot(x='variable', y='total', data=df_cat, hue='value', kind='bar', col='cardio')
  # Get the figure for the output
  fig = plot.figure
  # Do not modify the next two lines
  fig.savefig('catplot.png')
  return fig


# Function to draw Heat Map
def draw_heat_map():
  # Clean the data
  # Leave out patients where their diastolic (resting) pressure is higher than their systolic pressure --> this is medically incorrect 
  df_heat = df[df['ap_lo'] <= df['ap_hi']] # pulling rows from that data frame that meet the condition 'ap_lo' <= 'ap_hi'
  # Leave out "extreme values" by using percentiles 
  # we check the [condition], indentifying rows that are greater than the 2.5% percentile of the height data, then pull rows that meet the condition from df_heat, therefore leaving out the too-small values
  df_heat = df_heat[df['height'] >= df['height'].quantile(0.025)] # pull out rows that have a height greater than or equal to the 2.5% percentile of the height data
  df_heat = df_heat[df['height'] <= df['height'].quantile(0.975)] # pull out rows that have a height less than or equal to the 97.5% percentile of the height data
  df_heat = df_heat[df['weight'] >= df['weight'].quantile(0.025)] # pull out rows that have a weight value greater than or equal to the 2.5% percentile of the weight data
  df_heat = df_heat[df['weight'] <= df['weight'].quantile(0.975)] # pull out rows that have a weight less than or equal to the 97.5% percentile of the weight data
  print(df_heat)

  # Calculate the correlation matrix
  corr = df_heat.corr() 

  # Generate a mask for the upper triangle
  mask = np.triu(corr)

  # Set up the matplotlib figure
  fig, ax = plt.subplots(figsize=(16,16))

  # Draw the heatmap with 'sns.heatmap()'
  sns.heatmap(corr, mask=mask, annot=True, fmt='.1f')

  # Do not modify the next two lines
  fig.savefig('heatmap.png')
  return fig


# RUN FUNCTIONS
draw_cat_plot()
draw_heat_map()

