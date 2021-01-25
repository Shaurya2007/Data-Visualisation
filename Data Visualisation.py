import plotly_express as px
import csv
import pandas as pd

df = pd.read_csv("Data.csv")

data_list = df["date"].tolist()
cases_list = df["cases"].tolist()
country_list = df["country"].tolist()

fig = px.scatter(x = data_list , y = cases_list , color = country_list)
fig.show()
