num,length=map(int, input().split( ))
signal=[input().split() for _ in range(num)]

road=[0]*(length+1)
road[0]=-1
time=0

for i in range(num):
  road[int(signal[i][0])]=i+1

j=1
while j <= length:
  if road[j]==0:
    time+=1
  else:
    index=road[j]-1
    red_light=int(signal[index][1])
    green_light=int(signal[index][2])
    cycle=red_light+green_light
    signal_time=time%cycle

    if signal_time<red_light:
      time+=(red_light-signal_time)
    time+=1
  
  j+=1

print(time-1)
