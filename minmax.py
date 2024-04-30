MAX,MIN=1000,-1000

def minmax(node,depth,isMaximizingPlayer,values,alpha,beta):
  if depth==3:
    return values[node]
  if isMaximizingPlayer:
    best=MIN
    for i in range(0,2):
      val=minmax(node * 2 + i,depth+1,False,values,alpha,beta)
      best=max(best,val)
      alpha=max(alpha,best)
      if beta <= alpha:
        break
    return best
  else:
    best= MAX
    for i in range(0,2):
      val=minmax(node*2+i,depth+1,True,values,alpha,beta)
      best=min(best,val)
      beta=min(beta,best)
      if beta <= alpha:
        break
    return best
values=[1,2,5,7,0,1,6,4]
print("The optimal value is :",minmax(0,0,True,values,MIN,MAX))
