import tkinter as tk
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))))

from src.frontend.ui_constants import ui_constants
from src.frontend.widgets.settings_widgets.settings_page import SettingsPage
from src.backend.settings_manager import SettingsManager

FONT = ui_constants.FONT
FONTSIZE = ui_constants.FONTSIZE
BACKGROUND_COLOR = ui_constants.BACKGROUND_COLOR
HEADER_COLOR = ui_constants.HEADER_COLOR
ACCENT_COLOR = ui_constants.ACCENT_COLOR
TEXT_COLOR = ui_constants.TEXT_COLOR

class ModelSettingsPage(SettingsPage):
    def __init__(self, parent):
        super().__init__(parent, "Model Options")

        self.settings_manager = SettingsManager()
        self.model_settings = self.settings_manager.get_model_settings()