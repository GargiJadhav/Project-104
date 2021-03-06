import pandas as pd

data  = pd.read_csv("heightWeight.csv")

weight = data["Weight(Pounds)"].tolist()

n = len(weight)

weight.sort()

if n % 2 ==0:
    m1 = float(weight[n//2])
    m2 = float(weight[n//2 - 1])
    median = (m1+m2)/2
else :
    median = float(weight[n//2])

print("Median is ", median)