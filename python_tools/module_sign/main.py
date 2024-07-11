import gc
import socket
import tracemalloc
from PyQt5 import QtGui, QtCore
from module.write_read_json import RWJson
from ui_py.set_ui import Ui_Dialog
from ui_py.main_window_ui import *
from module.get_set_control_value import *
from module.post_data import *
from module.test_interface import *
from module.serial_method import *
# from module.create_hash import *
# from module.create_uuid import *
from module.create_write_check_key import *

class SetFont(QDialog):
    send_value_signal = pyqtSignal(dict)
    save_signal = pyqtSignal(dict)

    def __init__(self, parent=None):
        super(SetFont, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        upload_icon = QIcon('./icon/upload.svg')
        self.setWindowIcon(upload_icon)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.config_data = RWJson.read_json('./configs/config_data.json')
        self.ui.confirm.clicked.connect(self.save_control_value)
        self.ui.resect.clicked.connect(self.clear_all)
        self.setWindowTitle('上传设置')

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        set_control_value(self, self.config_data)
        self.ui.port.addItems(get_port_list())

    def send_control_value(self) -> None:
        control_values: dict = get_control_value(self, self.config_data)
        self.send_value_signal.emit(control_values)

    def save_control_value(self) -> None:
        control_values: dict = get_control_value(self, self.config_data)
        RWJson.write_json('./configs/config_data.json', control_values)
        self.save_signal.emit(control_values)

    def clear_all(self) -> None:
        control = self.findChildren(QLineEdit)
        for i in control:
            i.clear()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        gc.enable()
        tracemalloc.start()
        self.ui: Ui_MainWindow = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Get uuid_cert')
        self.is_mes_dict: dict = RWJson.read_json('./configs/is_mes.json')
        self.token: str = ''
        self.config_data: dict = RWJson.read_json('./configs/config_data.json')
        self.setting_font = SetFont()
        self.setting_font.save_signal.connect(
            lambda config_data: self.refresh_upload_config(config_data))
        self.state_thread: StateThread = StateThread(self)
        self.state_thread.change_text_signal.connect(
            lambda text: self.ui.test_state.setText(text))
        self.test_thread: TestThread = TestThread()
        self.test_thread.test_end_signal.connect(self.test_end_handel)
        self.test_thread.msg_signal.connect(self.ui.log.append_log)
        self.ui.sn.returnPressed.connect(self.start_test)
        self.ui.setting.clicked.connect(self.try_show)
        self.ui.stop.clicked.connect(self.stop_test)
        self.get_permit()

    def try_show(self):
        try:
            self.setting_font.show()
        except Exception as e:
            print(e)

    def get_permit(self) -> None:
        response = PostTestData().post_permit(post_data=self.config_data)
        response_json = response.json()
        if response.status_code == 200:
            self.token = response_json['access_token']
            self.ui.log.append_log('token获取成功')
            self.setting_font.close()
        else:
            self.ui.log.append_log(response_json)
            QMessageBox.critical(self.setting_font, '错误', 'token获取失败')

    def request_handle(self, request_method):
        try:
            request_method()
        except:
            self.ui.log.append_log(traceback.print_exc())

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        set_control_value(self, self.is_mes_dict)
        set_control_value(self.ui.num_widget, self.is_mes_dict)
        self.set_font()
        self.set_icon()
        self.ui.test_state.setAlignment(Qt.AlignCenter)

    def start_test(self):
        try:
            self.ui.test_state.setStyleSheet(u"background-color:#FF9900;\n"
                                             "border:1px solid black;")
            self.state_thread.is_continue = True
            self.ui.log.clear_log()
            self.test_thread.sn = self.ui.sn.text()
            self.test_thread.config_data = self.config_data
            self.test_thread.token = self.token
            self.test_thread.is_mes = self.ui.is_mes.isChecked()
            self.state_thread.start()
            self.test_thread.start()

        except Exception as e:
            self.ui.log.append_log(str(e))

    def set_font(self):
        font: QFont = QFont()
        font.setWeight(600)
        font.setPointSize(18)
        self.ui.test_state.setMinimumSize(QSize(250, 42))
        self.ui.test_state.setFont(font)

    def quit_test_thread(self):
        if self.test_thread.isRunning() is True:
            self.test_thread.terminate()

    def quit_state_thread(self):
        if self.state_thread.isRunning() is True:
            self.state_thread.is_continue = False
            self.state_thread.terminate()
            return "quit"
        else:
            return ""

    def stop_test(self):
        if self.quit_state_thread() == "quit":
            self.ui.test_state.setStyleSheet(
                "background-color:#ff3300;border:1px solid black;")
            self.ui.test_state.setText("Stop testing")
        self.quit_test_thread()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.quit_test_thread()
        self.quit_state_thread()
        control_values: dict = get_control_value(self, self.is_mes_dict)

        RWJson.write_json('./configs/is_mes.json', control_values)

    def set_icon(self):
        window_icon = QIcon('./icon/上位机.ico')
        self.setWindowIcon(window_icon)
        setting_icon = QIcon('./icon/setting.svg')
        self.ui.setting.setIcon(setting_icon)
        stop_icon = QIcon('./icon/stop.svg')
        self.ui.stop.setIcon(stop_icon)

    def refresh_upload_config(self, config_data):
        self.config_data = config_data
        self.request_handle(self.get_permit)

    def test_end_handel(self, state: str, pass_or_fail: str, message: str):
        self.quit_state_thread()
        self.ui.test_state.setText(state)
        self.ui.log.append_log(message)
        self.ui.log.create_log(self.ui.sn.text())
        if pass_or_fail == "PASS":
            self.ui.test_state.setStyleSheet(
                "background-color:green;border:1px solid black;")

        else:
            self.ui.test_state.setStyleSheet(
                "background-color:#ff3300;border:1px solid black;")
        self.ui.num_widget.handle_result(pass_or_fail)
        self.clear_trash()


    def clear_trash(self):
        gc.collect()  # 手动回收垃圾
        current_mem, peak_mem = tracemalloc.get_traced_memory()
        self.ui.log.append_log(f"released, Current memory usage is {current_mem / 10 ** 6}MB " +
                               f"Peak was {peak_mem / 10 ** 6}MB")
        self.ui.log.append_log(
            '======================================================================')


class StateThread(QThread):
    change_text_signal: pyqtSignal = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.is_continue: bool = False
        self.text_list: list = ['Testing   ',
                                'Testing.  ', 'Testing.. ', 'Testing...']

    def run(self):
        index: int = 0
        while self.is_continue is True:
            self.change_text_signal.emit(self.text_list[index])
            self.msleep(100)
            index = 0 if index >= 3 else index + 1


class TestThread(ThreadInterface):
    test_end_signal: pyqtSignal = pyqtSignal(str, str, str)
    msg_signal: pyqtSignal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.file_path: str = 'uuid.txt'
        self.server_url: str = ''
        self.out_put_path: str = './uuid_cert/uuid_cert.bin'
        self.is_mes: bool = False
        self.config_data: dict = {}
        self.sn_data: str = ''
        self.token = ''
        self.hash_string = ''
        self.ip = socket.gethostbyname(socket.gethostname())
        # self.ip = os.popen('hostname -I').readline().replace('\\n', '')
        self.uuid_str = ''

    def run(self):
        self.test_container(self.test_main)

    def test_container(self, func):
        try:
            self.msleep(int(self.config_data['delay'] * 1000))
            self.msleep(5)
            if self.config_data['sn_length'] == len(self.sn):  # 如果sn长度相同
                self.msg_signal.emit('发送过站请求: ')
                pass_result, msg = self.pass_station()  # 过站检查
                if pass_result is True:  # 如果检查通过
                    self.msg_signal.emit('过站成功')
                    self.msg_signal.emit('开始测试')
                    test_result, test_data, test_msg = func()
                    if test_result is True:  # 测试通过
                        self.msg_signal.emit('测试通过')
                        if self.is_mes is True:  # 如果mes上传为真
                            self.msg_signal.emit('开始上传结果')
                            http_result, msg = self.send_result(test_data)  # 结果上传
                            self.msg_signal.emit('生成excel')
                            self.create_excel("PASS", '')  # 生成excel
                            if http_result is True:  # 如果上传成功
                                self.msg_signal.emit('上传成功')
                                self.test_end_signal.emit("PASS", "PASS", msg)
                            else:  # 上传失败
                                self.msg_signal.emit('上传,上传失败')
                                self.test_end_signal.emit("FAIL", "FAIL", msg)
                        else:  # mes上传为假
                            self.create_excel("PASS", test_msg)
                            self.test_end_signal.emit("PASS", "PASS", "")
                    else:  # 测试不通过
                        try:
                            with open('./excel_files/' + str(date.today()) + '.xlsx', "r") as file:
                                pass
                            self.create_excel("PASS", 'str(e)')
                            self.test_end_signal.emit("FAIL", "FAIL", test_msg)
                        except IOError:
                            self.test_end_signal.emit(
                                "FAIL", "FAIL", "EXCEL文件未关闭")
                else:  # 检查不通过
                    self.test_end_signal.emit("FAIL", "FAIL", msg)
            else:  # 如果sn长度不同
                self.test_end_signal.emit("sn长度不符", "FAIL", "")
        except Exception as e:
            self.create_excel("PASS", str(e))
            self.test_end_signal.emit("FAIL", "FAIL", str(e))

    def test_main(self):
        file_path = './uuid/uuid.txt'
        out_put_path = './key/key.bin'
        uuid_string = create_uuid_file(file_path)
        # uuid_string = '40da9cf28aaf4b7ebaa8359c75946c3f'
        if get_file_size(file_path) == 32:
            self.msg_signal.emit("uuid_string: " + uuid_string)
            hash_value = get_sha256_hash(file_path)
            # hash_value = '9267FCFCF1B2FEFB5BBA658E478D455584E42325'
            signature, msg = send_file_for_signing(
                self.config_data['pi_url'], hash_value, self.msg_signal)
            if signature is not None:
                sign_file(signature, out_put_path)
                self.msg_signal.emit("key文件生成成功")
                return True, [{"uuid": uuid_string, "hash": hash_value, "key": str(signature)}], ''

            return False, [{"uuid": uuid_string, "hash": hash_value, "key": ""}], msg
        return False, [{"uuid": uuid_string, "hash": "", "key": ""}], "uuid文件大小不是32个字节"


app = QApplication([])
main_window: MainWindow = MainWindow()
main_window.show()
app.exec_()
