from lib.music_tracker import MusicTracker

def test_list_tracks_is_empty_initially():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

def test_add_one_track_and_list_it():
    tracker = MusicTracker()
    tracker.add("Bohemian Rhapsody by Queen")
    assert tracker.list_tracks() == ["Bohemian Rhapsody by Queen"]