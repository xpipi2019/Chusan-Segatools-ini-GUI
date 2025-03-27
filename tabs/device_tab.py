from PyQt5.QtWidgets import (
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
)
import os

from localization import Localization
from utils import (
    browse_file,
    create_scrollable_layout,
    edit_aime_card,
    update_aime_edit_button_state,
)

# 创建Aime卡
def create_aime_card(parent, aime_path, current_file):
    if not current_file:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "warning"),
            Localization.get_text(parent.language, "please_open_config"),
        )
        return False
        
    if not aime_path:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "warning"),
            Localization.get_text(parent.language, "please_set_aime_path"),
        )
        return False
        
    config_dir = os.path.dirname(os.path.abspath(current_file))
    
    # 创建device目录（如果不存在）
    device_dir = os.path.join(config_dir, "DEVICE")
    if not os.path.exists(device_dir):
        try:
            os.makedirs(device_dir)
        except Exception as e:
            QMessageBox.critical(
                parent,
                Localization.get_text(parent.language, "error"),
                Localization.get_text(parent.language, "create_folder_error").format(str(e)),
            )
            return False
    
    # 创建aime.txt
    aime_file = os.path.join(device_dir, "aime.txt")
    if os.path.exists(aime_file):
        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "info"),
            Localization.get_text(parent.language, "aime_file_exists"),
        )
        return False
        
    try:
        with open(aime_file, "w", encoding="utf-8") as f:
            f.write("")
        
        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "success"),
            Localization.get_text(parent.language, "aime_file_created"),
        )
        return True
    except Exception as e:
        QMessageBox.critical(
            parent,
            Localization.get_text(parent.language, "error"),
            Localization.get_text(parent.language, "create_file_failed").format(str(e)),
        )
        return False


def check_aime_file_exists(current_file):
    if not current_file:
        return False
        
    config_dir = os.path.dirname(os.path.abspath(current_file))
    aime_file = os.path.join(config_dir, "DEVICE", "aime.txt")
    return os.path.exists(aime_file)


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

    # 创建Aime卡按钮
    aime_create_btn = QPushButton(
        Localization.get_text(parent.language, "create_aime_card")
    )
    aime_create_btn.clicked.connect(
        lambda: create_aime_card(parent, aime_path_edit.text(), parent.current_file) and update_aime_buttons_state()
    )
    aime_layout.addWidget(aime_create_btn)

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

    def update_aime_buttons_state():
        enabled = aime_enable.isChecked()
        aime_path_edit.setEnabled(enabled)
        aime_path_browse.setEnabled(enabled)
        aime_path_tip.setEnabled(enabled)
        
        if enabled:
            aime_file_exists = check_aime_file_exists(parent.current_file)
            aime_create_btn.setEnabled(enabled and not aime_file_exists)
            update_aime_edit_button_state(parent, aime_path_edit.text(), aime_edit_btn)
        else:
            aime_create_btn.setEnabled(False)
            aime_edit_btn.setEnabled(False)

    aime_enable.toggled.connect(update_aime_buttons_state)
    aime_path_edit.textChanged.connect(update_aime_buttons_state)
    
    parent.config_loaded.connect(update_aime_buttons_state)

    update_aime_buttons_state()

    layout.addStretch()
