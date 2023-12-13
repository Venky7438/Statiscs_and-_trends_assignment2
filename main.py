#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:54:07 2023
@author: Venkatesh
"""

"""
# Libraries Required
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis


def dataframe_loading_reading(filepath):
    """
        Load a CSV file into a pandas DataFrame
        and create a reversed DataFrame.

        Parameters:
        - filepath (str): The file path to the CSV file.

        Returns:
        - df : Original DataFrame loaded from the CSV file.
        - df_reverse : Reversed DataFrame with 'Country Name'
        and 'Time' columns swapped.
    """
    df = pd.read_csv(filepath)
    df_reverse = df.copy()
    df_reverse[['Country Name' , 'Time']] =  \
        df_reverse[['Time' , 'Country Name']]
    df_reverse = \
        df.rename(columns = {'Country Name': 'Time' , 'Time': 'Country Name'})

    return df,df_reverse


def kurtosisMap(Data , value):
    """
        Create a bar plot to visualize the kurtosis of a variable.

        Parameters:
        - Data (list or array-like): Data points or
        categories for the x-axis.
        - value (float): The kurtosis value to be plotted.

        Returns:
        None
    """
    plt.bar(Data , [value] , color = 'blue')
    plt.title('kurtosis plot for Current health expenditure' ,
              fontsize = 17)
    plt.ylabel('Kurtosis')
    plt.show()


def skewMap(Data , value):
    """
        Create a bar plot to visualize the skewness of a variable.

        Parameters:
        - Data (list or array-like): Data points or categories for the x-axis.
        - value (float): The skewness value to be plotted.

        Returns:
        None
    """
    plt.figure(figsize = (6 , 4))
    plt.bar(Data , [value] , color = 'blue')
    plt.title('People using safely managed drinking water services (% of population)'
              , fontsize = 17)
    plt.ylabel('Skewness')
    plt.show()


def lineMap(Data):
    """
        Create a line plot to visualize the trend of a variable over time
        for selected countries.

        Parameters:
        - Data (pd.DataFrame): DataFrame containing data for multiple
        countries and years.

        Returns:
        None
    """

    for country in ['Singapore' , 'Malaysia' , 'Canada' , 'France' , 'Germany']:
        country_data = Data[Data['Country Name'] == country]
        plt.plot(country_data['Time'] ,
                 country_data
                 ['Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]'] ,
                 label = country)

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Current health expenditure')
    plt.title('Current health expenditure' , fontsize = 17)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)
    plt.show()


#Read and loading datasets
countryData , timeData = dataframe_loading_reading('Dataset.csv')
print("country data")
print(countryData.head())
print("time data")
print(timeData.head())

#Statistical analysis methods
countryData['Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]']\
    = pd.to_numeric(countryData['Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]'] ,
                    errors = 'coerce')
describes_statistics = \
    countryData['Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]']\
        .describe()
print(describes_statistics)

median_statistics = countryData['Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]']\
    .median()
print("median statistics" , median_statistics)

#kurtosis value
kurtosisData = countryData['Current health expenditure (% of GDP) [SH.XPD.CHEX.GD.ZS]']\
    .dropna()
kurtosis_value = kurtosis(kurtosisData , fisher=False)
print("Kurtosis:" , kurtosis_value)
kurtosisMap(kurtosisData , kurtosis_value)

#skewness value
countryData['People using safely managed drinking water services']\
    = pd.to_numeric(countryData['People using safely managed drinking water services'] ,
                    errors = 'coerce')
skewnessData = countryData['People using safely managed drinking water services'].dropna()
skewValue = skewnessData.skew()
# Plotting the skewness value
skewMap(skewnessData , skewValue)

lineMap(countryData)

barGraphData = countryData[countryData['Country Name'] == 'Canada']
selected_indicators = ['People using at least basic drinking water services' ,
                       'People using at least basic sanitation services' ,
                       'People using safely managed drinking water services']
bar_width = 0.2
barGraphData['People using at least basic drinking water services'] = \
    pd.to_numeric(barGraphData['People using at least basic drinking water services'] ,
                  errors='coerce')
bar_positions = np.arange(len(barGraphData['People using at least basic drinking water services']))

# Create bar plots for each indicator
for i , indicator in enumerate(barGraphData[selected_indicators]):  # Exclude 'Country Name'
    plt.bar(bar_positions + i * bar_width , barGraphData[indicator] ,
            width = bar_width , label = indicator)

# Set the labels and title
plt.xlabel('Year')
plt.ylabel('Values')
plt.title('Grouped Bar Plot of Indicators for Australia' , fontsize = 18)

# Set the x-axis ticks and labels
plt.xticks(bar_positions + bar_width , barGraphData['Time'])

# Display the legend
plt.legend()

# Show the plot
plt.show()

pieData = countryData[countryData['Time'] == 2020]
# Plotting the pie chart
plt.figure(figsize = (8 , 8))
plt.pie(pieData['Tuberculosis case detection rate (%, all forms) [SH.TBS.DTEC.ZS]'] ,
        labels = pieData['Country Name'] , autopct = '%1.1f%%' , startangle = 140)
plt.title('Tuberculosis case detection rate of each  Country')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()











