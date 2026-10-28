class MusicTracker:
    def __init__(self):
        self._tracks = []

    def list_tracks(self):
        return self._tracks

class MusicTracker:
    def __init__(self):
        self._tracks = []

    def list_tracks(self):
        return self._tracks

    def add(self, track):
        if track == "":
            raise Exception("Track cannot be empty.")
        self._tracks.append(track)