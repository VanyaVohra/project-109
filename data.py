import csv
import pandas as pd
import plotly.figure_factory as ff
import random
import statistics

df = pd.read_csv("StudentsPerformance.csv")
mathList = df["math score"].to_list()

mMean = statistics.mean(mathList)
print("Mean of the given dataset is: ", mMean)

mMedian = statistics.median(mathList)
print("Median of the given dataset is: ", mMedian)

mMode = statistics.mode(mathList)
print("Mode of the given dataset is: ", mMode)

mSd = statistics.stdev(mathList)
print("Stand Deviation of the given dataset is: ", mSd)

start1, end1 = mMean - mSd, mMean + mSd
listOfData1 = [result for result in mathList if result>start1 and result<end1]
print("Percentage of data that lies between 1 Standard Deviation: ", len(listOfData1)*100/len(mathList), "%")

start2, end2 = mMean - 2*mSd, mMean + 2*mSd
listOfData2 = [result for result in mathList if result>start2 and result<end2]
print("Percentage of data that lies between 2 Standard Deviation: ", len(listOfData2)*100/len(mathList), "%")

start3, end3 = mMean - 3*mSd, mMean + 3*mSd
listOfData3 = [result for result in mathList if result>start3 and result<end3]
print("Percentage of data that lies between 3 Standard Deviation: ", len(listOfData3)*100/len(mathList), "%")