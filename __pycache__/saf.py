import pandas as pd

ruta="C:\Listados\CR_lrollo_proceso.txt"

df= pd.read_csv(ruta,sep='\t')
print(df)

