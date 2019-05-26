# Inspired by:
#   https://stackoverflow.com/questions/37865230/changing-editing-mode-in-sublime-text-3-toggle-multiple-settings-with-a-command
import sublime, sublime_plugin

STORED_SETTINGS = {}

class toggle_setting_values( sublime_plugin.TextCommand ):
    def run( self, edit, setting, values ):
        view     = self.view
        settings = view.settings()

        for value in values:
            if value != settings.get(setting):
                settings.set(setting, value)
                break