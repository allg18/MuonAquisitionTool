# -*- coding: utf-8 -*-
"""
Various methods of drawing scrolling plots.
"""

import pyqtgraph as pg
# from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import timeit

import time


win = pg.GraphicsWindow()
win.setWindowTitle('pyqtgraph example: Scrolling Plots')


# 1) Simplest approach -- update data in the array such that plot appears to scroll
#    In these examples, the array size is fixed.
# data=[]
# p1 = win.addPlot()
# p2 = win.addPlot()
# curve1 = p1.plot(data1)
# curve2 = p2.plot(data1)
# ptr1 = 0

# def import_data():
# 	data=


#print (timeit.timeit())








# def update1():
#     global data1, curve1, ptr1
#     data1[:-1] = data1[1:]  # shift data in the array one sample left
#                             # (see also: np.roll)
#     data1[-1] = np.random.normal()
#     curve1.setData(data1)
    
#     ptr1 += 1
#     curve2.setData(data1)
#     curve2.setPos(ptr1, 0)
    
# def update():
#     update1()
#     update2()
#     update3()
# timer = pg.QtCore.QTimer()
# timer.timeout.connect(update)
# timer.start(50)



# ## Start Qt event loop unless running in interactive mode or using pyside.
# if __name__ == '__main__':
#     import sys
#     if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
#         QtGui.QApplication.instance().exec_()