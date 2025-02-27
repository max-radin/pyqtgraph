# -*- coding: utf-8 -*-

"""
Simple use of DataTreeWidget to display a structure of nested dicts, lists, and arrays
"""

import pyqtgraph as pg
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np


# for generating a traceback object to display
def some_func1():
    return some_func2()
def some_func2():
    try:
        raise Exception()
    except:
        import sys
        return sys.exc_info()[2]


app = pg.mkQApp("DataTreeWidget Example")
d = {
    'a list': [1,2,3,4,5,6, {'nested1': 'aaaaa', 'nested2': 'bbbbb'}, "seven"],
    'a dict': {
        'x': 1,
        'y': 2,
        'z': 'three'
    },
    'an array': np.random.randint(10, size=(40,10)),
    'a traceback': some_func1(),
    'a function': some_func1,
    'a class': pg.DataTreeWidget,
}

tree = pg.DataTreeWidget(data=d)
tree.show()
tree.setWindowTitle('pyqtgraph example: DataTreeWidget')
tree.resize(600,600)


if __name__ == '__main__':
    pg.exec()
