import plotly.figure_factory as ff
import pandas as pd

dataframe = pd.read_csv("data.csv")
graph = ff.create_distplot([dataframe["Height"].tolist()],["height"],show_hist=False)
graph.show()