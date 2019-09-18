from main import *
import matplotlib.pyplot as plt
import numpy as np
qc = quadbababa()
Kp = 0.1
Ki = 0.01
Kd = 0.009
x1_org = []
y1_org = []
z1_org = []
x1_fix = []
y1_fix = []
z1_fix = []
pos_error = qc.reset() - [0,0,0]    						 #對原點(0,0,0)的誤差
pos_error_sum = 0.0
prepos_error = [0,0,0]
anti_windup = 0						

for x in range(1,2001): 
	pos_error_sum = pos_error_sum + pos_error 				#誤差總和
	Kpwork = Kp * pos_error 						#Proportional
	Kiwork = Ki * pos_error_sum - anti_windup				#Integral
	Kdwork = Kd * (pos_error - prepos_error)				#Derivative
	prepos_error = pos_error 						#Last error

	ouput = np.clip(Kpwork + Kiwork + Kdwork,-0.3,0.3)			#anti_windup	
	anti_windup = Kpwork + Kiwork + Kdwork - ouput 			

	Kiwork = Ki * pos_error_sum - anti_windup				#再對積分器anti一次
	prepos_error = Kpwork + Kiwork + Kdwork

	x1_org.append(pos_error[0])
	y1_org.append(pos_error[1])	
	z1_org.append(pos_error[2])
	
	print(pos_error)	
	pos_error = qc.step(prepos_error)

str1 = '\n'.join([str(x) for x in x1_org])
with open("x1org","w") as f:
     f.write(str1)
# str2 = '\n'.join([str(x) for x in y1_org])
# with open("y1org","w") as f:
#      f.write(str2)
# str3 = '\n'.join([str(x) for x in z1_org])
# with open("z1org","w") as f:
#     f.write(str3)
plt.show()






	
	
