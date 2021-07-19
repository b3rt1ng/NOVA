import matplotlib.pyplot as plt
import numpy as np
import ast
from scipy.interpolate import make_interp_spline, BSpline

def render_weeks(data,name,index):
    plt.figure(figsize=(6, 2))
    caca=[0,0,0,0,0,0,0]
    days="0 1 2 3 4 5 6".split()
    for i in range(len(data[index])):
      if data[0][i][1]=="Monday":
        caca[0]=caca[0]+1
      if data[0][i][1]=="Tuesday":
        caca[1]=caca[1]+1
      if data[0][i][1]=="Wednesday":
        caca[2]=caca[2]+1
      if data[0][i][1]=="Thursday":
        caca[3]=caca[1]+1
      if data[0][i][1]=="Friday":
        caca[4]=caca[4]+1
      if data[0][i][1]=="Saturday":
        caca[5]=caca[5]+1
      if data[0][i][1]=="Sunday":
        caca[6]=caca[6]+1
    plt.plot(days, caca, "r--", color="r",linewidth=1)
    ticks,labels = list(range(0, 7)),"Lun Mar Mer Jeu Ven Sam Dim".split()
    plt.xticks(ticks, labels)
    plt.title("cacas de "+name[:-5])
    plt.grid()
    plt.savefig('temp.png')


def render_round_weeks(data,index):
    name = data[0][index]
    nombre = data[4][index]
    data = data[5][index]
    categories = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi',"Samedi","Dimanche"]
    base = [0,0,0,0,0,0,0]
    categories = [*categories, categories[0]]
    for i in range(len(data)):
        base[0]+=data[i].count("Monday")
        base[1]+=data[i].count("Tuesday")
        base[2]+=data[i].count("Wednesday")
        base[3]+=data[i].count("Thursday")
        base[4]+=data[i].count("Friday")
        base[5]+=data[i].count("Saturday")
        base[6]+=data[i].count("Sunday")
    base = [*base, base[0]]
    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(base))
    with plt.rc_context({'axes.edgecolor':'white', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'red'}):
        fig, (ax1) = plt.subplots(1,figsize=(8,8))
        ax1.grid()
        ax1 = plt.subplot(111, projection='polar')
        ax1.plot(label_loc, base, label='répartition des cacas de '+name[:-5], color="mediumslateblue")
        ax1.set_title(name[:-5]+' tu as fait '+str(nombre)+' cacas',color = "lightgreen", size=20, y=1.05)
        ax1.fill(label_loc, base, alpha=0.1)
        lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
        ax1.legend()
    plt.savefig('temp.png',transparent=True)

def render_round_weeks_everyone(data):
    names = data[0]
    data = data[5]
    categories = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi',"Samedi","Dimanche"]
    categories = [*categories, categories[0]]
    ent = []
    for j in range(len(data)):
        base = [0,0,0,0,0,0,0]
        for i in range(len(data[j])):
            base[0]+=data[j][i].count("Monday")
            base[1]+=data[j][i].count("Tuesday")
            base[2]+=data[j][i].count("Wednesday")
            base[3]+=data[j][i].count("Thursday")
            base[4]+=data[j][i].count("Friday")
            base[5]+=data[j][i].count("Saturday")
            base[6]+=data[j][i].count("Sunday")
        base = [*base, base[0]]
        ent.append(base)
    label_loc = np.linspace(start=0, stop=2 * np.pi, num=len(base))
    with plt.rc_context({'axes.edgecolor':'white', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'red'}):
        fig, (ax1) = plt.subplots(1,figsize=(8,8))
        ax1.grid()
        ax1 = plt.subplot(111, projection='polar')
        for i in range(len(ent)):
            ax1.plot(label_loc, ent[i], label='répartition des cacas de '+names[i][:-5])
            ax1.fill(label_loc, ent[i], alpha=0.1)
        lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
        ax1.set_title('cacas de tout le monde',color = "lightgreen", size=20, y=1.05)
        lines, labels = plt.thetagrids(np.degrees(label_loc), labels=categories)
        ax1.legend()
    plt.savefig('temp.png',transparent=True)
def render_moy(data,name,index):
    moy=[]
    for i in range(len(data[index])):
        moy.append(data[index][i][0])
    num=list(range(1, len(moy)+1))
    plt.figure(figsize=(6, 2))
    xnew = np.linspace(min(num), max(num), 300)
    spl = make_interp_spline(num, moy, k=3)
    power_smooth = spl(xnew)
    with plt.rc_context({'axes.edgecolor':'white', 'xtick.color':'white', 'ytick.color':'white', 'figure.facecolor':'red'}):
        # Temporary rc parameters in effect
        fig, (ax1) = plt.subplots(1,figsize=(6,2))
        ax1.plot(xnew, power_smooth, "r--", color="mediumslateblue",linewidth=1)
        ax1.plot(num, moy, "x", color="gold",linewidth=1)
        ax1.set_title("temps moyen des cacas de "+name[:-5],color = "lightgreen")
        ax1.grid()
    plt.savefig('temp.png',transparent=True)
