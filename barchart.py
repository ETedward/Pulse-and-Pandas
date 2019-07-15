import pandas as pd
import os

# read primary programming languages from CSV file
CSV_Path = os.path.join('data.csv')

df = pd.read_csv(CSV_Path, usecols = [7,8])
df = df.rename(index=str, columns={'Which language would you like to learn?': 'new language',
                                   'Which language(s) do you primarily use?': 'old language'})

# new lang dictionary
newlang = {
    "PHP": 0,
    "JavaScript": 0
}

# iterate for frequencies of new lang
for r in range (len(df)):
    key = df.loc[str(r),'new language']
    if key not in newlang:
        newlang.update({key : 1})
    else:
        numb = newlang.get(key) + 1
        newlang.update({key : numb})

# convert dict to two lists (for plotting bar chart)
langs = [k for k in newlang.keys()]
freqs = [j for j in newlang.values()]

# old lang dictionary
oldlang = {
    "PHP": 0,
    "JavaScript": 0,
}

# iterate for frequencies of old lang
for r in range (len(df)):
    key = df.loc[str(r),'old language']
    for k in key.split(", "):
        if k not in oldlang:
            oldlang.update({k : 1})
        else:
            numb = oldlang.get(k) + 1
            oldlang.update({k : numb})

oldlang.update({'Clojure': 0})

# convert old lang into 2 separate lists
ol = [k for k in oldlang.keys()]
ofreqs = [j for j in oldlang.values()]

# import plotly packages
import plotly.graph_objs as go
import plotly.offline as offline

trace1 = go.Bar(
    x=ol,
    y=ofreqs,
    name='Primary Language'
)

trace2 = go.Bar(
    x=langs,
    y=freqs,
    name='Learning Goal'
)

data = [trace1, trace2]
layout = go.Layout(
    barmode='group'
)

offline.plot(data, filename='group-bar')

""" 
# create plotly bar chart data
newdata = [go.Bar(
            x=langs,
            y=freqs
    )]
"""

olddata = [go.Bar(
            x=ol,
            y=ofreqs
    )]

# plot bar charts for frequencies of new and old languages

#offline.plot(newdata, filename='new-bar')
offline.plot(olddata, filename='old-bar')

