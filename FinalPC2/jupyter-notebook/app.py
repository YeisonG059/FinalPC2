import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import pymysql

total=[]
total2=[]
total3=[]
total4=[]
total5=[]
total6=[]
total7=[]
total8=[]
total9=[]
total10=[]
total11=[]
total12=[]
total13=[]

def request():
    sql = "select * from hurtos.table_name as tb where tb.SEXO = 'MASCULINO'"
    cur.execute(sql)
    for row in cur:
        total.append(row)

    sql = "select * from hurtos.table_name as tb where tb.SEXO = 'FEMENINO'"
    cur.execute(sql)
    for row in cur:
        total2.append(row)

    sql = "select * from hurtos.table_name as tb where tb.ARMA_EMPLEADA = 'SIN EMPLEO DE ARMAS'"
    cur.execute(sql)
    for row in cur:
        total3.append(row)

    sql = "select * from hurtos.table_name as tb where tb.ARMA_EMPLEADA = 'ARMA BLANCA'"
    cur.execute(sql)
    for row in cur:
        total4.append(row)

    sql = "select * from hurtos.table_name as tb where tb.ARMA_EMPLEADA = 'ARMA DE FUEGO'"
    cur.execute(sql)
    for row in cur:
        total5.append(row)

    sql = "select * from hurtos.table_name as tb where tb.ARMA_EMPLEADA = 'CONTUNDENTES'"
    cur.execute(sql)
    for row in cur:
        total6.append(row)

    sql = "select * from hurtos.table_name as tb where tb.MOVIL_AGRESOR = 'VEHICULO'"
    cur.execute(sql)
    for row in cur:
        total7.append(row)

    sql = "select * from hurtos.table_name as tb where tb.MOVIL_AGRESOR = 'A PIE'"
    cur.execute(sql)
    for row in cur:
        total8.append(row)

    sql = "select * from hurtos.table_name as tb where tb.MOVIL_AGRESOR = 'PASAJERO BUS'"
    cur.execute(sql)
    for row in cur:
        total9.append(row)

    sql = "select * from hurtos.table_name as tb where tb.MOVIL_AGRESOR = 'CONDUCTOR TAXI'"
    cur.execute(sql)
    for row in cur:
        total10.append(row)

    sql = "select * from hurtos.table_name as tb where tb.MOVIL_AGRESOR = 'BICICLETA'"
    cur.execute(sql)
    for row in cur:
        total11.append(row)

    sql = "select * from hurtos.table_name as tb where tb.MOVIL_AGRESOR = 'CONDUCTOR MOTOCICLETA'"
    cur.execute(sql)
    for row in cur:
        total12.append(row)

    sql = "select * from hurtos.table_name as tb where tb.MOVIL_AGRESOR = 'PASAJERO MOTOCICLETA'"
    cur.execute(sql)
    for row in cur:
        total13.append(row)



db = pymysql.connect(host='10.5.0.1', port=32000, user='root', password='root',database='hurtos')
cur = db.cursor(pymysql.cursors.DictCursor)
request()

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

df = pd.DataFrame({
    "Bogota": ["Masculino","Femenino"],
    "Numero de casos": [len(total), len(total2)],
    "Genero": ["Masculino", "Masculino"]
})

fig = px.bar(df, x="Bogota", y="Numero de casos", barmode="group")

df2 = pd.DataFrame({
    "Bogota": ["Sin arma", "Arma blanca", "Arma de fuego", "Contundentes"],
    "Numero de casos": [len(total3), len(total4),len(total5), len(total6)],
    "Genero": ["Masculino", "Masculino","Masculino", "Masculino"]
})

fig2 = px.bar(df2, x="Bogota", y="Numero de casos", barmode="group")

df3 = pd.DataFrame({
    "Bogota": ['Vehiculo', 'A pie', 'Pasajero bus', 'Conductor taxi', 'Bicicleta', 'Conductor motocicleta', 'Pasajero motocicleta'],
    "Numero de casos": [len(total7), len(total8), len(total9), len(total10), len(total11), len(total12), len(total13)],
    "Genero": ["Masculino", "Masculino","Masculino", "Masculino", "Masculino","Masculino", "Masculino"]
})

fig3 = px.bar(df3, x="Bogota", y="Numero de casos", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hurtos en Bogota'),
    html.Div(children='''
        Cantidad de hurtos por genero.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    ),
    html.Div(children='''
        Cantidad de hurtos dependiendo del arma usada por el agresor.
    '''),
    dcc.Graph(
        id='example-graph2',
        figure=fig2
    ),
    html.Div(children='''
        Cantidad de hurtos dependiendo del vehiculo utilizado por el agresor.
    '''),
    dcc.Graph(
        id='example-graph3',
        figure=fig3
    )
])



if __name__ == '__main__':
  app.run_server(host='0.0.0.0', port=8080, debug=True)
