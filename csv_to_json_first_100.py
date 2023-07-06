import pandas as pd 
df = pd.read_csv("data/data.csv")
df.drop(columns=['Fire Alarm'], inplace=True)

df.head(100).to_json("data/sensors.json", orient='records')