import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

# -=-=-=-=-=-=- PANDAS -=-=-=-=-=-=
# load dataframe
df = pd.read_csv("pennData.csv")
pennData = pd.DataFrame(df)

print("-_"*20)
print("Head of the DataFrame") #first 5 rows of df
print(pennData.head())

print("-_"*20)
print("Tail of the DataFrame") #last 5 rows of df
print(pennData.tail())

print("-_"*20)
print("Summary of the DataFrame") #data count per column, data types
print(pennData.info())

print("-_"*20)
print("Stats of the DataFrame") #mean,min,max,stdev,percentiles,count (only works for numbers)
print(round(pennData.describe()))

print("-_"*20)
print("Count of Students in each Pathway") #looks at the "Pathway" column and counts the occurences of each values
print(pennData["Pathway"].value_counts())

print("-_"*20)
print("Average GPA per year") #groups data using the first argument("Year") and caluculates the values in the second argument["GPA"]
print(pennData.groupby("Year")["GPA"].mean())

print("-_"*20)
print("Top 3 students by GPA") #grabs the top 3 values after being sorted, and prints those 
print(pennData.sort_values(by = "GPA", ascending = False).head(3))

print("-_"*20)
print("Students with GPA > 3.5") #prints the dataframe for everyone with a GPA value higher than 3.5
print(pennData[pennData["GPA"]>3.5])

print("-_"*20)
print("First Student Data") #pulls all data for a specific index (iloc = index location)
print(pennData.iloc[0])

# -=-=-=-=-=-= MATPLOTLIB -=-=-=-=-=-=
print("-_"*20)
print(pennData.groupby("Year")["GPA"].mean())  #still pandas #groups data for a graph by (first axis)[second axis]

print("-_"*20)
pennData.groupby("Year")["GPA"].mean().plot(kind='bar', color='red', edgecolor='black') 
    #takes the grouped values and turns it into a graph by using .plot(kind=type of graph, color=color of graph, edgecolor = outlines the bar in a color)

plt.title("this is the title of the graph") #adding labels
plt.xlabel("label of x axis")
plt.ylabel("label of y axis")
plt.show() #shows the graph
