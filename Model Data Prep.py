import numpy as np
import pandas as pd
import networkx as netx

data = pd.read_csv("advanced.csv")
rosters = pd.read_csv("rosters.csv")

rosters = rosters.set_index(['name', 'team', 'year'])

data = data.join(rosters, on=['name', 'team', 'year'], lsuffix= "left")

graph2020 = netx.read_gexf("graph2021.gexf")
graph2021 = netx.read_gexf("graph2022.gexf")
graph2022 = netx.read_gexf("graph2022.gexf")

degrees21 = pd.DataFrame([[node, val] for (node, val) in graph2021.degree()])
degrees20 = pd.DataFrame([[node, val] for (node, val) in graph2020.degree()])
degrees20.columns = ['name', 'degree']
degrees20 = degrees20.set_index(['name'])
degrees21.columns = ['name', 'degree']
degrees21 = degrees21.set_index(['name'])

#between21 = pd.DataFrame([[node, val] for (node, val) in netx.betweenness_centrality(graph2021)])
#between20 = pd.DataFrame([[node, val] for (node, val) in netx.betweenness_centrality(graph2020)])
#between20.columns = ['name', 'degree']
#between21.columns = ['name', 'degree']
#between21 = between21.set_index(['name'])
#between20 = between20.set_index(['name'])

#load21 = pd.DataFrame([[node, val] for (node, val) in netx.load_centrality(graph2021)])
#load20 = pd.DataFrame([[node, val] for (node, val) in netx.load_centrality(graph2020)])
#load20.columns = ['name', 'degree']
#load21.columns = ['name', 'degree']
#load21 = load21.set_index(['name'])
#load20 = load20.set_index(['name'])

#close21 = pd.DataFrame([[node, val] for (node, val) in netx.closeness_centrality(graph2021)])
#close20 = pd.DataFrame([[node, val] for (node, val) in netx.closeness_centrality(graph2020)])
#close20.columns = ['name', 'degree']
#close21.columns = ['name', 'degree']
#close21 = close21.set_index(['name'])
#close20 = close20.set_index(['name'])

players2020 = data[data['year'] == 2020]
players2021 = data[data['year'] == 2021]
players2022 = data[data['year'] == 2022]

response21 = []
response22 = []

for name in players2021['name']:
    play20 = players2020[players2020['name'] == name]
    play21 = players2021[players2021['name'] == name]
    if len(play20) != 0 and len(play21) != 0:
        if play20['team'].iloc[0] == play21['team'].iloc[0]:
            response21.append([name, 0])
        else:
            response21.append([name, 1])

for name in players2022['name']:
    play21 = players2021[players2021['name'] == name]
    play22 = players2022[players2022['name'] == name]
    if len(play21) != 0 and len(play22) != 0:
        if play21['team'].iloc[0] == play22['team'].iloc[0]:
            response22.append([name, 0])
        else:
            response22.append([name, 1])

response21 = pd.DataFrame(response21)
response21.columns = ['name', 'transfer']
response21 = response21.set_index(['name'])

response22 = pd.DataFrame(response22)
response22.columns = ['name', 'transfer']
response22 = response22.set_index('name')

players2021 = players2021.join(response21, on='name')
#players2021 = players2021.join(between20, on='name')
players2021 = players2021.join(degrees20, on='name')
#players2021 = players2021.join(close20, on='name')
#players2021 = players2021.join(load20, on='name')
players2021.drop(['Unnamed: 0left', 'Unnamed: 0'], axis=1, inplace=True)

players2022 = players2022.join(response22, on='name')
#players2022 = players2022.join(between21, on='name')
players2022 = players2022.join(degrees21, on='name')
#players2022 = players2022.join(close21, on='name')
#players2022 = players2022.join(load21, on='name')
players2022.drop(['Unnamed: 0left', 'Unnamed: 0'], axis=1, inplace=True)

players2021.to_csv("players2021_output.csv")
players2022.to_csv("players2022_output.csv")