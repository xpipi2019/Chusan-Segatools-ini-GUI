from PyQt5.QtWidgets import (
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from localization import Localization
from utils import browse_folder, create_default_folders, create_scrollable_layout


def setup_path_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    tips_label = QLabel(Localization.get_text(parent.language, "path_tips"))
    tips_label.setStyleSheet("color: blue;")
    layout.addWidget(tips_label)

    # VFS
    vfs_group = QGroupBox(Localization.get_text(parent.language, "vfs_settings"))
    vfs_layout = QVBoxLayout()

    # AMFS
    amfs_layout = QHBoxLayout()
    amfs_label = QLabel(Localization.get_text(parent.language, "amfs_path"))
    amfs_edit = QLineEdit()
    amfs_browse = QPushButton(Localization.get_text(parent.language, "browse"))
    amfs_browse.clicked.connect(lambda: browse_folder(parent, amfs_edit))

    amfs_layout.addWidget(amfs_label)
    amfs_layout.addWidget(amfs_edit)
    amfs_layout.addWidget(amfs_browse)
    vfs_layout.addLayout(amfs_layout)

    # Option
    option_layout = QHBoxLayout()
    option_label = QLabel(Localization.get_text(parent.language, "option_path"))
    option_edit = QLineEdit()
    option_browse = QPushButton(Localization.get_text(parent.language, "browse"))
    option_browse.clicked.connect(lambda: browse_folder(parent, option_edit))

    option_layout.addWidget(option_label)
    option_layout.addWidget(option_edit)
    option_layout.addWidget(option_browse)
    vfs_layout.addLayout(option_layout)

    # AppData
    appdata_layout = QHBoxLayout()
    appdata_label = QLabel(Localization.get_text(parent.language, "appdata_path"))
    appdata_edit = QLineEdit()
    appdata_browse = QPushButton(Localization.get_text(parent.language, "browse"))
    appdata_browse.clicked.connect(lambda: browse_folder(parent, appdata_edit))

    appdata_layout.addWidget(appdata_label)
    appdata_layout.addWidget(appdata_edit)
    appdata_layout.addWidget(appdata_browse)
    vfs_layout.addLayout(appdata_layout)

    # 创建默认文件夹按钮
    create_folders_btn = QPushButton(
        Localization.get_text(parent.language, "create_default_folders")
    )
    create_folders_btn.clicked.connect(
        lambda: create_default_folders(parent, amfs_edit, option_edit, appdata_edit)
    )
    vfs_layout.addWidget(create_folders_btn)

    vfs_group.setLayout(vfs_layout)
    layout.addWidget(vfs_group)

    if "vfs" in parent.config:
        amfs_edit.setText(parent.config["vfs"].get("amfs", ""))
        option_edit.setText(parent.config["vfs"].get("option", ""))
        appdata_edit.setText(parent.config["vfs"].get("appdata", ""))

    parent.widgets["vfs"] = {
        "amfs": amfs_edit,
        "option": option_edit,
        "appdata": appdata_edit,
    }

    layout.addStretch()
