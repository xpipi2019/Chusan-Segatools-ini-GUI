from PyQt5.QtWidgets import (
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from localization import Localization
from utils import KeycodeEdit, create_scrollable_layout


def setup_input_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    # IO3
    io3_group = QGroupBox(Localization.get_text(parent.language, "io3_settings"))
    io3_layout = QVBoxLayout()

    io3_tip = QLabel(Localization.get_text(parent.language, "keycode_tip"))
    io3_tip.setStyleSheet("color: blue;")
    io3_layout.addWidget(io3_tip)

    vk_tip = QLabel(Localization.get_text(parent.language, "vk_tip"))
    vk_tip.setStyleSheet("color: blue;")
    io3_layout.addWidget(vk_tip)

    # Test
    test_layout = QHBoxLayout()
    test_label = QLabel(Localization.get_text(parent.language, "test_key"))
    test_edit = KeycodeEdit()

    test_layout.addWidget(test_label)
    test_layout.addWidget(test_edit)
    io3_layout.addLayout(test_layout)

    # Service
    service_layout = QHBoxLayout()
    service_label = QLabel(Localization.get_text(parent.language, "service_key"))
    service_edit = KeycodeEdit()

    service_layout.addWidget(service_label)
    service_layout.addWidget(service_edit)
    io3_layout.addLayout(service_layout)

    # Coin
    coin_layout = QHBoxLayout()
    coin_label = QLabel(Localization.get_text(parent.language, "coin_key"))
    coin_edit = KeycodeEdit()

    coin_layout.addWidget(coin_label)
    coin_layout.addWidget(coin_edit)
    io3_layout.addLayout(coin_layout)

    # IR
    ir_layout = QHBoxLayout()
    ir_label = QLabel(Localization.get_text(parent.language, "ir_key"))
    ir_custom_hardware = QCheckBox(
        Localization.get_text(parent.language, "use_custom_air")
    )
    ir_edit = KeycodeEdit()

    ir_layout.addWidget(ir_label)
    ir_layout.addWidget(ir_custom_hardware)
    ir_layout.addWidget(ir_edit)
    io3_layout.addLayout(ir_layout)

    ir_tip = QLabel(Localization.get_text(parent.language, "ir_tip"))
    ir_tip.setStyleSheet("color: blue;")
    io3_layout.addWidget(ir_tip)

    # 重置按钮
    reset_btn = QPushButton(Localization.get_text(parent.language, "reset"))
    io3_layout.addWidget(reset_btn)

    io3_group.setLayout(io3_layout)
    layout.addWidget(io3_group)

    ir_group = QGroupBox(Localization.get_text(parent.language, "ir_sensor_settings"))
    ir_layout = QVBoxLayout()

    ir_sensor_tip = QLabel(Localization.get_text(parent.language, "ir_sensor_tip"))
    ir_sensor_tip.setStyleSheet("color: blue;")
    ir_layout.addWidget(ir_sensor_tip)

    ir_sensors_layout = QHBoxLayout()
    ir_sensors = []

    for i in range(6, 0, -1):
        ir_sensor_label = QLabel(f"IR{i}:")
        ir_sensor_edit = QLineEdit()
        ir_sensor_edit.setFixedWidth(50)
        ir_sensors.append((ir_sensor_label, ir_sensor_edit))
        ir_sensors_layout.addWidget(ir_sensor_label)
        ir_sensors_layout.addWidget(ir_sensor_edit)

        if i > 1:
            ir_sensors_layout.addSpacing(10)

    ir_layout.addLayout(ir_sensors_layout)
    ir_group.setLayout(ir_layout)
    layout.addWidget(ir_group)

    # Slider
    slider_group = QGroupBox(Localization.get_text(parent.language, "slider_settings"))
    slider_layout = QVBoxLayout()

    slider_enable = QCheckBox(Localization.get_text(parent.language, "enable_slider"))
    slider_layout.addWidget(slider_enable)

    slider_tip = QLabel(Localization.get_text(parent.language, "slider_tip"))
    slider_tip.setStyleSheet("color: blue;")
    slider_layout.addWidget(slider_tip)

    slider_note = QLabel(Localization.get_text(parent.language, "slider_note"))
    slider_layout.addWidget(slider_note)

    slider_group.setLayout(slider_layout)
    layout.addWidget(slider_group)

    if "io3" in parent.config:
        test_edit.setText(parent.config["io3"].get("test", "0x70"))
        service_edit.setText(parent.config["io3"].get("service", "0x71"))
        coin_edit.setText(parent.config["io3"].get("coin", "0x72"))

        ir_value = parent.config["io3"].get("ir", "0x20")
        # 检查是否是AIR硬件 (0x0, 0x00, 0)
        if ir_value in ["0x0", "0x00", "0"]:
            ir_custom_hardware.setChecked(True)
            ir_edit.setText("0x00")
        else:
            ir_custom_hardware.setChecked(False)
            ir_edit.setText(ir_value)
    else:
        # 默认值
        test_edit.setText("0x70")  # F1
        service_edit.setText("0x71")  # F2
        coin_edit.setText("0x72")  # F3
        ir_edit.setText("0x20")  # Space

    if "ir" in parent.config:
        for i, (label, edit) in enumerate(ir_sensors):
            sensor_num = 6 - i
            key = f"ir{sensor_num}"
            if key in parent.config["ir"]:
                edit.setText(parent.config["ir"][key])

    if "slider" in parent.config:
        slider_enable.setChecked(parent.config["slider"].getboolean("enable", False))

    parent.widgets["io3"] = {
        "test": test_edit,
        "service": service_edit,
        "coin": coin_edit,
        "ir": ir_edit,
        "ir_custom": ir_custom_hardware,
    }

    parent.widgets["ir"] = {}
    for i, (label, edit) in enumerate(ir_sensors):
        sensor_num = 6 - i
        parent.widgets["ir"][f"ir{sensor_num}"] = edit

    parent.widgets["slider"] = {"enable": slider_enable}

    def update_ir_state():
        custom_hardware = ir_custom_hardware.isChecked()
        ir_edit.setEnabled(not custom_hardware)
        if custom_hardware:
            ir_edit.setText("0x00")

        # 更新IR传感器设置的可用性
        for label, edit in ir_sensors:
            label.setEnabled(custom_hardware)
            edit.setEnabled(custom_hardware)
        ir_sensor_tip.setEnabled(custom_hardware)

    def reset_keycodes():
        test_edit.setText("0x70")  # F1
        service_edit.setText("0x71")  # F2
        coin_edit.setText("0x72")  # F3
        if not ir_custom_hardware.isChecked():
            ir_edit.setText("0x20")  # Space

    ir_custom_hardware.toggled.connect(update_ir_state)
    reset_btn.clicked.connect(reset_keycodes)

    update_ir_state()

    layout.addStretch()
