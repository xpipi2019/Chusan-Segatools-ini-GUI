from PyQt5.QtWidgets import (
    QButtonGroup,
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QVBoxLayout,
)

from localization import Localization
from utils import browse_file, create_scrollable_layout


def setup_io_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    # AimeIO
    aimeio_group = QGroupBox(Localization.get_text(parent.language, "aimeio_settings"))
    aimeio_layout = QVBoxLayout()

    aimeio_tip = QLabel(Localization.get_text(parent.language, "aimeio_tip"))
    aimeio_tip.setStyleSheet("color: blue;")
    aimeio_layout.addWidget(aimeio_tip)

    aimeio_dll_radio_layout = QVBoxLayout()
    aimeio_dll_label = QLabel(Localization.get_text(parent.language, "aimeio_dll"))
    aimeio_dll_radio_layout.addWidget(aimeio_dll_label)

    aimeio_radio_group = QButtonGroup(parent)

    # 预设AimeIO DLL选项
    aimeio_options = [
        ("aimeio", "aimeio.dll"),
        ((Localization.get_text(parent.language, "custom_selecton")), "custom"),
    ]

    parent.aimeio_radios = []
    for i, (label, value) in enumerate(aimeio_options):
        radio = QRadioButton(label)
        aimeio_radio_group.addButton(radio, i)
        aimeio_dll_radio_layout.addWidget(radio)
        parent.aimeio_radios.append((radio, value))

    parent.aimeio_custom_layout = QHBoxLayout()
    parent.aimeio_custom_label = QLabel(
        Localization.get_text(parent.language, "custom_dll_path")
    )
    parent.aimeio_custom_edit = QLineEdit()
    parent.aimeio_custom_browse = QPushButton(
        Localization.get_text(parent.language, "browse")
    )
    parent.aimeio_custom_browse.clicked.connect(
        lambda: browse_file(parent, parent.aimeio_custom_edit, "DLL 文件 (*.dll)")
    )

    parent.aimeio_custom_layout.addWidget(parent.aimeio_custom_label)
    parent.aimeio_custom_layout.addWidget(parent.aimeio_custom_edit)
    parent.aimeio_custom_layout.addWidget(parent.aimeio_custom_browse)

    aimeio_dll_radio_layout.addLayout(parent.aimeio_custom_layout)
    aimeio_layout.addLayout(aimeio_dll_radio_layout)

    aimeio_group.setLayout(aimeio_layout)
    layout.addWidget(aimeio_group)

    # ChuniIO
    chuniio_group = QGroupBox(
        Localization.get_text(parent.language, "chuniio_settings")
    )
    chuniio_layout = QVBoxLayout()

    chuniio_builtin = QCheckBox(
        Localization.get_text(parent.language, "use_builtin_chuniio")
    )
    chuniio_layout.addWidget(chuniio_builtin)

    chuniio_dll_radio_layout = QVBoxLayout()
    chuniio_dll_label = QLabel(Localization.get_text(parent.language, "chuniio_dll"))
    chuniio_dll_radio_layout.addWidget(chuniio_dll_label)

    chuniio_radio_group = QButtonGroup(parent)

    # 预设ChuniIO DLL选项
    chuniio_options = [
        ("chuniio", "chuniio.dll"),
        ("NicoChuniio", "nicochuniio.dll"),  # New ChuniIO
        ("TASOLLER", "tasoller.dll"),
        ("TASOLLER Plus", "tasoller_plus.dll"),
        ("Brokenithm", "brokenithm.dll"),
        ("chuniio-mux", "chuniio-mux.dll"),
        ((Localization.get_text(parent.language, "custom_selecton")), "custom"),
    ]

    parent.chuniio_radios = []
    for i, (label, value) in enumerate(chuniio_options):
        radio = QRadioButton(label)
        chuniio_radio_group.addButton(radio, i)
        chuniio_dll_radio_layout.addWidget(radio)
        parent.chuniio_radios.append((radio, value))

    parent.chuniio_custom_layout = QHBoxLayout()
    parent.chuniio_custom_label = QLabel(
        Localization.get_text(parent.language, "custom_dll_path")
    )
    parent.chuniio_custom_edit = QLineEdit()
    parent.chuniio_custom_browse = QPushButton(
        Localization.get_text(parent.language, "browse")
    )
    parent.chuniio_custom_browse.clicked.connect(
        lambda: browse_file(parent, parent.chuniio_custom_edit, "DLL 文件 (*.dll)")
    )

    parent.chuniio_custom_layout.addWidget(parent.chuniio_custom_label)
    parent.chuniio_custom_layout.addWidget(parent.chuniio_custom_edit)
    parent.chuniio_custom_layout.addWidget(parent.chuniio_custom_browse)

    chuniio_dll_radio_layout.addLayout(parent.chuniio_custom_layout)
    chuniio_layout.addLayout(chuniio_dll_radio_layout)

    chuniio_group.setLayout(chuniio_layout)
    layout.addWidget(chuniio_group)

    # NicoChuniio 相关配置项
    auto_reconnect_group = QGroupBox(
        Localization.get_text(parent.language, "nicochuniio_settings")
    )
    auto_reconnect_layout = QVBoxLayout()

    # 热拔插开关
    parent.auto_reconnect_checkbox = QCheckBox(
        Localization.get_text(parent.language, "auto_reconnect")
    )
    auto_reconnect_layout.addWidget(parent.auto_reconnect_checkbox)

    # 重连尝试间隔
    reconnect_interval_label = QLabel(
        Localization.get_text(parent.language, "reconnect_interval")
    )
    parent.reconnect_interval_edit = QLineEdit()
    reconnect_interval_layout = QHBoxLayout()
    reconnect_interval_layout.addWidget(reconnect_interval_label)
    reconnect_interval_layout.addWidget(parent.reconnect_interval_edit)
    auto_reconnect_layout.addLayout(reconnect_interval_layout)

    auto_reconnect_group.setLayout(auto_reconnect_layout)
    chuniio_layout.addWidget(auto_reconnect_group)

    # 设置初始值
    # AimeIO
    aimeio_path = ""
    if "aimeio" in parent.config:
        aimeio_path = parent.config["aimeio"].get("path", "")

    aimeio_matched = False
    for radio, value in parent.aimeio_radios:
        if value == aimeio_path and value != "custom":
            radio.setChecked(True)
            aimeio_matched = True
            break

    if not aimeio_matched:
        parent.aimeio_radios[-1][0].setChecked(True)  # 选择"自定义"单选按钮
        parent.aimeio_custom_edit.setText(aimeio_path)

    # ChuniIO
    chuniio_path = ""
    if "chuniio" in parent.config:
        chuniio_path = parent.config["chuniio"].get("path", "")
        # 如果path不存在，则认为使用内建映射
        chuniio_builtin.setChecked("path" not in parent.config["chuniio"])

    chuniio_matched = False
    for radio, value in parent.chuniio_radios:
        if value == chuniio_path and value != "custom":
            radio.setChecked(True)
            chuniio_matched = True
            break

    if not chuniio_matched and chuniio_path:
        parent.chuniio_radios[-1][0].setChecked(True)
        parent.chuniio_custom_edit.setText(chuniio_path)
    elif not chuniio_matched and not chuniio_path:
        parent.chuniio_radios[0][0].setChecked(True)

    parent.widgets["aimeio"] = {"path": None}

    parent.widgets["chuniio"] = {"path": None, "builtin": chuniio_builtin}

    # Chuniio-Nicochuniio
    parent.widgets["nico"] = {"autoReconnect": 0, "reconnectInterval": 1000}

    if "nico" in parent.config:
        parent.widgets["nico"]["autoReconnect"] = parent.config["nico"].get(
            "autoReconnect", 0
        )
        parent.widgets["nico"]["reconnectInterval"] = parent.config["nico"].get(
            "reconnectInterval", 1000
        )

    parent.auto_reconnect_checkbox.setChecked(parent.widgets["nico"]["autoReconnect"])
    parent.reconnect_interval_edit.setText(
        str(parent.widgets["nico"]["reconnectInterval"])
    )

    def update_aimeio_custom_state():
        custom_enabled = parent.aimeio_radios[-1][0].isChecked()
        parent.aimeio_custom_edit.setEnabled(custom_enabled)
        parent.aimeio_custom_label.setEnabled(custom_enabled)
        parent.aimeio_custom_browse.setEnabled(custom_enabled)

    def update_chuniio_custom_state():
        custom_enabled = (
            parent.chuniio_radios[-1][0].isChecked() and not chuniio_builtin.isChecked()
        )
        parent.chuniio_custom_edit.setEnabled(custom_enabled)
        parent.chuniio_custom_label.setEnabled(custom_enabled)
        parent.chuniio_custom_browse.setEnabled(custom_enabled)

    def update_chuniio_radio_state():
        builtin_enabled = chuniio_builtin.isChecked()
        for radio, _ in parent.chuniio_radios:
            radio.setEnabled(not builtin_enabled)
        chuniio_dll_label.setEnabled(not builtin_enabled)
        update_chuniio_custom_state()

    def update_auto_reconnet_state():
        nico_chuniio_selected = (
            parent.chuniio_radios[1][0].isChecked() and not chuniio_builtin.isChecked()
        )
        auto_reconnect_group.setEnabled(nico_chuniio_selected)

    def update_aimeio_state():
        aime_virtual_enabled = False
        if "aime" in parent.widgets and "enable" in parent.widgets["aime"]:
            aime_virtual_enabled = parent.widgets["aime"]["enable"].isChecked()

        # 如果启用了虚拟读卡器，禁用AimeIO设置
        enabled = not aime_virtual_enabled
        for radio, _ in parent.aimeio_radios:
            radio.setEnabled(enabled)
        aimeio_dll_label.setEnabled(enabled)
        parent.aimeio_custom_edit.setEnabled(
            enabled and parent.aimeio_radios[-1][0].isChecked()
        )
        parent.aimeio_custom_label.setEnabled(
            enabled and parent.aimeio_radios[-1][0].isChecked()
        )
        parent.aimeio_custom_browse.setEnabled(
            enabled and parent.aimeio_radios[-1][0].isChecked()
        )
        aimeio_tip.setEnabled(enabled)

    for radio, _ in parent.aimeio_radios:
        radio.toggled.connect(update_aimeio_custom_state)

    for radio, _ in parent.chuniio_radios:
        radio.toggled.connect(update_chuniio_custom_state)

    for radio, value in parent.chuniio_radios:
        radio.toggled.connect(update_auto_reconnet_state)

    chuniio_builtin.toggled.connect(update_chuniio_radio_state)

    if "aime" in parent.widgets and "enable" in parent.widgets["aime"]:
        parent.widgets["aime"]["enable"].toggled.connect(update_aimeio_state)

    update_aimeio_custom_state()
    update_chuniio_radio_state()
    update_aimeio_state()
    update_auto_reconnet_state()

    layout.addStretch()
