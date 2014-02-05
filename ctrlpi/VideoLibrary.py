import JSONRPC
class VideoLibrary(JSONRPC.JSONRPC):
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

    def export(self):
        if self.has_permission(permission="WriteFile"):
            r = self.post(method="VideoLibrary.Export")
            return self.result_is_ok(r)
        else:
            return False

    def scan(self):
        if self.has_permission(permission="UpdateData"):
            r = self.post(method="VideoLibrary.Scan")
            return self.result_is_ok(r)
        else:
            return False

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4 textwidth=80

