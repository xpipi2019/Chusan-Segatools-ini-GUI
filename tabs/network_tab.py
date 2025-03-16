from PyQt5.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
)

from localization import Localization
from utils import create_scrollable_layout


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
        ((Localization.get_text(parent.language, "offline")), "127.0.0.1"),
        ((Localization.get_text(parent.language, "custom_selecton")), "custom"),
    ]

    parent.dns_radios = []
    for i, (label, value) in enumerate(dns_options):
        radio = QRadioButton(label)
        dns_radio_group.addButton(radio, i)
        dns_server_layout.addWidget(radio)
        parent.dns_radios.append((radio, value))

    parent.custom_dns_layout = QHBoxLayout()
    parent.custom_dns_label = QLabel(
        Localization.get_text(parent.language, "custom_dns")
    )
    parent.custom_dns_edit = QLineEdit()
    parent.custom_dns_layout.addWidget(parent.custom_dns_label)
    parent.custom_dns_layout.addWidget(parent.custom_dns_edit)

    dns_server_layout.addLayout(parent.custom_dns_layout)
    dns_layout.addLayout(dns_server_layout)

    dns_group.setLayout(dns_layout)
    layout.addWidget(dns_group)

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
