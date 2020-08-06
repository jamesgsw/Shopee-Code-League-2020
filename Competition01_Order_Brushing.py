"""
Goal: The order brushing algorithm helps to identify orders that are not ordered by real users, 
but instead contact of the seller dispatching empty boxes in a bit to get more reviews

Inputs: order brushing dataset

Outputs: updated order brushing dataset
"""
#1. Importing Relevant Library
import pandas as pd

#2. Data Ingestion
df = pd.read_csv("order_brush_order.csv")
df1 = df.sort_values(by = ['shopid', 'userid'])

#3. Feature Engineering - event_time column
df1['event_time'] = pd.to_datetime(df1['event_time'])
df1['day_hour'] = df1['event_time'].dt.strftime('%d-%H')

#4. Calculate Concentration Rate Columns
df2 = pd.pivot_table(df1, index=["shopid", "day_hour"], values=["orderid", "userid"], aggfunc=lambda x: len(x.unique())).reset_index()
df2["Concentrate Rate"] = df2["orderid"]/df2["userid"]
df3 = df2[df2["Concentrate Rate"] >= 3]
df3