import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
df = pd.read_csv('medical_examination.csv')

# Add 'overweight' column
df['overweight'] = round(df.weight/pow((df.height/100),2),1)

# Normalize data by making 0 always good and 1 always bad. If the value of 'cholesterol' or 'gluc' is 1, make the value 0. If the value is more than 1, make the value 1.


# Draw Categorical Plot
def draw_cat_plot():
    # Create DataFrame for cat plot using `pd.melt` using just the values from 'cholesterol', 'gluc', 'smoke', 'alco', 'active', and 'overweight'.
    df_cat = pd.melt(frame=df,id_vars='cardio',value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # Group and reformat the data to split it by 'cardio'. Show the counts of each feature. You will have to rename one of the columns for the catplot to work correctly.
    df_cat = df_cat.groupby('cardio').value_counts().to_frame().reset_index().sort_values(by=['variable']).rename(columns={0:'total'})
    

    # Draw the catplot with 'sns.catplot()'



    # Get the figure for the output
    fig = sns.catplot(data=df_cat,x='variable',y='total',hue='value',kind='bar',col='cardio')


    # Do not modify the next two lines
    fig.savefig('catplot.png')
    return fig


# Draw Heat Map
def draw_heat_map():
    # Clean the data
    df_heat = df[(df.ap_lo<=df.ap_hi)&(df['height']>=df['height'].quantile(0.025))&(df.height<=df['height'].quantile(0.975))&(df.weight>=df.weight.quantile(0.025))&(df.weight<=df.weight.quantile(0.975))]

    # Calculate the correlation matrix
    corr = round(df_heat.corr(),1)

    # Generate a mask for the upper triangle
    mask = np.triu(corr)



    # Set up the matplotlib figure
    fig, ax = sns.heatmap(corr,mask=mask,annot=True,linewidth=.8,center=0.00,vmax=0.24,vmin=-0.05,cbar=True,fmt='.1f')

    # Draw the heatmap with 'sns.heatmap()'



    # Do not modify the next two lines
    fig.savefig('heatmap.png')
    return fig
