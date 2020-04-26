from Phase_detection import *
import numpy as np
import pandas as pd
name = 'WT901WIFI\\WIFI software-UDP mode pairing network\\data\\20200402\\18.log'

Incl1 = np.genfromtxt(name, delimiter=',')[:, 2:26]
[p1,p1y,p2,p2y,p3,p3y,p4,p4y,p5,p5y,phase_time,step_time] = Phase_detection(Incl1)
d = {'p1':p1,'p1y':p1y["peak_heights"],
     'p2':p2,'p2y':p2y["peak_heights"],
     'p3':p3,'p3y':p3y["peak_heights"],
     'p4':p4,'p4y':p4y["peak_heights"],
     'p5':p5,'p5y':p5y["peak_heights"]}
d2 = phase_time.transpose()
frame = pd.DataFrame(d) # собираем фрейм
frame1 = pd.DataFrame(d2)
frame.to_csv('C:\\Users\\Александр\\Documents\\GitHub\\Moving_tests\\P0S01_phases.csv',index=False)
frame1.to_csv('C:\\Users\\Александр\\Documents\\GitHub\\Moving_tests\\P0S01_phases_time.csv',index=False)