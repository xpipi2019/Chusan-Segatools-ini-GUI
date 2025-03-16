from PyQt5.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QComboBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QRadioButton,
    QVBoxLayout,
)

from localization import Localization
from utils import create_scrollable_layout


def setup_board_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    # Keychip
    keychip_group = QGroupBox(
        Localization.get_text(parent.language, "keychip_settings")
    )
    keychip_layout = QVBoxLayout()

    # Subnet
    subnet_layout = QHBoxLayout()
    subnet_label = QLabel(Localization.get_text(parent.language, "subnet"))
    subnet_edit = QLineEdit()

    subnet_layout.addWidget(subnet_label)
    subnet_layout.addWidget(subnet_edit)
    keychip_layout.addLayout(subnet_layout)

    # ID
    id_layout = QHBoxLayout()
    id_label = QLabel(Localization.get_text(parent.language, "id"))
    id_edit = QLineEdit()

    id_layout.addWidget(id_label)
    id_layout.addWidget(id_edit)
    keychip_layout.addLayout(id_layout)

    id_tip = QLabel(Localization.get_text(parent.language, "id_tip"))
    id_tip.setStyleSheet("color: blue;")
    keychip_layout.addWidget(id_tip)

    keychip_group.setLayout(keychip_layout)
    layout.addWidget(keychip_group)

    # System
    system_group = QGroupBox(Localization.get_text(parent.language, "system_settings"))
    system_layout = QVBoxLayout()

    system_enable = QCheckBox(Localization.get_text(parent.language, "enable_alls"))
    system_layout.addWidget(system_enable)

    system_tip = QLabel(Localization.get_text(parent.language, "system_tip"))
    system_tip.setStyleSheet("color: red;")
    system_layout.addWidget(system_tip)

    # Freeplay
    freeplay = QCheckBox(Localization.get_text(parent.language, "enable_freeplay"))
    system_layout.addWidget(freeplay)

    freeplay_tip = QLabel(Localization.get_text(parent.language, "freeplay_tip"))
    freeplay_tip.setStyleSheet("color: blue;")
    system_layout.addWidget(freeplay_tip)

    # DIPSW1
    dipsw1_layout = QVBoxLayout()
    dipsw1_label = QLabel(Localization.get_text(parent.language, "dipsw1"))
    dipsw1_layout.addWidget(dipsw1_label)

    dipsw1_radio_group = QButtonGroup(parent)
    dipsw1_client = QRadioButton(
        Localization.get_text(parent.language, "dipsw1_client")
    )
    dipsw1_server = QRadioButton(
        Localization.get_text(parent.language, "dipsw1_server")
    )
    dipsw1_radio_group.addButton(dipsw1_client, 0)
    dipsw1_radio_group.addButton(dipsw1_server, 1)

    dipsw1_layout.addWidget(dipsw1_client)
    dipsw1_layout.addWidget(dipsw1_server)

    dipsw1_tip = QLabel(Localization.get_text(parent.language, "dipsw1_tip"))
    dipsw1_tip.setStyleSheet("color: blue;")
    dipsw1_layout.addWidget(dipsw1_tip)

    system_layout.addLayout(dipsw1_layout)

    # DIPSW2
    dipsw2_layout = QHBoxLayout()
    dipsw2_label = QLabel(Localization.get_text(parent.language, "dipsw2"))
    dipsw2_combo = QComboBox()
    dipsw2_combo.addItem("120FPS", "0")
    dipsw2_combo.addItem("60FPS", "1")

    dipsw2_layout.addWidget(dipsw2_label)
    dipsw2_layout.addWidget(dipsw2_combo)
    system_layout.addLayout(dipsw2_layout)

    # DIPSW3
    dipsw3_layout = QHBoxLayout()
    dipsw3_label = QLabel(Localization.get_text(parent.language, "dipsw3"))
    dipsw3_combo = QComboBox()
    dipsw3_combo.addItem("SP", "0")
    dipsw3_combo.addItem("CVT", "1")

    dipsw3_layout.addWidget(dipsw3_label)
    dipsw3_layout.addWidget(dipsw3_combo)
    system_layout.addLayout(dipsw3_layout)

    display_tip = QLabel(Localization.get_text(parent.language, "display_tip"))
    display_tip.setStyleSheet("color: blue;")
    system_layout.addWidget(display_tip)

    system_group.setLayout(system_layout)
    layout.addWidget(system_group)

    # 设置初始值
    if "keychip" in parent.config:
        subnet_edit.setText(parent.config["keychip"].get("subnet", ""))
        id_edit.setText(parent.config["keychip"].get("id", ""))

    if "system" in parent.config:
        system_enable.setChecked(parent.config["system"].getboolean("enable", False))
        freeplay.setChecked(parent.config["system"].getboolean("freeplay", False))

        dipsw1_value = parent.config["system"].get("dipsw1", "1")
        if dipsw1_value == "0":
            dipsw1_client.setChecked(True)
        else:
            dipsw1_server.setChecked(True)

        dipsw2_index = dipsw2_combo.findData(parent.config["system"].get("dipsw2", "0"))
        if dipsw2_index >= 0:
            dipsw2_combo.setCurrentIndex(dipsw2_index)

        dipsw3_index = dipsw3_combo.findData(parent.config["system"].get("dipsw3", "0"))
        if dipsw3_index >= 0:
            dipsw3_combo.setCurrentIndex(dipsw3_index)

    parent.widgets["keychip"] = {"subnet": subnet_edit, "id": id_edit}

    parent.widgets["system"] = {
        "enable": system_enable,
        "freeplay": freeplay,
        "dipsw1_client": dipsw1_client,
        "dipsw1_server": dipsw1_server,
        "dipsw2": dipsw2_combo,
        "dipsw3": dipsw3_combo,
    }

    layout.addStretch()
