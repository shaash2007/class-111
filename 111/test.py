import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import random
import statistics

df=pd.read_csv("math.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
std_deviation=statistics.stdev(data)
print(mean,std_deviation)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index=random.randint(0,len(data)-1)
        value=data[random_index]
        dataset.append(value)    
    mean=statistics.mean(dataset)
    return mean

mean_list=[]
for i in range (0,1000):
    set_of_mean=random_set_of_mean(100)
    mean_list.append(set_of_mean)

mean=statistics.mean(mean_list)
std_deviation=statistics.stdev(mean_list)
print(mean,std_deviation)
#fig=ff.create_distplot([mean_list],["student_mrks"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.20],mode="lines",name="mean"))
#fig.show()  

df=pd.read_csv("math2.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
print("intervention1",mean)

df=pd.read_csv("math3.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
print("intervention2",mean)

df=pd.read_csv("math4.csv")
data=df["Math_score"].tolist()
mean=statistics.mean(data)
print("intervention3",mean)