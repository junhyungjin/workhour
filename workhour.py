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
import datetime

form_class = uic.loadUiType("workhour.ui")[0]

class MyWindow(QMainWindow, form_class):    
    
    startWorkHour = 0
    lateWorkHour = 0
    endWorkHour = 0
    
    
      
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        cur_date=datetime.datetime.now()
        self.weekWorkHour = datetime.datetime.strptime(str(cur_date.year) + \
                                              '-'+ str(cur_date.month) +'-'+\
                                              str(cur_date.day) +\
                                              ' 9:00:00', '%Y-%m-%d %H:%M:%S')
        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)
        self.weekWorkHourLabel.setText(str(self.weekWorkHour))
        self.startWorkTimeBtn.clicked.connect(self.startWorkTimeBtn_clicked)
        
    def startWorkTimeBtn_clicked(self):
        cur_date=datetime.datetime.now()
        now = cur_date.strftime('%Y-%m-%d %H:%M:%S')
        self.startWorkTime.setText(now)
        
        if self.weekWorkHour > cur_date:
            lateTime = self.weekWorkHour - cur_date
            addWorkTime = (lateTime)/2
        else:
            lateTime = cur_date - self.weekWorkHour
            addWorkTime = (lateTime)/2
            
        self.addWorkHourLabel.setText(str(addWorkTime))
        self.lateWorkLabel.setText(str(lateTime))
        
        endWorkTime = cur_date + datetime.timedelta(hours=9) + addWorkTime
        endWorkTimeStr = endWorkTime.strftime('%Y-%m-%d %H:%M:%S')
        self.endWorkTimeLabel.setText(endWorkTimeStr)
        
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()