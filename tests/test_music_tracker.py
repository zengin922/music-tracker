from lib.music_tracker import MusicTracker

def test_list_tracks_is_empty_initially():
    tracker = MusicTracker()
    assert tracker.list_tracks() == []

def test_add_one_track_and_list_it():
    tracker = MusicTracker()
    tracker.add("Bohemian Rhapsody by Queen")
    assert tracker.list_tracks() == ["Bohemian Rhapsody by Queen"]

def test_add_several_tracks_keeps_order():
    tracker = MusicTracker()
    tracker.add("Bohemian Rhapsody by Queen")
    tracker.add("Hey Ya! by OutKast")
    assert tracker.list_tracks() == ["Bohemian Rhapsody by Queen", "Hey Ya! by OutKast"]

def test_same_track_twice_is_listed_twice():
    tracker = MusicTracker()
    tracker.add("Hey Ya! by OutKast")
    tracker.add("Hey Ya! by OutKast")
    assert tracker.list_tracks() == ["Hey Ya! by OutKast", "Hey Ya! by OutKast"]