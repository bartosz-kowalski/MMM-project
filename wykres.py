import matplotlib.pyplot as plt
import subprocess as sb

m=input("Wprowadź masę obiektu: ")
b=input("Wprowadź współczynnik oporu powietrza obiektu: ")
y0=input("Wprowadź wysokość początkową obiektu: ")
h=-1*input("Wprowadź krok całkowania: ")
#v0=input("Wprowadź prękość początkową obiektu: ")

sb.run("g++ mmm.cpp -o mmm", shell=True, stdout=sb.PIPE)
command="./mmm "+m+' '+b+' '+y0+' '+h
sb.run(command, shell=True, stdout=sb.PIPE)

file = open(r"wyniki.csv", "rt")

file.readline()
pocz=file.tell()
lines = len(file.readlines())
file.seek(pocz)
y=[]
v=[]
t=[]

for i in range(lines-1):
    s=file.readline()
    s=s.split(';')
    t.append(float(s[0]))
    y.append(float(s[1]))
    v.append(abs(float(s[2])))

plt.plot(t,y,t,v)
plt.grid(True)
plt.xlabel("Czas [s]")
plt.ylabel("Wysokość [m] / Prędkość [m/s]")
plt.suptitle("Wysokość i prędkość w zaleności od czasu")
plt.title("masa: "+m+", wsp. oporu b: "+b+", wys. początkowa: "+y0)
plt.show()
