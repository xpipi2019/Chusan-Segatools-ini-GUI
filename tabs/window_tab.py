from PyQt5.QtWidgets import (
    QCheckBox,
    QGroupBox,
    QHBoxLayout,
    QLabel,
    QSpinBox,
    QVBoxLayout,
)

from localization import Localization
from utils import create_scrollable_layout


def setup_window_tab(parent, tab):
    layout = create_scrollable_layout(tab)

    # GFX
    gfx_group = QGroupBox(Localization.get_text(parent.language, "window_settings"))
    gfx_layout = QVBoxLayout()

    # Windowed
    windowed = QCheckBox(Localization.get_text(parent.language, "windowed_mode"))
    gfx_layout.addWidget(windowed)

    # Framed
    framed = QCheckBox(Localization.get_text(parent.language, "show_frame"))
    gfx_layout.addWidget(framed)

    # Display
    display_layout = QHBoxLayout()
    display_label = QLabel(Localization.get_text(parent.language, "monitor"))
    display_spin = QSpinBox()
    display_spin.setRange(0, 10)

    display_layout.addWidget(display_label)
    display_layout.addWidget(display_spin)
    gfx_layout.addLayout(display_layout)

    display_tip = QLabel(Localization.get_text(parent.language, "monitor_tip"))
    display_tip.setStyleSheet("color: blue;")
    gfx_layout.addWidget(display_tip)

    gfx_group.setLayout(gfx_layout)
    layout.addWidget(gfx_group)

    if "gfx" in parent.config:
        windowed.setChecked(parent.config["gfx"].getboolean("windowed", False))
        framed.setChecked(parent.config["gfx"].getboolean("framed", False))
        display_spin.setValue(int(parent.config["gfx"].get("monitor", "0")))

    parent.widgets["gfx"] = {
        "windowed": windowed,
        "framed": framed,
        "monitor": display_spin,
    }

    layout.addStretch()
