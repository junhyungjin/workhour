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
        self.weekWorkHourChangeBtn.clicked.connect(self.weekWorkHourChangeBtn_clicked)
        self.endWorkAlarmChkBox.stateChanged.connect(self.endWorkAlarmChkBoxState)
        
        
    def endWorkAlarmChkBoxState(self):
        msg = ""
        if self.endWorkAlarmChkBox.isChecked() == True:
            msg = "Alarm 설정되었습니다"
            self.statusBar().showMessage(msg)
        
    def weekWorkHourChangeBtn_clicked(self):
        text, ok = QInputDialog.getText(self, '이번주 근무 시간','근무 시작 시간을 입력하세요 ex) 09:30:00')
        if ok:
            cur_date=datetime.datetime.now()
            self.weekWorkHour = datetime.datetime.strptime(str(cur_date.year) + \
                                              '-'+ str(cur_date.month) +'-'+\
                                              str(cur_date.day) +\
                                              ' '+str(text), '%Y-%m-%d %H:%M:%S')
            self.weekWorkHourLabel.setText(str(self.weekWorkHour))
        
        
    def startWorkTimeBtn_clicked(self):
        cur_date=datetime.datetime.now()
        now = cur_date.strftime('%Y-%m-%d %H:%M:%S')
        self.startWorkTime.setText(now)
        
        if self.weekWorkHour > cur_date:
            lateTime = self.weekWorkHour - cur_date
            addWorkTime = lateTime
            endWorkTime = cur_date + datetime.timedelta(hours=9) - addWorkTime
        else:
            lateTime = cur_date - self.weekWorkHour
            addWorkTime = (lateTime)/2
            endWorkTime = cur_date + datetime.timedelta(hours=9) + addWorkTime
            
        self.addWorkHourLabel.setText(str(addWorkTime))
        self.lateWorkLabel.setText(str(lateTime))
          
        endWorkTimeStr = endWorkTime.strftime('%Y-%m-%d %H:%M:%S')
        self.endWorkTimeLabel.setText(endWorkTimeStr)
        
    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage("현재시간: "+str_time)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()