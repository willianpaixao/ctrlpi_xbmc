import System

class Playlist(System.System):
    """
    :Author: Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        super(Playlist, self).__init__(object)

    def add(self, params):
        r = self.post(method="Playlist.Add", params=params)
        if r and (r["result"] == u"OK"):
            return True
        else:
            return False

    def clear(self, params):
        """
        Resets a playlist.

        :param params: ID of desired play list
        :type params: Playlist.Id
        :rtype: True if successfully, False otherwise
        """
        r = self.post(method="Playlist.Clear", params=params)
        if r and (r["result"] == u"OK"):
            return True
        else:
            return False

    def get_items(self, params):
        r = self.post(method="Playlist.GetItems", params=params)
        if r and ("result" in r):
            return r["result"]
        else:
            return False

    def get_playlists(self):
        """
        Return all existing playlists.
        """
        r = self.post(method="Playlist.GetPlaylists")
        if r and ("result" in r):
            return r["result"]
        else:
            return False

    def get_playlist_properties(self, params):
        r = self.post(method="Playlist.GetProperties", params=params)
        if r and ("result" in r):
            return r["result"]
        else:
            return False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80
