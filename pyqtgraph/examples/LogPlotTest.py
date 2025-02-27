# -*- coding: utf-8 -*-
"""
Simple logarithmic plotting test
"""

from pyqtgraph.Qt import QtGui, QtCore
import numpy as np
import pyqtgraph as pg

app = pg.mkQApp("Log Plot Example")

win = pg.GraphicsLayoutWidget(show=True, title="Basic plotting examples")
win.resize(1000,600)
win.setWindowTitle('pyqtgraph example: LogPlotTest')


p5 = win.addPlot(title="Scatter plot, axis labels, log scale")
x = np.random.normal(size=1000) * 1e-5
y = x*1000 + 0.005 * np.random.normal(size=1000)
y -= y.min()-1.0
mask = x > 1e-15
x = x[mask]
y = y[mask]
p5.plot(x, y, pen=None, symbol='t', symbolPen=None, symbolSize=10, symbolBrush=(100, 100, 255, 50))
p5.setLabel('left', "Y Axis", units='A')
p5.setLabel('bottom', "Y Axis", units='s')
p5.setLogMode(x=True, y=False)


if __name__ == '__main__':
    pg.exec()
