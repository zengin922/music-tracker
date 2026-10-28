from lib.music_tracker import MusicTracker

def test_list_tracks_is_empty_initially():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []