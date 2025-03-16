import json
import os
import re

from PyQt5.QtWidgets import (
    QFileDialog,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QMessageBox,
    QPushButton,
    QVBoxLayout,
)

from localization import Localization
from utils import create_scrollable_layout


def setup_misc_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    # 修改 config_common.json 部分
    common_group = QGroupBox(
        Localization.get_text(parent.language, "common_config_settings")
    )
    common_layout = QVBoxLayout()

    common_label = QLabel(Localization.get_text(parent.language, "common_config_desc"))
    common_label.setWordWrap(True)
    common_layout.addWidget(common_label)

    common_button = QPushButton(
        Localization.get_text(parent.language, "fix_common_config")
    )
    common_button.clicked.connect(lambda: fix_common_config(parent))
    common_layout.addWidget(common_button)

    common_group.setLayout(common_layout)
    layout.addWidget(common_group)

    # 修改 config_sp.json 部分
    sp_group = QGroupBox(Localization.get_text(parent.language, "sp_config_settings"))
    sp_layout = QVBoxLayout()

    sp_label = QLabel(Localization.get_text(parent.language, "sp_config_desc"))
    sp_label.setWordWrap(True)
    sp_layout.addWidget(sp_label)

    sp_button = QPushButton(Localization.get_text(parent.language, "fix_sp_config"))
    sp_button.clicked.connect(lambda: fix_sp_config(parent))
    sp_layout.addWidget(sp_button)

    sp_group.setLayout(sp_layout)
    layout.addWidget(sp_group)

    # 修复 OpenSSL 部分
    openssl_group = QGroupBox(
        Localization.get_text(parent.language, "openssl_fix_settings")
    )
    openssl_layout = QVBoxLayout()

    openssl_label = QLabel(Localization.get_text(parent.language, "openssl_fix_desc"))
    openssl_label.setWordWrap(True)
    openssl_layout.addWidget(openssl_label)

    openssl_button = QPushButton(Localization.get_text(parent.language, "fix_openssl"))
    openssl_button.clicked.connect(lambda: fix_openssl(parent))
    openssl_layout.addWidget(openssl_button)

    openssl_group.setLayout(openssl_layout)
    layout.addWidget(openssl_group)

    # 修复 OnlineFlag 部分
    online_flag_group = QGroupBox(
        Localization.get_text(parent.language, "online_flag_settings")
    )
    online_flag_layout = QVBoxLayout()

    online_flag_label = QLabel(
        Localization.get_text(parent.language, "online_flag_desc")
    )
    online_flag_label.setWordWrap(True)
    online_flag_layout.addWidget(online_flag_label)

    online_flag_button = QPushButton(
        Localization.get_text(parent.language, "fix_online_flag")
    )
    online_flag_button.clicked.connect(lambda: fix_online_flag(parent))
    online_flag_layout.addWidget(online_flag_button)

    online_flag_group.setLayout(online_flag_layout)
    layout.addWidget(online_flag_group)

    # TODO: fufubot team segatools change

    layout.addStretch()


def get_bin_folder(parent):
    # 如果已有segatools.ini文件，尝试从其路径推断bin文件夹位置
    if parent.current_file and os.path.exists(parent.current_file):
        ini_dir = os.path.dirname(parent.current_file)
        potential_bin = os.path.join(ini_dir, "bin")
        if os.path.exists(potential_bin) and os.path.isdir(potential_bin):
            return potential_bin

    # 否则让用户选择bin文件夹
    bin_dir = QFileDialog.getExistingDirectory(
        parent, Localization.get_text(parent.language, "select_bin_folder")
    )
    if bin_dir and os.path.exists(bin_dir) and os.path.isdir(bin_dir):
        return bin_dir

    return None


def fix_common_config(parent):
    bin_folder = get_bin_folder(parent)
    if not bin_folder:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "folder_not_found_title"),
            Localization.get_text(parent.language, "bin_folder_not_found"),
        )
        return

    config_path = os.path.join(bin_folder, "config_common.json")
    if not os.path.exists(config_path):
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "file_not_found_title"),
            Localization.get_text(parent.language, "common_config_not_found"),
        )
        return

    try:
        backup_path = config_path + ".bak"
        import shutil

        shutil.copy2(config_path, backup_path)

        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        if "allnet_auth" in config:
            config["allnet_auth"]["type"] = "1.0"

        if "allnet_accounting" in config:
            config["allnet_accounting"]["enable"] = False

        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "success_title"),
            Localization.get_text(parent.language, "common_config_fixed"),
        )

    except Exception as e:
        QMessageBox.critical(
            parent,
            Localization.get_text(parent.language, "error_title"),
            Localization.get_text(parent.language, "fix_error").format(str(e)),
        )


