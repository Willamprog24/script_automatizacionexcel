import pandas as pd

ruta = r'C:\Listados\CR_lrollo_proceso.txt'

df = pd.read_csv(ruta,delimiter='\t')
print(df.filter(codigo="085113"))


