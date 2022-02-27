from django.core.files.storage import FileSystemStorage


class DuplicationFixFileSystemStorage(FileSystemStorage):
    """
    Overrides _save method to prevent file duplication
    """

    def _save(self, name, content):
        if self.exists(name):
            return name

        return super()._save(name, content)
