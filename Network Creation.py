import pandas as pd
import numpy as np
from scipy import sparse

players = pd.read_csv("advanced.csv")

all = pd.Series(players['name'].unique())

adj2014 = np.zeros((len(all), len(all)))

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2014)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2014)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2014[i,ind] = 1

adj2015 = adj2014.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2015)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2015)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2015[i,ind] = 1

adj2016 = adj2015.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2016)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2016)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2016[i, ind] = 1

adj2017 = adj2016.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2017)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2017)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2017[i, ind] = 1

adj2018 = adj2017.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2018)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2018)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2018[i, ind] = 1

adj2019 = adj2018.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2019)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2019)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2019[i, ind] = 1

adj2020 = adj2019.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2020)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2020)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2020[i, ind] = 1

adj2021 = adj2020.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2021)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2021)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2021[i, ind] = 1

adj2022 = adj2021.copy()

for i, x in enumerate(all):
    team = players[(players['name'] == x) & (players['year'] == 2022)]['team']
    if not team.empty:
        teammates = players[(players['team'] == team.iloc[0]) & (players['year'] == 2022)]['name']
        for y in teammates.iteritems():
            ind = all[all == y[1]].index[0]
            adj2022[i, ind] = 1

np.savetxt('2014.csv', adj2014, fmt="%i")
np.savetxt('2015.csv', adj2015, fmt="%i")
np.savetxt('2016.csv', adj2016, fmt="%i")
np.savetxt('2017.csv', adj2017, fmt="%i")
np.savetxt('2018.csv', adj2018, fmt="%i")
np.savetxt('2019.csv', adj2019, fmt="%i")
np.savetxt('2020.csv', adj2020, fmt="%i")
np.savetxt('2021.csv', adj2021, fmt="%i")
np.savetxt('2022.csv', adj2022, fmt="%i")

