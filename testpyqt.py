# import sys
# from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QLineEdit
# from PyQt5.QtCore import Qt
#
# # Subclass QMainWindow to customise your application's main window
# class MainWindow(QMainWindow):
#
#     def __init__(self, *args, **kwargs):
#         super(MainWindow, self).__init__(*args, **kwargs)
#
#         self.setWindowTitle("My Awesome App")
#         # Text field
#         self.lineEntry = QLineEdit(self)
#         self.lineEntry.move(16, 16)
#         self.lineEntry.resize(200, 40)
#
#         label = QLabel("This is a PyQt5 window!")
#
#         # The `Qt` namespace has a lot of attributes to customise
#         # widgets. See: http://doc.qt.io/qt-5/qt.html
#         label.setAlignment(Qt.AlignCenter)
#
#         # Set the central widget of the Window. Widget will expand
#         # to take up all the space in the window by default.
#         self.setCentralWidget(label)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
#
# app.exec_()
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import Qt
import webbrowser, sys


class App(QWidget):

    def __init__(self):
        super().__init__()
        QWidget.__init__(self, None, Qt.WindowStaysOnTopHint)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.title = 'Drop to search'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 60
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: #2B2D42")

        # editBox = QLineEdit('Drag this', self)
        # editBox.setDragEnabled(True)
        # editBox.move(10, 10)
        # editBox.resize(100, 32)
        exitButton = QPushButton("X",self)
        exitButton.setStyleSheet("background-color : #EF233C; "
                                 "color: #EDF2F4;"
                                 "font: bold 12px;"
                                 "border-style: outset;")
        exitButton.move(300,0)
        exitButton.resize(19, 15)
        #exitButton.resize(exitButton.sizeHint())


        exitButton.clicked.connect(self.on_click)

        button = CustomLabel('Drop here', self)
        button.move(0, -5)
        button.resize(150, 70)
        button.setStyleSheet("background-color: #8D99AE; "
                             "color: #EDF2F4;"
                             "font: bold 12px;")
        button.setAlignment(Qt.AlignCenter)

        self.show()

    @pyqtSlot()
    def on_click(self):
        sys.exit()


    # this function allows window to be dragged
    def mousePressEvent(self, event):
        self.offset = event.pos()

    # this function allows window to be dragged
    def mouseMoveEvent(self, event):
        x = event.globalX()
        y = event.globalY()
        x_w = self.offset.x()
        y_w = self.offset.y()
        self.move(x - x_w, y - y_w)

# Manages what happens if anything is dropped to CustomLabel
# contains dropEvent() for searching in browsers
class CustomLabel(QLabel):

    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, e):
        if e.mimeData().hasFormat('text/plain'):
            e.accept()
        else:
            e.ignore()

    def dropEvent(self, e):
        query = e.mimeData().text()

        if query:
            query = query.replace(' ', '+')
            query = 'https://duckduckgo.com/?t=ffab&q=' + query
            webbrowser.open(query, new=2)
        elif sys.argv[1]:
            query = sys.argv[1]
            query = query.replace(' ', '+')
            query = 'https://duckduckgo.com/?t=ffab&q=' + query
            webbrowser.open(query, new=2)
        else:
            self.setText('Enter query')

        self.setText(e.mimeData().text())

# runs app
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

# https://pythonbasics.org/pyqt-buttons/
# https://pythonbasics.org/qlineedit/   https://pythonspot.com/pyqt5-drag-and-drop/
# https://stackoverflow.com/questions/1925015/pyqt-always-on-top