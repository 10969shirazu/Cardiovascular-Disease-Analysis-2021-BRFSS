import pandas as pd 
from warnings import simplefilter
simplefilter(action="ignore",category=pd.errors.PerformanceWarning)

df = pd.read_sas("LLCP2022.XPT")
df.head(12)
df.to_csv("cdc.csv")
