from Phase_detection import *
from func import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

name = 'WT901WIFI\\WIFI software-UDP mode pairing network\\data\\20200402\\18.log'
[NofS, lNofS] = split_func(name)
Incl = np.genfromtxt(name, delimiter=',')[:,2:26]  # [0:-1:lNofS, 2:26]

'Crop massive'
print('Выбор крайних точек сигнала')
plt.plot(Incl[:,3:6])
th = plt.ginput(2)
plt.close()
x_th = [0, 0]
x_th[0] = int(th[0][0])
x_th[1] = int(th[1][0])

# sens_names={'W0038':'1 или Left_arm'}
# name_sen=sens_name[str(NofS(0))] -> 'Left_arm'
for i in range(lNofS):
    name_sen = str(NofS[i])
    [p1, p1y, p2, p2y, p3, p3y, p4, p4y, p5, p5y, phase_time, step_time] = Phase_detection(Incl[i:-1:lNofS, :], x_th)
    d = {'p1': p1, 'p1y': p1y["peak_heights"],
         'p2': p2, 'p2y': p2y["peak_heights"],
         'p3': p3, 'p3y': p3y["peak_heights"],
         'p4': p4, 'p4y': p4y["peak_heights"],
         'p5': p5, 'p5y': p5y["peak_heights"]}
    d2 = phase_time.transpose()
    frame = pd.DataFrame(d)  # собираем фрейм
    frame1 = pd.DataFrame(d2)
    frame.to_csv('C:\\Users\\Александр\\Documents\\GitHub\\Moving_tests\\P0S' + name_sen + '_phases.csv', index=False)
    frame1.to_csv('C:\\Users\\Александр\\Documents\\GitHub\\Moving_tests\\P0S' + name_sen + '_phases_time.csv',
                  index=False)
