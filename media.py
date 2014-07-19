from client import JSONRPC, System

class Files(JSONRPC):
    """
    .. todo:: Implement failing procedure.

    :Author:  Willian Paixao <willian.paixaoo@gmail.com>
    :Version: 0.01
    """

    def __init__(self, object):
        super(Files, self).__init__(object)

    def get_directory(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Files.GetDirectory", params=params)
            return self.result_is_ok(r)
        return False

    def get_file_details(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Files.GetFileDetails", params=params)
            return self.result_is_ok(r)
        return False

    def get_sources(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Files.GetSources", params=params)
            return self.result_is_ok(r)
        return False

    def prepare(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Files.PrepareDownload", params=params)
            return self.result_is_ok(r)
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
        return False

    def get_properties(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Player.GetProperties", params=params)
            return self.result_is_ok(r)
        return False

    def goto(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.GoTo", params=params)
            return self.result_is_ok(r)
        return False

    def move(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.Move", params=params)
            return self.result_is_ok(r)
        return False

    def open(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.Open", params=params)
            return self.result_is_ok(r)
        return False

    def play_pause(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.PlayPause", params=params)
            return self.result_is_ok(r)
        return False

    def rotate(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.Rotate", params=params)
            return self.result_is_ok(r)
        return False

    def seek(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.Seek", params=params)
            return self.result_is_ok(r)
        return False

    def set_audio_stream(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.SetAudioStream", params=params)
            return self.result_is_ok(r)
        return False

    def set_partymode(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.SetPartymode", params=params)
            return self.result_is_ok(r)
        return False

    def set_repeat(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.SetRepeat", params=params)
            return self.result_is_ok(r)
        return False

    def set_shuffle(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.SetShuffle", params=params)
            return self.result_is_ok(r)
        return False

    def set_speed(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.SetSpeed", params=params)
            return self.result_is_ok(r)
        return False

    def set_subtitle(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.SetSubtitle", params=params)
            return self.result_is_ok(r)
        return False

    def stop(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.Stop", params=params)
            return self.result_is_ok(r)
        return False

    def zoom(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Player.Zoom", params=params)
            return self.result_is_ok(r)
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

    def add(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Playlist.Add", params=params)
            return self.result_is_ok(r)
        return False

    def clear(self, params={}):
        """
        Resets a playlist.

        :param params: ID of desired play list
        :type params: Playlist.Id
        :rtype: True if successfully, False otherwise
        """
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Playlist.Clear", params=params)
            return self.result_is_ok(r)
        return False

    def get_items(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Playlist.GetItems", params=params)
            return self.result_is_ok(r)
        return False

    def get_playlists(self):
        """
        Return all existing playlists.
        """
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Playlist.GetPlaylists")
            return self.result_is_ok(r)
        return False

    def get_playlist_properties(self, params={}):
        if self.has_permission(permission="ReadData"):
            r = self.post(method="Playlist.GetProperties", params=params)
            return self.result_is_ok(r)
        return False

    def insert(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Playlist.Insert", params=params)
            return self.result_is_ok(r)
        return False

    def remove(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Playlist.Remove", params=params)
            return self.result_is_ok(r)
        return False

    def swap(self, params={}):
        if self.has_permission(permission="ControlPlayback"):
            r = self.post(method="Playlist.Swap", params=params)
            return self.result_is_ok(r)
        return False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80
