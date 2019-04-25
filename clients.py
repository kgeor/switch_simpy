import random
class params:
  PORTS=10
  RATE=100
  BUF=200
  DISTRIB=None
  CAM={}
  ports={}
class topo:
  for i in range(params.PORTS):
    cl=[None]*random.randint(1,4)
    for j in range(len(cl)):
      idc='p'+str(i+1)+'c'+str(j+1)
      params.CAM[idc]=i+1
      cl[j]=idc
    params.ports[i+1]=cl #SwitchPort()

  src=random.choice(params.ports[random.randint(1,params.PORTS)]) # its true, we generally randomize the port, not client
  dst=random.choice(params.ports[random.randint(1,params.PORTS)])
  #sport=port[params.CAM[src]]

  while (src[1:2]==dst[1:2]):
    dst=random.choice(params.ports[random.randint(1,params.PORTS)])

p=topo()    
print(p.src)
print(p.dst)
print(a.params.ports)

class wiring:
foreach cl in CAM:
Swport[cl].in=cl.gen
cl.sink=Swport[cl].out

'''
params.CAM и Port словари сделать глобальными. Возможно инициализировать их в спец классе build
Класс switchport перевести в buffer, новый класс switcport  имеет два атрибута, равные экземплярам класса buffer
Сделать класс switch, который соответственно будет сопоставлять порт входа.in с портом выхода.out:


Class clients:
Def init(self, num, params.ports) 
Num, params.ports - равноразмерные списки

Class switchport(rate, bufsize):
Self.in=None #буфер приходящих извне пакетов
Self.out=None #буфер уходящих с коммутатора

Class switch:
Def init(self, topo) 

i=p.params.CAM[topo.dst]
SwitchPort[i-1].out=topo
#мб добавить маааленькую рандомную задержку

class wiring:
foreach cl in CAM:
Swport[cl].in=cl.gen
cl.sink=Swport[cl].out

Вообще порядок:
Опред кво портов и их парам(с б) 
Опред кво клиентов и их парам(ид) 
Подсоединить клиентов к портам
Составить таблицы 
Инициализировать коммутатор, передав ему таблицы

Надо бы сделать так, чтобы в один момент пакеты отправляло опред число клиентов. 
В pgen для каждого клиента дать свое распределение времени отправки


'''