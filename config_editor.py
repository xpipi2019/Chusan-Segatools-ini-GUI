import configparser
import json
import os

from PyQt5.QtCore import Qt,pyqtSignal
from PyQt5.QtWidgets import (
    QCheckBox,
    QComboBox,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

from localization import Localization
from tabs.board_tab import setup_board_tab
from tabs.device_tab import setup_device_tab
from tabs.input_tab import setup_input_tab
from tabs.io_tab import setup_io_tab
from tabs.led_tab import setup_led_tab
from tabs.misc_tab import setup_misc_tab
from tabs.network_tab import setup_network_tab
from tabs.path_tab import setup_path_tab
from tabs.window_tab import setup_window_tab
from utils import create_scrollable_layout


class ConfigEditor(QMainWindow):
    config_loaded = pyqtSignal()
    def __init__(self, language="zh_CN"):
        super().__init__()

        self.version = "0.3"
        self.language = language

        self.setWindowTitle(
            Localization.get_text(self.language, "app_title", self.version)
        )
        self.setGeometry(100, 100, 1050, 700)

        self.config = configparser.ConfigParser()

        self.config.comment_prefixes = (";",)
        self.config.optionxform = str  # 保持键的大小写

        self.original_content = []
        self.current_file = ""

        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout(central_widget)

        lang_layout = QHBoxLayout()
        lang_label = QLabel(Localization.get_text(self.language, "language"))
        self.lang_combo = QComboBox()
        self.lang_combo.addItem(
            Localization.get_text(self.language, "language_zh"), "zh_CN"
        )
        self.lang_combo.addItem(
            Localization.get_text(self.language, "language_en"), "en_US"
        )
        self.lang_combo.currentIndexChanged.connect(self.change_language)

        lang_layout.addWidget(lang_label)
        lang_layout.addWidget(self.lang_combo)
        lang_layout.addStretch()

        main_layout.addLayout(lang_layout)

        self.tab_widget = QTabWidget()
        main_layout.addWidget(self.tab_widget)

        button_layout = QHBoxLayout()

        self.open_button = QPushButton(
            Localization.get_text(self.language, "open_config")
        )
        self.open_button.clicked.connect(self.open_config)
        button_layout.addWidget(self.open_button)

        self.save_button = QPushButton(
            Localization.get_text(self.language, "save_config")
        )
        self.save_button.clicked.connect(self.save_config)
        self.save_button.setEnabled(False)
        button_layout.addWidget(self.save_button)

        main_layout.addLayout(button_layout)

        self.widgets = {}

        index = self.lang_combo.findData(self.language)
        if index >= 0:
            self.lang_combo.setCurrentIndex(index)

    def change_language(self):
        self.language = self.lang_combo.currentData()

        self.setWindowTitle(
            Localization.get_text(self.language, "app_title", self.version)
        )

        self.open_button.setText(Localization.get_text(self.language, "open_config"))
        self.save_button.setText(Localization.get_text(self.language, "save_config"))

        if self.current_file:
            self.create_tabs()

        if os.path.basename:
            self.setWindowTitle(
                f"{Localization.get_text(self.language, 'app_title', self.version)} - segatools.ini"
            )

        self.save_settings()

    def save_settings(self):
        settings = {"language": self.language}
        settings_file = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "settings.json"
        )
        try:
            with open(settings_file, "w", encoding="utf-8") as f:
                json.dump(settings, f)
        except:
            pass  # 忽略保存设置时的错误

    def open_config(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            Localization.get_text(self.language, "open_file_dialog"),
            "",
            "INI文件 (*.ini);;所有文件 (*)",
        )

        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    self.original_content = f.readlines()

                self.config.read(file_path, encoding="utf-8")
                self.current_file = file_path
                self.create_tabs()
                self.save_button.setEnabled(True)
                self.setWindowTitle(
                    f"{Localization.get_text(self.language, 'app_title', self.version)} - {os.path.basename(file_path)}"
                )
            except Exception as e:
                QMessageBox.critical(
                    self,
                    Localization.get_text(self.language, "error"),
                    Localization.get_text(self.language, "cannot_read_config", str(e)),
                )
        self.config_loaded.emit()

    def save_config(self):
        if not self.current_file:
            return

        backup_file = self.current_file + ".bak"
        try:
            if os.path.exists(self.current_file):
                import shutil
                shutil.copy2(self.current_file, backup_file)
        except Exception as e:
            QMessageBox.warning(
                self,
                Localization.get_text(self.language, "backup_error_title"),
                Localization.get_text(self.language, "backup_error_msg").format(str(e)),
            )

        self.update_config_from_widgets()

        try:
            with open(self.current_file, "w", encoding="utf-8") as f:
                # 如果有原始内容，尝试保留注释
                if self.original_content:
                    new_content = []
                    processed_sections = set()
                    section = None

                    for line in self.original_content:
                        line = line.rstrip()

                        if line.startswith("[") and line.endswith("]"):
                            section = line[1:-1]
                            new_content.append(line)
                            processed_sections.add(section)

                            if section in self.config:
                                for key, value in self.config[section].items():
                                    new_content.append(f"{key}={value}")

                        # 如果不是节标题也不是键值对，保留原始行（注释等）
                        elif not ("=" in line and not line.lstrip().startswith(";")):
                            new_content.append(line)
                    
                    # 添加未处理的节
                    for section in self.config.sections():
                        if section not in processed_sections:
                            new_content.append("")  # 添加空行分隔
                            new_content.append(f"[{section}]")
                            for key, value in self.config[section].items():
                                new_content.append(f"{key}={value}")

                    f.write("\n".join(new_content))
                else:
                    self.config.write(f)

            QMessageBox.information(
                self,
                Localization.get_text(self.language, "save_success_title"),
                Localization.get_text(self.language, "save_success_msg").format(
                    self.current_file
                ),
            )
        except Exception as e:
            QMessageBox.critical(
                self,
                Localization.get_text(self.language, "save_error_title"),
                Localization.get_text(self.language, "save_error_msg").format(str(e)),
            )

    def create_tabs(self):
        self.tab_widget.clear()
        self.widgets = {}

        path_tab = QWidget()
        device_tab = QWidget()
        network_tab = QWidget()
        board_tab = QWidget()
        window_tab = QWidget()
        led_tab = QWidget()
        io_tab = QWidget()
        input_tab = QWidget()
        misc_tab = QWidget()

        self.tab_widget.addTab(
            path_tab, Localization.get_text(self.language, "tab_path")
        )
        self.tab_widget.addTab(
            device_tab, Localization.get_text(self.language, "tab_device")
        )
        self.tab_widget.addTab(
            network_tab, Localization.get_text(self.language, "tab_network")
        )
        self.tab_widget.addTab(
            board_tab, Localization.get_text(self.language, "tab_board")
        )
        self.tab_widget.addTab(
            window_tab, Localization.get_text(self.language, "tab_window")
        )
        self.tab_widget.addTab(led_tab, Localization.get_text(self.language, "tab_led"))
        self.tab_widget.addTab(io_tab, Localization.get_text(self.language, "tab_io"))
        self.tab_widget.addTab(
            input_tab, Localization.get_text(self.language, "tab_input")
        )
        self.tab_widget.addTab(
            misc_tab, Localization.get_text(self.language, "tab_misc")
        )

        setup_path_tab(self, path_tab)
        setup_device_tab(self, device_tab)
        setup_network_tab(self, network_tab)
        setup_board_tab(self, board_tab)
        setup_window_tab(self, window_tab)
        setup_led_tab(self, led_tab)
        setup_io_tab(self, io_tab)
        setup_input_tab(self, input_tab)
        setup_misc_tab(self, misc_tab)

    def update_config_from_widgets(self):
        if "vfs" not in self.config:
            self.config["vfs"] = {}

        for key, widget in self.widgets.get("vfs", {}).items():
            self.config["vfs"][key] = widget.text()

        if "aime" not in self.config:
            self.config["aime"] = {}

        aime_enable = self.widgets["aime"]["enable"].isChecked()
        self.config["aime"]["enable"] = "1" if aime_enable else "0"

        if aime_enable:
            # 只有启用时才写入路径
            self.config["aime"]["aimePath"] = self.widgets["aime"]["aimePath"].text()
        else:
            if "aimePath" in self.config["aime"]:
                del self.config["aime"]["aimePath"]

        high_baud_widget = self.widgets["aime"]["highBaud"]
        # if not high_baud_widget.property("original_state") == "unmodified":
        self.config["aime"]["highBaud"] = "1" if high_baud_widget.isChecked() else "0"

        if "vfd" not in self.config:
            self.config["vfd"] = {}

        for key, widget in self.widgets.get("vfd", {}).items():
            if isinstance(widget, QCheckBox):
                self.config["vfd"][key] = "1" if widget.isChecked() else "0"
            else:
                self.config["vfd"][key] = widget.text()

        if "dns" not in self.config:
            self.config["dns"] = {}

        selected_dns = None
        for radio, value in self.dns_radios:
            if radio.isChecked():
                if value == "custom":
                    selected_dns = self.custom_dns_edit.text()
                else:
                    selected_dns = value
                break

        if selected_dns:
            self.config["dns"]["default"] = selected_dns

        if "netenv" not in self.config:
            self.config["netenv"] = {}

        for key, widget in self.widgets.get("netenv", {}).items():
            if isinstance(widget, QCheckBox):
                self.config["netenv"][key] = "1" if widget.isChecked() else "0"
            elif isinstance(widget, QSpinBox):
                self.config["netenv"][key] = str(widget.value())
            else:
                self.config["netenv"][key] = widget.text()

        if "keychip" not in self.config:
            self.config["keychip"] = {}

        for key, widget in self.widgets.get("keychip", {}).items():
            self.config["keychip"][key] = widget.text()

        if "system" not in self.config:
            self.config["system"] = {}

        self.config["system"]["enable"] = (
            "1" if self.widgets["system"]["enable"].isChecked() else "0"
        )
        self.config["system"]["freeplay"] = (
            "1" if self.widgets["system"]["freeplay"].isChecked() else "0"
        )

        if self.widgets["system"]["dipsw1_client"].isChecked():
            self.config["system"]["dipsw1"] = "0"
        else:
            self.config["system"]["dipsw1"] = "1"

        dipsw2_combo = self.widgets["system"]["dipsw2"]
        self.config["system"]["dipsw2"] = dipsw2_combo.currentData()

        dipsw3_combo = self.widgets["system"]["dipsw3"]
        self.config["system"]["dipsw3"] = dipsw3_combo.currentData()

        if "gfx" not in self.config:
            self.config["gfx"] = {}

        for key, widget in self.widgets.get("gfx", {}).items():
            if isinstance(widget, QCheckBox):
                self.config["gfx"][key] = "1" if widget.isChecked() else "0"
            elif isinstance(widget, QSpinBox):
                self.config["gfx"][key] = str(widget.value())
            else:
                self.config["gfx"][key] = widget.text()

        if "led15093" in self.widgets:
            if "led15093" not in self.config:
                self.config["led15093"] = {}

            if "enable" in self.widgets["led15093"]:
                self.config["led15093"]["enable"] = (
                    "1" if self.widgets["led15093"]["enable"].isChecked() else "0"
                )

        if "aimeio" not in self.config:
            self.config["aimeio"] = {}

        selected_aimeio = None
        for radio, value in self.aimeio_radios:
            if radio.isChecked():
                if value == "custom":
                    selected_aimeio = self.aimeio_custom_edit.text()
                else:
                    selected_aimeio = value
                break

        if selected_aimeio:
            self.config["aimeio"]["path"] = selected_aimeio

        if "chuniio" not in self.config:
            self.config["chuniio"] = {}

        chuniio_builtin = self.widgets["chuniio"]["builtin"].isChecked()

        if chuniio_builtin:
            if "path" in self.config["chuniio"]:
                del self.config["chuniio"]["path"]
        else:
            selected_chuniio = None
            for radio, value in self.chuniio_radios:
                if radio.isChecked():
                    if value == "custom":
                        selected_chuniio = self.chuniio_custom_edit.text()
                    else:
                        selected_chuniio = value
                    break

            if selected_chuniio:
                self.config["chuniio"]["path"] = selected_chuniio

        # NicoChuniio 配置
        nico_selected = False
        for radio, value in self.chuniio_radios:
            if radio.isChecked() and value == "nicochuniio.dll":
                nico_selected = True
                break

        if nico_selected and not chuniio_builtin:
            if "nico" not in self.config:
                self.config["nico"] = {}
            
            if "nico" in self.widgets:
                self.config["nico"]["autoReconnect"] = self.widgets["nico"]["autoReconnect"]
                self.config["nico"]["reconnectInterval"] = self.widgets["nico"]["reconnectInterval"]
        else:
            if "nico" in self.config:
                del self.config["nico"]

        if "io3" not in self.config:
            self.config["io3"] = {}

        self.config["io3"]["test"] = self.widgets["io3"]["test"].text()
        self.config["io3"]["service"] = self.widgets["io3"]["service"].text()
        self.config["io3"]["coin"] = self.widgets["io3"]["coin"].text()

        if self.widgets["io3"]["ir_custom"].isChecked():
            self.config["io3"]["ir"] = "0x00"
        else:
            self.config["io3"]["ir"] = self.widgets["io3"]["ir"].text()

        if "ir" not in self.config:
            self.config["ir"] = {}

        if self.widgets["io3"]["ir_custom"].isChecked():
            for key, widget in self.widgets.get("ir", {}).items():
                if widget.text():
                    self.config["ir"][key] = widget.text()
        else:
            for i in range(1, 7):
                key = f"ir{i}"
                if key in self.config["ir"]:
                    del self.config["ir"][key]

        if "slider" not in self.config:
            self.config["slider"] = {}

        for key, widget in self.widgets.get("slider", {}).items():
            if isinstance(widget, QCheckBox):
                self.config["slider"][key] = "1" if widget.isChecked() else "0"
            else:
                self.config["slider"][key] = widget.text()
