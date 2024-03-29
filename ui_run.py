import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5.QtGui import QImage, QPixmap, QGuiApplication
from Final_Project_ui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        """
        Constructor of runner

        Returns
        -------
        None.

        """
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        
    def closeEvent(self, event):
        """
        This is the special method which is closeEvent method. When the program closing from the X on the top right of the screen, This method shows a pop up screen and asks do you want to close the program or not.

        Parameters
        ----------
        event : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        self.ui.statusbar.showMessage('Close Event')
        
        reply = QMessageBox.warning(self,'Message',
                "Are you sure to quit?",QMessageBox.Yes |
                QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
            self.ui.statusbar.clearMessage()
            
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

    