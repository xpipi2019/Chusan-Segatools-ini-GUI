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
from utils import (
    browse_file,
    create_scrollable_layout,
    edit_aime_card,
    update_aime_edit_button_state,
)


def setup_device_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    # Aime
    aime_group = QGroupBox(Localization.get_text(parent.language, "aime_settings"))
    aime_layout = QVBoxLayout()

    aime_enable = QCheckBox(
        Localization.get_text(parent.language, "use_virtual_reader")
    )
    aime_layout.addWidget(aime_enable)

    # Aime Path
    aime_path_layout = QHBoxLayout()
    aime_path_label = QLabel(Localization.get_text(parent.language, "aime_path"))
    aime_path_edit = QLineEdit()
    aime_path_browse = QPushButton(Localization.get_text(parent.language, "browse"))
    aime_path_browse.clicked.connect(lambda: browse_file(parent, aime_path_edit))

    aime_path_layout.addWidget(aime_path_label)
    aime_path_layout.addWidget(aime_path_edit)
    aime_path_layout.addWidget(aime_path_browse)
    aime_layout.addLayout(aime_path_layout)

    aime_path_tip = QLabel(Localization.get_text(parent.language, "path_tip"))
    aime_path_tip.setStyleSheet("color: blue;")
    aime_layout.addWidget(aime_path_tip)

    # 编辑卡号按钮
    aime_edit_btn = QPushButton(
        Localization.get_text(parent.language, "edit_aime_card")
    )
    aime_edit_btn.clicked.connect(
        lambda: edit_aime_card(parent, aime_path_edit.text(), parent.current_file)
    )
    aime_layout.addWidget(aime_edit_btn)

    # High Baud
    aime_high_baud = QCheckBox(
        Localization.get_text(parent.language, "enable_high_baud")
    )
    aime_layout.addWidget(aime_high_baud)

    aime_group.setLayout(aime_layout)
    layout.addWidget(aime_group)

    # VFD
    vfd_group = QGroupBox(Localization.get_text(parent.language, "vfd_settings"))
    vfd_layout = QVBoxLayout()

    vfd_enable = QCheckBox(Localization.get_text(parent.language, "enable_vfd"))
    vfd_layout.addWidget(vfd_enable)

    vfd_tip = QLabel(Localization.get_text(parent.language, "vfd_tip"))
    vfd_tip.setStyleSheet("color: blue;")
    vfd_layout.addWidget(vfd_tip)

    vfd_group.setLayout(vfd_layout)
    layout.addWidget(vfd_group)

    # 设置初始值
    if "aime" in parent.config:
        aime_enable.setChecked(parent.config["aime"].getboolean("enable", False))
        aime_path_edit.setText(parent.config["aime"].get("aimePath", ""))

        # 只有当highBaud键存在时才设置值
        if "highBaud" in parent.config["aime"]:
            aime_high_baud.setChecked(
                parent.config["aime"].getboolean("highBaud", False)
            )
        else:
            aime_high_baud.setProperty("original_state", "unmodified")

    if "vfd" in parent.config:
        vfd_enable.setChecked(parent.config["vfd"].getboolean("enable", False))

    parent.widgets["aime"] = {
        "enable": aime_enable,
        "aimePath": aime_path_edit,
        "highBaud": aime_high_baud,
        "edit_btn": aime_edit_btn,
    }

    parent.widgets["vfd"] = {"enable": vfd_enable}

    def update_aime_path_state():
        enabled = aime_enable.isChecked()
        aime_path_edit.setEnabled(enabled)
        aime_path_browse.setEnabled(enabled)
        aime_path_tip.setEnabled(enabled)
        aime_edit_btn.setEnabled(enabled)

        # 检查文件是否存在
        if enabled:
            update_aime_edit_button_state(parent, aime_path_edit.text(), aime_edit_btn)

    aime_enable.toggled.connect(update_aime_path_state)
    aime_path_edit.textChanged.connect(
        lambda: update_aime_edit_button_state(
            parent, aime_path_edit.text(), aime_edit_btn
        )
    )

    update_aime_path_state()

    layout.addStretch()
