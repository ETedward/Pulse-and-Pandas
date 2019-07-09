import pandas as pd
import os
import matplotlib.pyplot as plt

CSV_Path = os.path.join('Master_Pulse.csv')

df = pd.read_csv(CSV_Path, nrows=1371, usecols=[6,9,11,12,13,14,15,16,17])

headers = ["email", "Level", "Location", "Quality", "Quantity", "Communication", "Init" , "Prof", "Inte"]
df.columns = headers

s = df['Level'] == 'D1 Developer'
df = df.assign(Score = df.loc[:, "Quality"] + df.loc[:, "Quantity"] + df.loc[:, "Communication"])
#df = df.assign(Soft = df.loc[:, "Init"] + df.loc[:, "Prof"] + df.loc[:, "Inte"])

# delete columns df.drop(columns = "Init")
df = df.drop(["Quality", "Quantity", "Communication", "Init" , "Prof", "Inte"], axis = 1)

# sort by index / similar emails and average same person scores
df = df.sort_values('email') # sort based on a column

# take first score as the average of the scores for a developer
for r in range(1370):
    if df.iloc[r, 0] == df.iloc[r+1, 0] and df.iloc[r, 0] != df.iloc[r-1,0]:
        tmp = df.iloc[r, 3]
        N = 1
        R = r + 1
        while R < 10371 and df.iloc[r, 0] == df.iloc[R, 0]:
            tmp += df.iloc[R, 3]
            R = R + 1
            N = N + 1
        df.iloc[r, 3] = tmp / N

df = df.drop_duplicates(subset = 'email')

# sort by Level and export D0A, D0B, D1, D+
df = df.sort_values('Level')
df.to_csv('pandaclean.csv')

grouped = df.groupby('Location').size()
fig = plt.figure()
subplot = fig.add_subplot(1,1,1)
subplot.set_ylabel("Developers")
subplot.set_title("Andelan by Region")
grouped.plot(ax = subplot)
fig.savefig('Andela1.png')
plt.show()


