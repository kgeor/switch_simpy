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

a=pkt()    
print(a.src)
print(a.dst)
print(a.ports)
  
