from PyQt5 import QtWidgets , QtCore
from views import goal_view
import json
import requests
import os
class Goal_Manager(QtWidgets.QWidget, goal_view.Ui_Form):
    loginAcceptedSignal = QtCore.pyqtSignal()
    def __init__(self):
        super(Goal_Manager, self).__init__()
        self.setupUi(self)

        # self.login_btn.clicked.connect(self.handle_login)
        # self.base_url = "https://saied.pythonanywhere.com/login/"
        # self.userToken = ''


        self.loginAcceptedSignal.emit()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = Goal_Manager()
    w.show()
    # app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    app.exec_()