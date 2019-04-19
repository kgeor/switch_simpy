from google.colab import drive
drive.mount('/content/drive')
!ls '/content/drive/My Drive/python/modules'
!pip install simpy
import sys
import simpy
import functools
import random
sys.path.append('/content/drive/My Drive/python/modules')
from switchnet import PacketGenerator, PacketSink, SwitchPort

def constArrival():
    return random.random()    # time interval

def constSize():
    return 100.0  # bites


class Switch:
    def __init__(self, env, num, rate, buffer):
      self.num=num #num of ports
      self.env=env
      self.rate=rate
      self.buffer=buffer # size of buffer in bytes
      self.i=0
      self.port=[None]*num
      # generate empty class
      class pt():
          pass
      while self.i < self.num:
        self.prt=pt()
        self.prt.inner=SwitchPort(env, rate, buffer)
        self.prt.outer=SwitchPort(env, rate, buffer)
        self.port[self.i]=self.prt
        self.i+=1
      # все inner должны быть связаны друг с другом  
class PC:
  def __init__(self, env, clientnum, srcport, dstport, time=constArrival, size=constSize, finish=30, flow=10, rec_arrivals=False,  absolute_arrivals=True, rec_waits, debug=True, selector=None ):
    self.env=env
    self.clientnum=clientnum
    self.srcport=srcport
    self.dstport=dstport
    self.time=time
    self.size=size
    self.finish=finish
    self.flow=flow
    self.rec_arrivals=rec_arrivals
    self.absolute_arrivals=absolute_arrivals
    self.rec_waits=rec_waits
    self.debug=debug
    self.selector=selector
    self.server=[None]*random.randint(1, self.clientnum)
    class pc():
      pass
    self.i=0
    while self.i < self.clientnum:
      self.node=pc()
      self.node.gen=PacketGenerator(self.env, self.srcport, self.dstport, self.time, self.size, self.finish, self.flow)
      # коннект к порту-источнику (для каждой пары gen-sink прописать полный путь)
      self.node.sink=PacketSink(self.env, self.rec_arrivals, self.absolute_arrivals, self.rec_waits, self.debug, self.selector)
      self.server[self.i]=node
      self.i+=1
      
class wiring:
  def __init__(self,env,pc,switchport)
  
'''
  def __init__(self, env, num, rate, buffer):
    super().__init__(env, num, rate, buffer)
  def init(self):
    inner=SwitchPort(env, rate, buffer)
    outer=SwitchPort(env, rate, buffer)
'''
num=4
env = simpy.Environment()  # Create the SimPy environment
switch=Switch(env,num,1000,500)
sport=
nodes=PC(env,num,)

ps1 = PacketSink(env, debug=True) # debug: every packet arrival is printed
pg1 = PacketGenerator(env, "first", constArrival, constSize, finish=20, flow_id=10)
pg2 = PacketGenerator(env, "second", constArrival, constSize, finish=20, flow_id=20)
ps2 = PacketSink(env, debug=True)
# Wire packet generators and sinks together
pg1.out = switch.port[0].outer
switch.port[0].outer.out = switch.port[1].inner
switch.port[1].inner.out = ps1

pg2.out = switch.port[1].outer
switch.port[1].outer.out = switch.port[0].inner
switch.port[0].inner.out = ps1
env.run(until=50)

 # debug: every packet arrival is printed

switch_port2 = SwitchPort(env, rate=200.0, qlimit=4800)
# Wire packet generators and sinks together
pg2.out = switch_port2
switch_port2.out = ps2

print("waits: {}".format(ps1.waits))
print("received: {}, dropped {}, sent {}".format(ps1.packets_rec,
     switch_port1.packets_drop, pg1.packets_sent))
print("waits: {}".format(ps2.waits))
print("received: {}, dropped {}, sent {}".format(ps2.packets_rec,
     switch_port2.packets_drop, pg2.packets_sent))