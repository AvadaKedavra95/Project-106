import csv
import plotly.express as px
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df=csv.DictReader(f)
        fig=px.scatter(df,x="Marks In Percentage",y="Days Present")
        fig.show()

def getDataSource(data_path):
    temperature=[]
    icecream_sales=[]
    with open(data_path) as f:
        df=csv.DictReader(f)
        for row in df:
            temperature.append(float(row["Marks In Percentage"]))
            icecream_sales.append(float(row["Days Present"]))
    return{"x":temperature,"y":icecream_sales}

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("Correlation between Marks In Percentage and Days Present is : ",correlation[0,1])

def setup():
    data_path="Student Marks vs Days Present.csv"
    data_source=getDataSource(data_path)
    findCorrelation(data_source)
    plotFigure(data_path)

setup()