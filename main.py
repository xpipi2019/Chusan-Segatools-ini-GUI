import json
import os
import sys

from PyQt5.QtWidgets import QApplication

from config_editor import ConfigEditor


def load_settings():
    """加载用户设置"""
    settings_file = os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "settings.json"
    )
    if os.path.exists(settings_file):
        try:
            with open(settings_file, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return {"language": "zh_CN"}
    return {"language": "zh_CN"}


def main():
    app = QApplication(sys.argv)
    settings = load_settings()
    editor = ConfigEditor(settings.get("language", "zh_CN"))
    editor.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
