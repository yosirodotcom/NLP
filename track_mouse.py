from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QTimer, QObject
from PyQt5.QtGui import QCursor

class MouseTracker(QObject):
    def __init__(self):
        super().__init__()
        self.timer = QTimer()
        self.timer.timeout.connect(self.track_mouse)
        self.timer.start(100)  # Update mouse position every 100 milliseconds

    def track_mouse(self):
        cursor = QCursor()
        print(cursor.pos().x(), cursor.pos().y())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    tracker = MouseTracker()
    sys.exit(app.exec_())
