from ursina import *
from ursina.prefabs.file_browser_save import FileBrowserSave
import json

class SaveData(FileBrowserSave):
    def __init__(self):
        super().__init__(
            file_type = '.json',
            enabled = False,
        )

    def show(self,data):
        self.path = Path('src/assets/storage').resolve()
        self.data = json.dumps(data)
        self.enabled = not self.enabled