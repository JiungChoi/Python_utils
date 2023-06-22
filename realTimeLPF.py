from matplotlib.figure import figaspect
import numpy as np
import math, random, time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

SCOPE = 10 #볼 데이터 수  최근 n개까지만 봄
FPS = 1 # 애니메이션 초당 프레임 수
CUT_OFF_FREQUENCY = 2 # 컷오프주파수
TS = 0.1 #주기

class LowPassFilter(object):
    def __init__(self, cut_off_freqency, ts):
        
        self.ts = ts
        self.cut_off_freqency = cut_off_freqency
        self.tau = self.get_tau()

        self.prev_data = 0.
        
    def get_tau(self):
        return 1 / (2 * np.pi * self.cut_off_freqency)

    def filter(self, data):
        val = (self.ts * data + self.tau * self.prev_data) / (self.tau + self.ts)
        self.prev_data = val
        return val
    

# 빨간색 스캐터 점 그래프 : 원본데이터
# 파란색 꺾은선 선 그래프 : 필터처리 후 데이터
if __name__ == "__main__":
    x, y, y_lpf = [0], [0], [0]

    lpf = LowPassFilter(CUT_OFF_FREQUENCY, TS)

    while(True):
        x.append(x[-1] + 1)
        y.append(math.sin(random.randint(-10, 10) * 0.01 * np.pi))
        y_lpf.append(lpf.filter(y[-1]))


        x = x[-SCOPE:] # 최근 SCOPE개만 봄 
        y = y[-SCOPE:] 

        plt.plot(x, y_lpf)
        plt.scatter(x, y, c="r", s=1)
        plt.show()
        time.sleep(1/FPS)
        plt.cla()
