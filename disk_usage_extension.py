import subprocess
import gi
gi.require_version("Nautilus", "4.1")
from gi.repository import Nautilus, GObject

class DiskUsageExtension(GObject.GObject, Nautilus.MenuProvider):
    def menu_activate_cb(self, menu, file):
        path = file.get_location().get_path()
        if path:
            subprocess.Popen(["baobab", path])

    def get_file_items(self, files):
        if len(files) != 1 or not files[0].is_directory():
            return []
        item = Nautilus.MenuItem(
            name="DiskUsageExtension::ScanFolder",
            label="Scan with Disk Usage Analyzer",
            tip="Analyze disk space used by this folder"
        )
        item.connect("activate", self.menu_activate_cb, files[0])
        return [item]
