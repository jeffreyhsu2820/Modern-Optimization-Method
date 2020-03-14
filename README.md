# Modern_Optimization_Method
 This is a pracitce of the hw--SA
 
 ## Following are the example condition
 k1,k2=1,1             #將風險跟利潤看唯一樣重要
population=6          #初始pool的個數
var_num=3             #有幾個變數
# target_function=    向上面定的一樣
# constraint=         向上面定的一樣
scope=430             #變數值的範圍可以從0到幾
R=[-6,6]              #設定尋找的範圍
boltzmann_constant=1  #設定波茲曼常數
c=0.5                 #設定temperaturereductionfactor
iteration=2           #要跌代幾次
converge_criteria=500 #連續幾次都是同一個point
 ### Inputs of the equation.
def target_function(x):   #we change maximize into minimize problem
    return 1/(1+500*x[0]+300*x[1]+200*x[2]+math.sqrt(22500*(x[0]**2)+ 10000*(x[1]**2)+ 2500*(x[2]**2)))
def constraint(x):
    y1=4*x[0]+ 4*x[1]+ 8*x[2]-1720+1.645*(math.sqrt(16*(x[0]**2)+(x[1]**2)+ 9*(x[2]**2)+ 29584))
    y2=4*x[1]+ 16*x[2]-1680+1.645*math.sqrt(4*(x[1]**2)+ 16*(x[2]**2)+ 112896)
    y3=8*x[0]+ 12*x[1]-1840+1.645*math.sqrt(4*(x[0]**2)+ 4*(x[1]**2)+ 76176)
    return y1, y2, y3
