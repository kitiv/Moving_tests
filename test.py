from Phase_detection import *
from split_func import *
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

L = 20  # Distance
H = 180 / 250  # Growth
A = 24  # Age
S = 1  # Sex
W = 84 / 200  # Weigth
id = 'M00001'
dis = 'C:\\Users\\Александр\\Documents\\GitHub\\Moving_tests\\WT901WIFI\\WT901WIFI\\WIFI software-UDP mode pairing network\\data\\20200427'
name = dis + '\\22.log'
[NofS, lNofS] = split_func(name)  # Разделение массива [Номера датчиков по порядку массива, кол-во датчиков]
Incl = np.genfromtxt(name, delimiter=',')[:, 2:26]  # [0:-1:lNofS, 2:26]
# Incl2=Incl[[i for i, ltr in enumerate(NofS) if ltr == "WT4700001010"],5]
# x = [i for i, ltr in enumerate(NofS) if ltr == "WT4700000973"]
'Crop massive'
print('Выбор крайних точек сигнала')
plt.plot(Incl[:, 3:6])  # Построение угловых скоростей для выбора крайних точек сигнала
th = plt.ginput(2)  # Выбор крайних точек
plt.close()
x_th = [0, 0]  # Коорд крайних точек
x_th[0] = int(th[0][0])
x_th[1] = int(th[1][0])
Incl1 = Incl[x_th[0]:x_th[1], :]  # Обрезание данных с датчика по крайним точкам
NofS1 = NofS[x_th[0]:x_th[1]]  # Обрезание массива имен датчиков по крайним точкам
d_name = list(set(NofS1))  # выделение уникальных имен датчиков
print('Используемые датчики: ', d_name)
# sens_names={'W0038':'1 или Left_arm'}
# name_sen=sens_name[str(NofS(0))] -> 'Left_arm'
for i in d_name:  # Цикл по датчикам
    Incl2 = Incl1[[j for j, ltr in enumerate(NofS1) if ltr == i],
            :]  # Выделение строк относящ к опред датчику из общего массива
    [p1, p1y, p2, p2y, p3, p3y, p4, p4y, p5, p5y, phase_time, step_time, NFog, TF] = Phase_detection(
        Incl2)  # Функция расчета фаз шага
    d = {'p1': p1, 'p1y': p1y["peak_heights"],
         'p2': p2, 'p2y': p2y["peak_heights"],
         'p3': p3, 'p3y': p3y["peak_heights"],
         'p4': p4, 'p4y': p4y["peak_heights"],
         'p5': p5, 'p5y': p5y["peak_heights"]}  # Массив фаз
    print(d)
    d2 = phase_time.transpose()
    frame = pd.DataFrame(d)  # собираем фрейм
    frame1 = pd.DataFrame(d2)
    frame.to_csv(dis + '\\P0S' + i + '_phases.csv', index=False)
    frame1.to_csv(dis + '\\P0S' + i + '_phases_time.csv', mode='w', index=False)

    Nstep = len(p2)
    Twalk = p1[-1] - p1[0]  # Проверить
    GP1 = L / Nstep / H
    GP2 = L / Nstep / Twalk
    # GP3_1=0 # Задумка встроить инеграл от угловой скорости на переносе ноги, чтобы вычилить макс поднятие
    GP3_2 = np.mean(p3y)
    [GP4, GP5, GP6, GP7, GP8, GP9, GP10, GP11] = [np.mean(phase_time[0, :]), np.mean(phase_time[1, :]),
                                                  np.mean(phase_time[2, :]),
                                                  np.mean(phase_time[3, :]), np.std(phase_time[0, :]),
                                                  np.std(phase_time[1, :]),
                                                  np.std(phase_time[2, :]), np.std(phase_time[3, :])]
    GP12_1 = NFog  # встроить по точкам определение N_FOG
    GP12_2 = np.mean(TF)  # встроить по точкам определение T_средн_FOG

    Out_mass = {'Growth': H, 'Sex': S, 'Age': A, 'Weight': W, 'GP1': GP1, 'GP2': GP2, 'GP3.2': GP3_2, 'GP4': GP4,
                'GP5': GP5, 'GP6': GP6, 'GP7': GP7, 'GP8': GP8, 'GP1': GP9, 'GP1': GP9, 'GP1': GP10, 'GP11': GP11,
                'GP12.1': GP12_1, 'GP12.2': GP12_2}  # Массив выходных параметров
    out_frame = pd.DataFrame(Out_mass)
    out_frame.to_csv(id + '.csv', index=False)
