# 此程式的日期列索引已經轉到欄位去了  而且日期變成了字串格式
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf

df = yf.download("SI=F", period="6mo")
# df.index = df.index.astype(str)
# df = df.reset_index()
df.info()

日期 = df.index
收盤價 = df['Close']

import matplotlib
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rc('font', family='Microsoft JhengHei')

_fig = plt.gcf()
_axes = plt.gca()

_fig.set_facecolor((255/255,219/255,172/255))
_fig.set_figheight(7)
_fig.set_figwidth(14)
_fig.set_layout_engine(layout='tight')  # 'constrained', 'compressed', 'tight', 'none'
_axes.set_facecolor(((241/255,194/255,125/255)))

# _xticks = [ n for n in range(0,len(日期),10) ]
# _labels = [ 日期[n][5:] for n in _xticks]

plt.title("白銀股價折線圖", **{'fontsize':18})
plt.plot(日期,收盤價,**{'color':(0,0,1),
                            'linewidth':2.0,
                            'marker':'o',
                            'markerfacecolor':(1,0,0)
                           })
# plt.xticks(ticks=_xticks,labels=_labels,**{'rotation':20})
plt.xlabel("日期", **{'fontsize':12,'rotation':0})
plt.ylabel("收盤價(美元)", **{'fontsize':12})
plt.grid(visible=True,axis='y',**{'linestyle':'--'})
plt.show()