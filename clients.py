import random
class pkt:
  num=10 # ports
  cam={}
  ports={}
  for i in range(num):
    clients=random.randint(1,4)
    cl=[None]*clients
    for j in range(clients):
      idc='p'+str(i+1)+'c'+str(j+1)
      cam[idc]=i+1
      cl[j]=idc
    ports[i+1]=cl #SwitchPort()

  src=random.choice(ports[random.randint(1,num)]) # its true, we generally randomize the port, not client
  #sport=port[cam[src]]
  dst=random.choice(list(cam.keys()))
  
  while (src[1]==dst[1])&(src[2]==dst[2]):
    dst=random.choice(list(cam.keys()))

P=pkt()    
print(p.src)
print(p.dst)
print(a.ports)

CAM и Port словари сделать глобальными. Возможно инициализировать их в спец классе build
Класс switchport перевести в buffer, новый класс switcport  имеет два атрибута, равные экземплярам класса buffer
Сделать класс switch, который соответственно будет сопоставлять порт входа.in с портом выхода.out:
Class params:
PORTS=10
RATE=
BUF=
DISTRIB

Class clients:
Def init(self, num, ports) 
Num, ports - равноразмерные списки

Class switchport(rate, bufsize):
Self.in=None #буфер приходящих извне пакетов
Self.out=None #буфер уходящих с коммутатора

Class switch:
Def init(self, pkt) 

i=p.cam[pkt.dst]
SwitchPort[i-1].out=pkt
#мб добавить маааленькую рандомную задержку


Вообще порядок:
Опред кво портов и их парам(с б) 
Опред кво клиентов и их парам(ид) 
Подсоединить клиентов к портам
Составить таблицы 
Инициализировать коммутатор, передав ему таблицы

Надо бы сделать так, чтобы в один момент пакеты отправляло опред число клиентов. 
В pgen для каждого клиента дать свое распределение времени отправки
