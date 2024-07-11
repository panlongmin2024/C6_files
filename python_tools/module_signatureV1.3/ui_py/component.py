from datetime import datetime

from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import (QPlainTextEdit, QLineEdit, QLabel, QWidget, QHBoxLayout,
                             QPushButton, QApplication, QMessageBox)


class TestLog(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.log_times = 0

    def append_log(self, msg: str):
        self.appendPlainText(
            '[' + datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')[:-3] + '] ' + msg)
        print(msg)

    def create_log(self, product_sn):
        # self.log_times += 1
        # if self.log_times >= 500:
        # 创建log文件
        log_file: str = ('./log/' + product_sn + '_' +
                         datetime.now().strftime('%Y-%m-%d_%H-%M-%S.%f')[:-3] + '.txt')
        # log_file: str = ('./log/'+ '_' +datetime.now().strftime('%Y-%m-%d-%H:%M:%S.%f')[:-3] + '.txt')
        with open(log_file, mode='w', encoding='utf-8') as file:
            file.write(self.toPlainText())
            file.close()
        # self.log_times = 0
        # self.clear_log()

    def clear_log(self):
        self.clear()
        self.verticalScrollBar().setValue(0)

    def set_max_bar(self):
        self.verticalScrollBar().setValue(self.log.verticalScrollBar().maximum())


class SNLinedit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

    def end_test(self):
        self.setEnabled(True)
        self.clear()
        self.setFocus()


class TestState(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.set_font()

    def set_font(self):
        font: QFont = QFont()
        font.setWeight(600)
        font.setPointSize(18)
        self.setMinimumSize(QSize(250, 42))
        self.setFont(font)

    def test_end(self, pass_or_fail):
        if pass_or_fail == "PASS":
            self.setStyleSheet(
                "background-color:green;border:1px solid black;")
        else:
            self.setStyleSheet(
                "background-color:#ff3300;border:1px solid black;")


class StatisticsWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.test_num1: int = 0
        self.pass_num1: int = 0
        self.test_label = QLabel('测试数：')
        self.pass_label = QLabel('通过数：')
        self.rate_label = QLabel('通过率：')
        self.pass_num = QLabel('0')
        self.pass_num.setObjectName('pass_num')
        self.test_num = QLabel(self)
        self.test_num.setObjectName('test_num')
        self.passing_rate = QLabel(self)
        self.passing_rate.setObjectName('passing_rate')
        self.resect = QPushButton(self)
        self.resect.setText('重置')
        self.h_layout = QHBoxLayout(self)
        self.h_layout.addWidget(self.test_label)
        self.h_layout.addWidget(self.test_num)
        self.h_layout.addWidget(self.pass_label)
        self.h_layout.addWidget(self.pass_num)
        self.h_layout.addWidget(self.rate_label)
        self.h_layout.addWidget(self.passing_rate)
        self.h_layout.addWidget(self.resect)
        self.setLayout(self.h_layout)
        self.label_list: list[QLabel] = [
            self.passing_rate, self.pass_num, self.test_num]
        self.set_line(40)
        self.set_font()
        self.resect.clicked.connect(self.resect_num)

    def set_line(self, width):
        for label in self.label_list:
            label.setMinimumWidth(width)
            # label.setMaximumWidth(width)
            label.setAlignment(Qt.AlignCenter)
        self.passing_rate.setMinimumWidth(65)

    def set_font(self):
        font1 = QFont()
        font1.setFamily(u"Microsoft New Tai Lue")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setWeight(50)
        self.setFont(font1)

    def resect_num(self):
        reply = QMessageBox.question(self, 'Message', '确认重置?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            for label in self.label_list:
                label.setText('0')
            self.passing_rate.setText('0%')
            self.test_num1 = 0
            self.pass_num1 = 0

    def handle_result(self, result):
        self.test_num1 += 1
        self.test_num.setText(str(self.test_num1))
        if result == 'PASS':
            self.pass_num1 += 1
            self.pass_num.setText(str(self.pass_num1))
        percentage = self.calculate_percentage(self.pass_num1, self.test_num1)
        self.passing_rate.setText(f"{percentage:.1f}%")

    @staticmethod
    def calculate_percentage(partial, total):
        return (partial / total) * 100

# if __name__ == '__main__':
#     app = QApplication([])
#     widg = StatisticsWidget()
#     widg.show()
#     app.exec_()
