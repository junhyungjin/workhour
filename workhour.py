#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 13:36:16 2019

@author: hjjun
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from datetime import datetime

form_class = uic.loadUiType("workhour.ui")[0]

class MyWindow(QMainWindow, form_class):  
  
      
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
        self.curTimeBtn.clicked.connect(self.curTimeBtn_clicked)
        self.thisWeekBtn.clicked.connect(self.thisWeekBtn_clicked)
        
    def curTimeBtn_clicked(self):
        cur_time = QTime.currentTime()
        now = cur_time.toString("hh:mm:ss")
        self.startTimeEdit.setText(now)
        
    def thisWeekBtn_clicked(self):
        self.thisWeekTime.getText()
        
        
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()