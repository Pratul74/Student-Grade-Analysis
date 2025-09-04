import pandas as pd
import numpy as np

#Loading the data
df=pd.read_csv("students.csv")
print(df.head())

#Calculating the total of each student
print("\n")
df["Total"]=df[["Math","Science","English","History","Computer"]].sum(axis=1)
print(df.head())

#Calculating the average of each student
df["Average"]=df["Total"]/5
print("\n")
print(df.head())

#Function to assign grade to each student
def get_grade(avg):
    if avg>=90:
        return "A"
    elif avg>=75:
        return "B"
    elif avg>=60:
        return "C"
    elif avg>=50:
        return "D"
    else:
        return "F"

#Using the get_grade function and applying the garde to each student
df["Grade"]=df["Average"].apply(get_grade)
print("\n")
print(df.head())

#Giving rank to each student based on total marks
print("\n")
df["Rank"]=df["Total"].rank(ascending=False,method="dense").astype(int)
df=df.sort_values("Rank")
print(df.head())

#Calculating class's average for each subjects
print("\n")
print("Class Average: ")
print(df[["Math","Science","English","History","Computer"]].mean())

#Top 3 student who scored max maxks in whole class
print("\n")
print("Top 3 students: ")
print(df.head(3))

#Calculating no of grades
print("\n")
print("Grade Counts: ")
print(df["Grade"].value_counts())

