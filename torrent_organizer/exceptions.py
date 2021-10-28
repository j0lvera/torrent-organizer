class TorrentOrganizerException(Exception):
    """Base exception"""

    pass


class InIgnoreList(TorrentOrganizerException):
    """File name contains words in ignore list"""

    def __init__(self, message, payload=None):
        self.message = message
        self.payload = payload

    def __str__(self):
        return str(self.message)
