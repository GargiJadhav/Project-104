import pandas as pd

data  = pd.read_csv("heightWeight.csv")

weight = data["Weight(Pounds)"].tolist()

n = len(weight)

sum = 0

for i in weight :
    sum = sum + i

mean = sum/n

print("Mean is " , mean)









