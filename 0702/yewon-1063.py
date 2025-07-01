#switch on/off

switch_num=int(input())
switch=list(map(int, input().split( )))
student_num=int(input())
student=[list(map(int, input().split( ))) for _ in range(student_num)]

for i in range(student_num):
  if student[i][0]==1:
    for j in range(student[i][1]-1,switch_num,student[i][1]):
      if switch[j]==0:
        switch[j]=1
      else:
        switch[j]=0
  elif student[i][0]==2:
    axis=student[i][1]-1
    left=axis-1
    right=axis+1
    while left >=0 and right<switch_num and switch[left]==switch[right]:
      if switch[left]==0:
        switch[left]=1
      else: switch[left]=0

      if switch[right]==0:
        switch[right]=1
      else: switch[right]=0

      left-=1
      right+=1

    if switch[axis]==1:
      switch[axis]=0
    else: switch[axis]=1
  
  else:
    print("exception")

result=' '.join(str(x) for x in switch)
print(result)

