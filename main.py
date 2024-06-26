from PyQt5.QtWidgets import QApplication, QMainWindow
from MainWindow import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        """
        Initializes the Main class.

        Sets up the main window by initializing the UI from the MainWindow class.

        Args:
            None
        
        Returns:
            None
        """
        super(Main, self).__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication([])
    window = Main()
    window.show()
    app.exec_()
