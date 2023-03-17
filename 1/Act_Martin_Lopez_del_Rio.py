import pandas as pd

'''

Actividad de Martín López del Río

'''
df = pd.read_csv('finanzas2020.csv',sep='\t') #importamos BDD


print('Las columnas a continuación tiene valores no numéricos:')
print(df.select_dtypes(exclude=['number'])) #Comprobamos columnas con valores no numericos
print('Vamos a limpiar la BDD')

def limpiar():
    global df
    
    try:
        df = df.apply(pd.to_numeric) #Intentamos cambiar columnas a formato num
        print('Todas las columnas se han podido convertir a formato numérico')
    
    except Exception as e:
        
        #Eliminamos apóstrofes de los valores en columnas tipo objeto
        
        string_cols = df.select_dtypes(include='object').columns
        df[string_cols] = df[string_cols].apply(lambda x: x.str.strip("'"))
        
        #Reemplazamos strings con 0 y cambiamos a numérico
        df = df.apply(lambda x: pd.to_numeric(x, errors='coerce')).fillna(0)

        df = df.apply(pd.to_numeric)

        print (df.dtypes)
        print('La base de datos se ha podido limpiar')

def col(): #lista con filas*columnas
    a=list(df.shape)
    if a[1] <12:
        print( 'Hay menos de 12 columnas')
    else:
        print(f'La base de datos tiene {a[0]} filas y {a[1]} columnas')

def empty_cols(): #detectar columnas vacías, en caso de que haya alguna, eliminarla
    try:
        empty_cols = [col for col in df.columns if df[col].isnull().all()]
        if empty_cols ==[]:
            print('No hay columnas vacías')
    except:
        df.drop(empty_cols,axis=1,inplace=True)
        print(f'Se han eliminado las columnas vacías {empty_cols} ')

def calculos():
    global dict1,dict
    try: 
        dict1={} #Diccionario que se completa con clave (mes) y valor max de cada columna

        for i,col in enumerate (df.columns):
            dict1[col]=df[col].max()
        max_key=max(dict1,key=dict1.get)
        max_value=max(dict1.values())

        print(f' El mes en el que más se ahorro es {max_key} con {max_value}€')

        dict2={} # #Diccionario que se completa con clave (mes) y valor min de cada columna

        for i,col in enumerate (df.columns):
            dict2[col]=df[col].min()
        min_key=min(dict2,key=dict2.get)
        min_value=min(dict2.values())

        print(f' El mes en el que más se gastó es {min_key} con {min_value*(-1)}€')

        #Cálculos para todo el dataframe
        negative_mean = df[df < 0].mean().mean()
        print(f'La media de gasto anual es {negative_mean} €')

        pos_mean = df[df > 0].mean().mean()
        print(f'La media de gasto anual es {pos_mean} €')

        gasto_total=df[df<0].sum().sum()
        print(f'El gasto total del año es de {gasto_total*(-1)} €')

        ahorro_total=df[df>0].sum().sum()
        print(f'Los ingresos totales del año son de {ahorro_total} €')
    except Exception as e:
        print('Tenemos algunos problemas con los datos: ', e)

limpiar()
col()
empty_cols()
calculos()