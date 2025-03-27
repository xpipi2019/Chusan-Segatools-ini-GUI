from PyQt5.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
)
from PyQt5.QtCore import QThread, pyqtSignal
import subprocess
import platform

from localization import Localization
from utils import create_scrollable_layout


# 创建一个线程类来执行ping测试
class PingThread(QThread):
    ping_result = pyqtSignal(str, bool)
    
    def __init__(self, host_list):
        super().__init__()
        self.host_list = host_list
        
    def run(self):
        for host in self.host_list:
            if host == "custom":
                continue
                
            # 根据操作系统选择ping命令参数
            param = "-n" if platform.system().lower() == "windows" else "-c"
            command = ["ping", param, "1", host]
            
            try:
                # 执行ping命令
                result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=2)
                success = result.returncode == 0
                self.ping_result.emit(host, success)
            except subprocess.TimeoutExpired:
                self.ping_result.emit(host, False)
            except Exception:
                self.ping_result.emit(host, False)

def setup_network_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    # DNS
    dns_group = QGroupBox(Localization.get_text(parent.language, "dns_settings"))
    dns_layout = QVBoxLayout()

    dns_server_layout = QVBoxLayout()
    dns_server_label = QLabel(Localization.get_text(parent.language, "default_server"))
    dns_server_layout.addWidget(dns_server_label)

    dns_radio_group = QButtonGroup(parent)

    # 预设DNS选项
    dns_options = [
        ("RinNET", "aqua.naominet.live"),
        ("AquaNet", "aquadx.hydev.org"),
        ("Sam Aqua", "aime.msm.moe"),
        ("Poiteam.Net", "47.74.15.244"),
        ((Localization.get_text(parent.language, "localhost")), "127.0.0.1"),
        ((Localization.get_text(parent.language, "custom_selecton")), "custom"),
    ]

    parent.dns_radios = []
    parent.dns_status_labels = {} 
    
    for i, (label, value) in enumerate(dns_options):
        radio_layout = QHBoxLayout()
        radio = QRadioButton(label)
        dns_radio_group.addButton(radio, i)
        radio_layout.addWidget(radio)
        
        # 为每个DNS选项添加状态标签
        if value != "custom":
            status_label = QLabel("")
            radio_layout.addWidget(status_label)
            parent.dns_status_labels[value] = status_label
        
        dns_server_layout.addLayout(radio_layout)
        parent.dns_radios.append((radio, value))

    parent.custom_dns_layout = QHBoxLayout()
    parent.custom_dns_label = QLabel(
        Localization.get_text(parent.language, "custom_dns")
    )
    parent.custom_dns_edit = QLineEdit()
    parent.custom_dns_layout.addWidget(parent.custom_dns_label)
    parent.custom_dns_layout.addWidget(parent.custom_dns_edit)

    # 添加测试按钮
    test_button_layout = QHBoxLayout()
    test_dns_button = QPushButton(Localization.get_text(parent.language, "test_network"))
    test_button_layout.addWidget(test_dns_button)
    test_button_layout.addStretch()

    dns_server_layout.addLayout(parent.custom_dns_layout)
    dns_layout.addLayout(dns_server_layout)
    dns_layout.addLayout(test_button_layout)

    dns_group.setLayout(dns_layout)
    layout.addWidget(dns_group)

    # 网络TEST
    def update_ping_result(host, success):
        if host in parent.dns_status_labels:
            if success:
                parent.dns_status_labels[host].setText("✓")
                parent.dns_status_labels[host].setStyleSheet("color: green;")
            else:
                parent.dns_status_labels[host].setText("✗")
                parent.dns_status_labels[host].setStyleSheet("color: red;")
    
    def test_network():
        for label in parent.dns_status_labels.values():
            label.setText("测试中...")
            label.setStyleSheet("color: blue;")
        
        hosts_to_test = [value for _, value in parent.dns_radios if value != "custom"]
        
        if parent.dns_radios[-1][0].isChecked() and parent.custom_dns_edit.text():
            custom_host = parent.custom_dns_edit.text()
            hosts_to_test.append(custom_host)
            
            if custom_host not in parent.dns_status_labels:
                status_label = QLabel("")
                parent.custom_dns_layout.addWidget(status_label)
                parent.dns_status_labels[custom_host] = status_label
        
        # 创建并启动ping线程
        parent.ping_thread = PingThread(hosts_to_test)
        parent.ping_thread.ping_result.connect(update_ping_result)
        parent.ping_thread.start()
    
    test_dns_button.clicked.connect(test_network)

    # NetEnv
    netenv_group = QGroupBox(Localization.get_text(parent.language, "netenv_settings"))
    netenv_layout = QVBoxLayout()

    netenv_enable = QCheckBox(Localization.get_text(parent.language, "lan_simulation"))
    netenv_layout.addWidget(netenv_enable)

    # Address Suffix
    addr_suffix_layout = QHBoxLayout()
    addr_suffix_label = QLabel(Localization.get_text(parent.language, "ip_suffix"))
    addr_suffix_spin = QSpinBox()
    addr_suffix_spin.setRange(1, 254)

    addr_suffix_layout.addWidget(addr_suffix_label)
    addr_suffix_layout.addWidget(addr_suffix_spin)
    netenv_layout.addLayout(addr_suffix_layout)

    suffix_tip = QLabel(Localization.get_text(parent.language, "suffix_tip"))
    suffix_tip.setStyleSheet("color: blue;")
    netenv_layout.addWidget(suffix_tip)

    netenv_group.setLayout(netenv_layout)
    layout.addWidget(netenv_group)

    current_dns = ""
    if "dns" in parent.config:
        current_dns = parent.config["dns"].get("default", "127.0.0.1")

    dns_matched = False
    for radio, value in parent.dns_radios:
        if value == current_dns and value != "custom":
            radio.setChecked(True)
            dns_matched = True
            break

    if not dns_matched:
        parent.dns_radios[-1][0].setChecked(True)
        parent.custom_dns_edit.setText(current_dns)

    if "netenv" in parent.config:
        netenv_enable.setChecked(parent.config["netenv"].getboolean("enable", False))
        addr_suffix_spin.setValue(int(parent.config["netenv"].get("addrSuffix", "11")))

    parent.widgets["dns"] = {"default": None}

    parent.widgets["netenv"] = {"enable": netenv_enable, "addrSuffix": addr_suffix_spin}

    def update_custom_dns_state():
        custom_enabled = parent.dns_radios[-1][0].isChecked()
        parent.custom_dns_edit.setEnabled(custom_enabled)
        parent.custom_dns_label.setEnabled(custom_enabled)

    for radio, _ in parent.dns_radios:
        radio.toggled.connect(update_custom_dns_state)

    update_custom_dns_state()

    layout.addStretch()
