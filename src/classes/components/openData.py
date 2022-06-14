from ursina import *
from ursina.prefabs.file_browser_save import FileBrowser

class OpenData(FileBrowser):
    def __init__(self, submit):
        super().__init__(
            file_types = ['.json'],
            enabled = False
        )
        self.position = (0, .4, -20)
        self.on_submit = submit
        self.path = Path('src/assets/storage').resolve()

    def show(self):
        self.enabled = not self.enabled

    