import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
import seaborn as sns

def Phase_detection(Incl):
    'Crop massive'
    print('Выбор крайних точек сигнала')
    plt.plot(Incl[:, 3:6])
    th = plt.ginput(2)
    plt.close()

    x_th = [0, 0]
    x_th[0] = int(th[0][0])
    x_th[1] = int(th[1][0])

    'Create variables'
    acc = Incl[x_th[0]:x_th[1], 0:3]
    ang_vel = Incl[x_th[0]:x_th[1], 3:6]
    ang = Incl[x_th[0]:x_th[1], 6:9]
    mag = Incl[x_th[0]:x_th[1], 9:12]
    qatern = Incl[x_th[0]:x_th[1], 16:20]

    # Определение начала 1й 5й фаз
    'Выделение плато из ang_v_x'''
    '''scipy.signal.find_peaks(x, height=None, 
    threshold=None, distance=None, prominence=None, width=None, wlen=None, rel_height=0.5, plateau_size=None)[source]'''
    print('Определение начала 1 и 5 фаз')
    dx = 20
    a = ang_vel[:, 0]
    p = (abs(a) < dx) * 1
    p[0] = 1
    p[-1] = 1
    p[1] = 1
    p[-2] = 1
    # plt.plot(p)
    Sum = 0
    for i in range(2, len(p) - 2):
        Sum = p[i] + p[i - 1] + p[i + 1] + p[i + 2] + p[i - 2]
        if Sum < 3:
            p[i] = 0
        else:
            p[i] = 1

    # plt.plot(p)
    # plt.show()

    [p1, p1y] = find_peaks(-np.diff(p), height=0.5, distance=10)
    [p5, p5y] = find_peaks(np.diff(p), height=0.5, distance=10)

    p5 = p5 + 1

    plt.plot(a)
    plt.plot(p1, p1y["peak_heights"], 'bo')
    plt.plot(p5, p5y["peak_heights"], 'ro')
    plt.show()

    # Определение начала 2 фазы

    aa = ang[:, 0]
    print('Определение начала 2 фазы')
    while True:
        H = float(input('def 20\n') or '20')
        D = float(input('def 25\n') or '25')
        [p2, p2y] = find_peaks(aa, height=H, distance=D)  # or -np.diff(a)
        plt.plot(aa)
        plt.plot(p2, p2y["peak_heights"], 'bo')
        plt.show()
        ans = input('If good print 1 \n')
        if ans == '1':
            break

    # Определение начала 3 фазы
    print('Определение начала 3 фазы')
    H = 20
    D = 25
    [p3, p3y] = find_peaks((-a), height=H, distance=D)
    plt.plot(a)
    plt.plot(p3, -p3y["peak_heights"], 'bo')
    plt.show()

    # Определение начала 4 фазы
    print('Определение начала 4 фазы')
    ab = acc[:, 2] - acc[0, 2]
    H = 0.1
    D = 25
    [p4, p4y] = find_peaks(-ab, height=H, distance=D)
    plt.plot(ab)
    plt.plot(p4, -p4y["peak_heights"], 'bo')
    plt.show()

    '''
    plt.plot(a)
    plt.plot(p1,p1y["peak_heights"]*0,'o')
    plt.plot(p2,p2y["peak_heights"]*0,'*')
    plt.plot(p3,-p3y["peak_heights"]*0,'*')
    plt.plot(p4,-p4y["peak_heights"]*0,'o')
    plt.plot(p5,-p5y["peak_heights"]*0,'o')
    plt.show()
    '''

    # Построение гистограмм фаз
    step_time = np.zeros((len(p1) - 1))
    phase_time = np.zeros((5, len(p1)))

    for i in range(0, len(p1) - 1):
        step_time[i] = p1[i + 1] - p1[i]
        phase_time[4, i] = p1[i + 1] - p5[i]

    for i in range(0, len(p1)):
        phase_time[0, i] = p2[i] - p1[i]
        phase_time[1, i] = p3[i] - p2[i]
        phase_time[2, i] = p4[i] - p3[i]
        phase_time[3, i] = p5[i] - p4[i]

    plt.figure(figsize=(10, 8))
    plt.subplot(231)
    sns.distplot(step_time / 20, bins=20, kde=False, rug=True, label='Step_time')
    plt.title('Step_time')

    plt.subplot(232)
    sns.distplot(phase_time[0, :] / 20, bins=20, kde=False, rug=True, label='Phase1')
    plt.title('Phase1')

    plt.subplot(233)
    sns.distplot(phase_time[1, :] / 20, bins=20, kde=False, rug=True, label='Phase2')
    plt.title('Phase2')

    plt.subplot(234)
    sns.distplot(phase_time[2, :] / 20, bins=20, kde=False, rug=True, label='Phase3')
    plt.title('Phase3')

    plt.subplot(235)
    sns.distplot(phase_time[3, :] / 20, bins=20, kde=False, rug=True, label='Phase4')
    plt.title('Phase4')

    plt.subplot(236)
    sns.distplot(phase_time[4, :] / 20, bins=20, kde=False, rug=True, label='Phase5')
    plt.title('Phase5')
    plt.savefig("hist.png", dpi=150)
    plt.show()

    for i in range(0, len(p1) - 1):
        plt.plot(a[p1[i]:p1[i + 1]])
    plt.show()
    return p1,p1y,p2,p2y,p3,p3y,p4,p4y,p5,p5y,phase_time,step_time