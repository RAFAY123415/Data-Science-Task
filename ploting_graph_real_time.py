import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count

frame_len = 30000
fig = plt.figure(figsize=(9, 6))

def animate(self):
    data = pd.read_csv('sentiment.csv')
    y1 = data['bitcoin']
    y2 = data['ethereum']
    print(y1)
    if len(y1) <= frame_len:
        plt.cla()
        plt.plot(y1, label='Bitcoin')
        plt.plot(y2, label='Ethereum')
    else:
        plt.cla()
        plt.plot(y1[-frame_len:], label='Bitcoin')
        plt.plot(y2[-frame_len:], label='Ethereum')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=100)
plt.show()