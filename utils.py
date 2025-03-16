import os

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (
    QDialog,
    QFileDialog,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from localization import Localization


def create_scrollable_layout(tab):
    scroll = QScrollArea()
    scroll.setWidgetResizable(True)

    content = QWidget()
    layout = QVBoxLayout(content)

    scroll.setWidget(content)

    tab_layout = QVBoxLayout(tab)
    tab_layout.addWidget(scroll)

    return layout


def browse_folder(parent, line_edit):
    folder = QFileDialog.getExistingDirectory(
        parent, Localization.get_text(parent.language, "open_folder_dialog")
    )
    if folder:
        line_edit.setText(folder)


def browse_file(parent, line_edit, filter_str="所有文件 (*)"):
    file_path, _ = QFileDialog.getOpenFileName(
        parent,
        Localization.get_text(parent.language, "open_file_dialog"),
        "",
        filter_str,
    )
    if file_path:
        line_edit.setText(file_path)


def edit_aime_card(parent, aime_path, current_file):
    if not aime_path:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "warning"),
            Localization.get_text(parent.language, "please_open_config"),
        )
        return

    file_path = aime_path
    if not os.path.isabs(aime_path) and current_file:
        base_dir = os.path.dirname(os.path.abspath(current_file))
        file_path = os.path.join(base_dir, aime_path)

    if not os.path.exists(file_path):
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "warning"),
            Localization.get_text(parent.language, "file_not_exist", file_path),
        )
        return

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()

        dialog = QDialog(parent)
        dialog.setWindowTitle(Localization.get_text(parent.language, "edit_aime_title"))
        dialog.setMinimumWidth(300)

        layout = QVBoxLayout(dialog)

        info_label = QLabel(Localization.get_text(parent.language, "edit_aime_desc"))
        layout.addWidget(info_label)

        edit = QLineEdit(content)
        edit.setPlaceholderText(
            Localization.get_text(parent.language, "edit_aime_placeholder")
        )
        layout.addWidget(edit)

        button_layout = QHBoxLayout()
        ok_button = QPushButton(Localization.get_text(parent.language, "ok"))
        cancel_button = QPushButton(Localization.get_text(parent.language, "cancel"))

        ok_button.clicked.connect(dialog.accept)
        cancel_button.clicked.connect(dialog.reject)

        button_layout.addWidget(ok_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)

        if dialog.exec_() == QDialog.Accepted:
            new_content = edit.text().strip()
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(new_content)
            QMessageBox.information(
                parent,
                Localization.get_text(parent.language, "success"),
                Localization.get_text(parent.language, "aime_updated"),
            )

    except Exception as e:
        QMessageBox.critical(
            parent,
            Localization.get_text(parent.language, "error"),
            Localization.get_text(parent.language, "edit_aime_error", str(e)),
        )


def update_aime_edit_button_state(parent, aime_path, edit_button):
    if not aime_path:
        edit_button.setEnabled(False)
        return

    file_path = aime_path
    if not os.path.isabs(aime_path) and parent.current_file:
        base_dir = os.path.dirname(os.path.abspath(parent.current_file))
        file_path = os.path.join(base_dir, aime_path)

    if os.path.exists(file_path) and file_path.lower().endswith(".txt"):
        edit_button.setEnabled(True)
    else:
        edit_button.setEnabled(False)


def create_default_folders(parent, amfs_edit, option_edit, appdata_edit):
    if not parent.current_file:
        QMessageBox.warning(
            parent,
            Localization.get_text(parent.language, "warning"),
            Localization.get_text(parent.language, "please_open_config"),
        )
        return

    ini_dir = os.path.dirname(os.path.abspath(parent.current_file))

    folders = {"amfs": amfs_edit, "option": option_edit, "appdata": appdata_edit}

    created = []
    for folder_name, edit_widget in folders.items():
        folder_path = os.path.join(ini_dir, folder_name)
        try:
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
                created.append(folder_name)

            edit_widget.setText(folder_name)

        except Exception as e:
            QMessageBox.warning(
                parent,
                Localization.get_text(parent.language, "error"),
                Localization.get_text(
                    parent.language, "create_folder_error", folder_name, str(e)
                ),
            )

    if created:
        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "success"),
            Localization.get_text(
                parent.language, "folders_created", ", ".join(created)
            ),
        )
    else:
        QMessageBox.information(
            parent,
            Localization.get_text(parent.language, "success"),
            Localization.get_text(parent.language, "all_folders_exist"),
        )


class KeycodeEdit(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)

    def keyPressEvent(self, event):
        key = event.key()
        if key != Qt.Key_Escape:  # 忽略Escape键
            hex_code = f"0x{key:x}"
            self.setText(hex_code)
