from django.shortcuts import render
import random,math,networkx as nx,matplotlib.pyplot as plt


# Create your views here.

def home(request):
    return render(request,'index.html',{"v":''})

def boton(request):
    U = 0 
    if request.method == 'GET':
        U = float(request.GET.get('umbral'))
    rango={
        "p":poblacion(U),
        "v":"Si"
    }  
    return render(request,'index.html',rango)

#Metodos
def disE(a,b):
    d=math.sqrt((math.pow(b[0]-a[0],2)+math.pow(b[1]-a[1],2)))
    return d

def poblacion(u):
    m=[]
    f=[]
    G=nx.DiGraph()
    for i in range(4):
        m.append([random.randrange(0,10),random.randrange(0,10)])
        G.add_node(str(m[i]))
    for j in range(len(m)):
        for k in range(j,len(m)):
            if conex(disE(m[j],m[k]),u)=="Si":
                G.add_edge(str(m[j]),str(m[k]))
            f.append([[j+1,k+1],m[j],m[k],disE(m[j],m[k]),conex(disE(m[j],m[k]),u)])
    pos = nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos,node_color="grey")
    nx.draw_networkx_labels(G, pos)
    nx.draw_networkx_edges(G, pos, edge_color='grey', arrows = True)
    plt.savefig("./static/Grafo.jpg")
    plt.clf()
    return f

def conex(a,u):
    if(u<a):
        return "Si"
    else:
        return "No"