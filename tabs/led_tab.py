from PyQt5.QtWidgets import QCheckBox, QGroupBox, QLabel, QVBoxLayout

from localization import Localization
from utils import create_scrollable_layout


def setup_led_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    warning_label = QLabel(Localization.get_text(parent.language, "led_warning"))
    warning_label.setStyleSheet("color: red; font-weight: bold;")
    layout.addWidget(warning_label)

    # LED15093
    led15093_group = QGroupBox(
        Localization.get_text(parent.language, "led15093_settings")
    )
    led15093_layout = QVBoxLayout()

    led15093_enable = QCheckBox(
        Localization.get_text(parent.language, "enable_led15093")
    )
    led15093_layout.addWidget(led15093_enable)

    led15093_group.setLayout(led15093_layout)
    layout.addWidget(led15093_group)

    # LED
    led_group = QGroupBox(Localization.get_text(parent.language, "led_settings"))
    led_layout = QVBoxLayout()

    led_tip = QLabel(Localization.get_text(parent.language, "led_tip"))
    led_tip.setWordWrap(True)
    led_layout.addWidget(led_tip)

    led_group.setLayout(led_layout)
    layout.addWidget(led_group)

    if "led15093" in parent.config and "enable" in parent.config["led15093"]:
        led15093_enable.setChecked(
            parent.config["led15093"].getboolean("enable", False)
        )

    parent.widgets["led15093"] = {"enable": led15093_enable}

    layout.addStretch()
