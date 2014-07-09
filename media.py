from client import JSONRPC, System

class Files(JSONRPC):
    """
    .. todo:: Implement failing procedure.

    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        super(Files, self).__init__(object)

    def get_item(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Player.GetItem", params=params)
            return self.result_is_ok(r)
        else:
            return False

class Player(JSONRPC):
    """
    .. todo:: Implement failing procedure.

    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        super(Player, self).__init__(object)

    def get_active_players(self):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Player.GetActivePlayers")
            s = self.result_is_ok(r)
            if s:
                return s
        return False

    def get_item(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Player.GetItem", params=params)
            return self.result_is_ok(r)
        else:
            return False

    def get_properties(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Player.GetProperties", params=params)
            return self.result_is_ok(r)
        else:
            return False

    def play_pause(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.PlayPause", params=params)
            return self.result_is_ok(r)
        else:
            return False

class VideoLibrary(JSONRPC):
    """
    .. todo:: Implement failing procedure.

    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        super(VideoLibrary, self).__init__(object)

    def clean(self):
        if self.has_permission(permission="RemoveData"):
            r = self.post(method="VideoLibrary.Clean")
            return self.result_is_ok(r)
        else:
            return False

    def export(self, params={}):
        """
        .. todo:: Add export parameters.
        """
        if self.has_permission(permission="WriteFile"):
            r = self.post(method="VideoLibrary.Export", params=params)
            return self.result_is_ok(r)
        else:
            return False

    def get_episodes(self):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="VideoLibrary.GetEpisodes")
            return self.result_is_ok(r)
        else:
            return False

    def get_episode_details(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="VideoLibrary.GetEpisodeDetails",params=params)
            return self.result_is_ok(r)
        else:
            return False

    def get_movies(self):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="VideoLibrary.GetMovies")
            return self.result_is_ok(r)
        else:
            return False

    def get_movie_details(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="VideoLibrary.GetMovieDetails",params=params)
            return self.result_is_ok(r)
        else:
            return False

    def get_recently_added_episodes(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="VideoLibrary.GetRecentlyAddedEpisodes",params=params)
            return self.result_is_ok(r)
        else:
            return False

    def get_recently_added_movies(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="VideoLibrary.GetRecentlyAddedMovies",params=params)
            return self.result_is_ok(r)
        else:
            return False

    def get_tvshows(self):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="VideoLibrary.GetTVShows")
            return self.result_is_ok(r)
        else:
            return False

    def scan(self):
        if self.has_permission(permission="UpdateData"):
            r = self.post(method="VideoLibrary.Scan")
            return self.result_is_ok(r)
        else:
            return False

class Playlist(System):
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
