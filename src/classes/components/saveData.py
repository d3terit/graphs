from ursina import *
from ursina.prefabs.file_browser_save import FileBrowserSave
import json
class SaveData(FileBrowserSave):
    def __init__(self):
        super().__init__(
            file_type = '.json',
            enabled = False,
            position = (0,.4,-20)
        )


    def show(self,data):
        self.path = Path('src/assets/storage').resolve()
        self.data = json.dumps(data, indent=4)
        self.enabled = True