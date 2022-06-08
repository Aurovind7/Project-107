import plotly.express as px
import pandas as pd
import csv



df=pd.read_csv("data.csv")
all_data=df.groupby(["student_id","level"],as_index=False)["attempt"].mean()
print(all_data)
fig=px.scatter(all_data, x="student_id", y="level",size="attempt", color="attempt")

fig.show()