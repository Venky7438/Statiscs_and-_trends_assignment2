#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 02 20:54:07 2023
@author: Ajay Prabhat Gorrumuchu
"""

"""
# Importing Required Libraries
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.stats import skew
from scipy.stats import kurtosis


def world_bank_data_frame(path):

    df = pd.read_csv(path)
    transposed = df.copy()
    transposed[['Country Name','Time']] = transposed[['Time','Country Name']]
    transposed = transposed.rename(columns={'Country Name': 'Time', 'Time': 'Country Name'})
    cleanedDataset = transposed.dropna()
    return df , transposed , cleanedDataset

def claimsOnCentralGov(Data):
    for country in countryList:
        country_data = Data[Data['Country Name'] == country]
        plt.plot(country_data['Time'],
                 country_data['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'],
                 label=country)

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Claims on central government')
    plt.title('Claims on central government (annual growth as % of broad money)', fontsize=17)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)
    plt.show()


def stocksTradedPercentOfGdp(data):
    # Plotting the bar graph
    data.plot(kind='bar', stacked=True, figsize=(10, 6))
    plt.title('Stock Trades of Three Countries Over Years')
    plt.xlabel('Year')
    plt.ylabel('Stocks traded (% of GDP)')
    plt.legend(title='Country')
    plt.show()


def wholeSalePriceIndex(data):
    # Plotting a pie chart using Seaborn and Matplotlib
    plt.figure(figsize=(8, 8))
    plt.title('Wholesale price index (INDIA)', fontsize=17)
    # Create a pie chart using matplotlib
    plt.pie(data['Wholesale price index (2010 = 100) [FP.WPI.TOTL]'], labels=data['Time'],
            autopct='%1.1f%%', startangle=140)
    # Display the chart
    plt.show()


def realIntrestRate(data):
    for country in IntrestedCountries:
        country_data = data[data['Country Name'] == country]
        plt.plot(country_data['Time'],
                 country_data['Real interest rate (%) [FR.INR.RINR]'],
                 label=country)

    # Adding labels and title
    plt.xlabel('Year')
    plt.ylabel('Real interest rate (%) ')
    plt.title('Real interest rate (%) of different countries', fontsize=17)

    # Adding legend
    plt.legend()

    # Display a grid
    plt.grid(True)
    plt.show()


def Stocks_traded(data):
    # Plotting using Seaborn
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Country Name', y='Stocks traded, total value (current US$) [CM.MKT.TRAD.CD]',
                data=data, palette='viridis', legend=False)
    plt.title('Stocks traded, total value (current US$) in 2019', fontsize=17)
    plt.xlabel('Country')
    plt.ylabel('Stocks traded, total value (current US$)')
    plt.show()


def commercialBank(data):
    sns.set(style="whitegrid")
    # Plotting a pie chart using Matplotlib with Seaborn style
    plt.figure(figsize=(8, 8))
    plt.title('Commercial bank branches (per 100,000 adults)', fontsize=17)

    # Create a pie chart using matplotlib
    plt.pie(data['Commercial bank branches (per 100,000 adults) [FB.CBK.BRCH.P5]'], labels=data['Country Name'],
            autopct='%1.1f%%', startangle=140)

    # Display the chart
    plt.show()


dataTime , dataCountry , cleanedData = world_bank_data_frame('Dataset.csv')
print("Data Country")
print(dataCountry.head())
print("Data Time")
print(dataTime.head())
print("cleaned dataset")
print(cleanedData.head())

"""
Task 2: Statistical Methods 
"""
#Describes Method
dataCountry['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'] = pd.to_numeric(dataCountry['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'],errors='coerce')
describeMethod = dataCountry['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'].describe()
print(describeMethod)

#Median
median = dataCountry['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'].median()
print("median",median)

#mode
mode = dataCountry['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'].mode()
print("mode",mode)

#skewness
skewnessvalue = dataCountry['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'].skew()
print('skewness',skewnessvalue)

#kurtosis
kurtosisvalue = dataCountry['Claims on central government (annual growth as % of broad money) [FM.AST.CGOV.ZG.M3]'].kurtosis()
print('kurtosis',kurtosisvalue)

#Visualizations
#Line Graph
countryList = ['Australia','Canada','China','Germany','India','Malaysia']
dataCountry['Time'] = pd.to_numeric(dataCountry['Time'],errors='coerce')
lineGraphdataCountry = dataCountry[(dataCountry['Time'] >= 2010) & (dataCountry['Time'] <= 2020)]

claimsOnCentralGov(lineGraphdataCountry)

#BAR GRAPH
# barGraphData = dataCountry[(dataCountry['Country Name']) == 'United Kingdom']
# barGraphData['Time'] = pd.to_numeric(barGraphData['Time'],errors='coerce')
barGraphData = dataCountry.copy()
selected_countries = ['Malaysia', 'United States', 'China']
filtered_data = barGraphData[barGraphData['Country Name'].isin(selected_countries)]
filtered_data = filtered_data[(filtered_data['Time'] >= 2010) & (filtered_data['Time'] <= 2019)]
filtered_data['Stocks traded, total value (% of GDP) [CM.MKT.TRAD.GD.ZS]'] = pd.to_numeric(filtered_data['Stocks traded, total value (% of GDP) [CM.MKT.TRAD.GD.ZS]'],errors='coerce')

pivot_df = filtered_data.pivot(index='Time', columns='Country Name', values='Stocks traded, total value (% of GDP) [CM.MKT.TRAD.GD.ZS]')
stocksTradedPercentOfGdp(pivot_df)

#Pie graph
pieGraphData = dataCountry[dataCountry['Country Name'] == 'India']
pieGraphData = pieGraphData.dropna()
print(pieGraphData['Wholesale price index (2010 = 100) [FP.WPI.TOTL]'])
pieGraphData['Time'] = pd.to_numeric(pieGraphData['Time'],errors='coerce')
pieGraphData['Wholesale price index (2010 = 100) [FP.WPI.TOTL]'] = pd.to_numeric(pieGraphData['Wholesale price index (2010 = 100) [FP.WPI.TOTL]'],errors='coerce')

wholeSalePriceIndex(pieGraphData)


#real intrest rate
IntrestedCountries = ['China','India','Indonesia','Malaysia','United States']
realIntrestData = dataCountry[(dataCountry['Time'] >= 2000) & (dataCountry['Time'] <= 2015)]
# realIntrestData= dataCountry[dataCountry['Country Name'].isin(selected_countries)]

realIntrestRate(realIntrestData)

# Filter data for the year 2019
Stocks_traded_2019 = dataCountry[dataCountry['Time'] == 2019].dropna()
IntrestedCountries = ['China','India','Indonesia','Malaysia','Afghanistan','Australia','Canada','Germany','Indonesia','Poland']
stock_trade_dollar_2019 = Stocks_traded_2019[Stocks_traded_2019['Country Name'].isin(IntrestedCountries)]

Stocks_traded(stock_trade_dollar_2019)

#Deposit Intrest Rate
commercial_bank_branches = dataCountry[dataCountry['Time']==2019]
commercial_bank_branches  = commercial_bank_branches .dropna()
commercial_bank_branches ['Commercial bank branches (per 100,000 adults) [FB.CBK.BRCH.P5]'] = pd.to_numeric(commercial_bank_branches ['Commercial bank branches (per 100,000 adults) [FB.CBK.BRCH.P5]'],errors='coerce')

commercialBank(commercial_bank_branches)