def fix_sp_config(parent):
    bin_folder = get_bin_folder(parent)
    if not bin_folder:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "folder_not_found_title"),
            Localization.get_text(parent.language, "bin_folder_not_found"),
        )
        return

    config_path = os.path.join(bin_folder, "config_sp.json")
    if not os.path.exists(config_path):
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "file_not_found_title"),
            Localization.get_text(parent.language, "sp_config_not_found"),
        )
        return

    try:
        backup_path = config_path + ".bak"
        import shutil

        shutil.copy2(config_path, backup_path)

        with open(config_path, "r", encoding="utf-8") as f:
            config = json.load(f)

        if "emoney" in config:
            config["emoney"]["enable"] = False

        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(config, f, indent=4, ensure_ascii=False)

        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "success_title"),
            Localization.get_text(parent.language, "sp_config_fixed"),
        )

    except Exception as e:
        QMessageBox.critical(
            parent,
            Localization.get_text(parent.language, "error_title"),
            Localization.get_text(parent.language, "fix_error").format(str(e)),
        )


def fix_openssl(parent):
    bin_folder = get_bin_folder(parent)
    if not bin_folder:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "folder_not_found_title"),
            Localization.get_text(parent.language, "bin_folder_not_found"),
        )
        return

    bat_path = os.path.join(bin_folder, "start.bat")
    if not os.path.exists(bat_path):
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "file_not_found_title"),
            Localization.get_text(parent.language, "start_bat_not_found"),
        )
        return

    try:
        backup_path = bat_path + ".bak"
        import shutil

        shutil.copy2(bat_path, backup_path)

        with open(bat_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.readlines()

        openssl_line = "set OPENSSL_ia32cap=:~0x20000000\n"
        if any(line.strip() == openssl_line.strip() for line in content):
            QMessageBox.information(
                parent,
                Localization.get_text(parent.language, "info_title"),
                Localization.get_text(parent.language, "openssl_already_fixed"),
            )
            return

        new_content = []
        added = False
        for line in content:
            new_content.append(line)
            if line.strip().lower() == "@echo off":
                new_content.append(openssl_line)
                added = True

        if not added:
            new_content.insert(0, "@echo off\n")
            new_content.insert(1, openssl_line)

        with open(bat_path, "w", encoding="utf-8") as f:
            f.writelines(new_content)

        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "success_title"),
            Localization.get_text(parent.language, "openssl_fixed"),
        )

    except Exception as e:
        QMessageBox.critical(
            parent,
            Localization.get_text(parent.language, "error_title"),
            Localization.get_text(parent.language, "fix_error").format(str(e)),
        )


def fix_online_flag(parent):
    bin_folder = get_bin_folder(parent)
    if not bin_folder:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "folder_not_found_title"),
            Localization.get_text(parent.language, "bin_folder_not_found"),
        )
        return

    # 检查option/A001是否存在
    option_a001_path = os.path.join(bin_folder, "option", "A001")
    if not os.path.exists(option_a001_path) or not os.path.isdir(option_a001_path):
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "folder_not_found_title"),
            Localization.get_text(parent.language, "a001_not_found"),
        )
        return

    # 检查Event.xml是否存在
    event_xml_path = os.path.join(
        option_a001_path, "event", "event00000018", "Event.xml"
    )
    if not os.path.exists(event_xml_path):
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "file_not_found_title"),
            Localization.get_text(parent.language, "event_xml_not_found"),
        )
        return

    try:
        backup_path = event_xml_path + ".bak"
        import shutil

        shutil.copy2(event_xml_path, backup_path)

        with open(event_xml_path, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()

        if "<alwaysOpen>true</alwaysOpen>" in content:
            QMessageBox.information(
                parent,
                Localization.get_text(parent.language, "info_title"),
                Localization.get_text(parent.language, "online_flag_already_fixed"),
            )
            return

        modified_content = re.sub(
            r"<alwaysOpen>false</alwaysOpen>", "<alwaysOpen>true</alwaysOpen>", content
        )

        if modified_content == content:
            QMessageBox.warning(
                parent,
                Localization.get_text(parent.language, "warning_title"),
                Localization.get_text(parent.language, "online_flag_not_found"),
            )
            return

        with open(event_xml_path, "w", encoding="utf-8") as f:
            f.write(modified_content)

        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "success_title"),
            Localization.get_text(parent.language, "online_flag_fixed"),
        )

    except Exception as e:
        QMessageBox.critical(
            parent,
            Localization.get_text(parent.language, "error_title"),
            Localization.get_text(parent.language, "fix_error").format(str(e)),
        )
