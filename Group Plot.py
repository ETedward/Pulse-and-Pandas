import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

CSV_Path = os.path.join('pandaclean.csv')

df = pd.read_csv(CSV_Path, skiprows = 922, nrows=1293, usecols=[0,1,2,3])
headers = ["email", "Level", "Location", "Score"]
df.columns = headers

print (df)

grouped = df.groupby(['Location'])

x2 = np.random.randint(1, size=(7, 4))
print (x2)

i = 0
for place, gdf in grouped:
    print("tagged")
    print (gdf)
    total = gdf.shape[0] # gives row count
    great = 0
    good = 0
    bad = 0

    for j in range(total):
        if gdf.iloc[j,3] > 3.1:
            great = great + 1
        elif gdf.iloc[j,3] < 3:
            bad = bad + 1
        else:
            good = good + 1

    x2[i][0] = great
    x2[i][1] = bad
    x2[i][2] = good
    x2[i][3] = total

    i = i + 1

pd.DataFrame(x2).to_csv("LocationGGB.csv")