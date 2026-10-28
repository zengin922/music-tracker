# MusicTracker Class Design Recipe

## 1. Describe the Problem

```
As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.
```

Notes:
- A track is a string, e.g. "Bohemian Rhapsody by Queen"
- Tracks are listed in the order they were added
- The same track can be added more than once (I might listen to it twice)
- Adding an empty track raises an error

## 2. Design the Class Interface

```python
class MusicTracker:
    # User-facing properties:
    #   none

    def __init__(self):
        # Side effects:
        #   Creates an empty list of tracks
        pass

    def add(self, track):
        # Parameters:
        #   track: string, e.g. "Bohemian Rhapsody by Queen"
        # Returns:
        #   Nothing
        # Side effects:
        #   Adds the track to the list
        #   Raises an exception if the track is an empty string
        pass

    def list_tracks(self):
        # Returns:
        #   A list of strings: every track added, in order
        pass
```

## 3. Create Examples as Tests

```python
"""
Given no tracks
#list_tracks returns an empty list
"""
tracker = MusicTracker()
tracker.list_tracks() # => []

"""
Given one track
#list_tracks returns a list containing that track
"""
tracker = MusicTracker()
tracker.add("Bohemian Rhapsody by Queen")
tracker.list_tracks() # => ["Bohemian Rhapsody by Queen"]

"""
Given several tracks
#list_tracks returns them all in the order they were added
"""
tracker = MusicTracker()
tracker.add("Bohemian Rhapsody by Queen")
tracker.add("Hey Ya! by OutKast")
tracker.list_tracks() # => ["Bohemian Rhapsody by Queen", "Hey Ya! by OutKast"]

"""
Given the same track twice
#list_tracks shows it twice
"""
tracker = MusicTracker()
tracker.add("Hey Ya! by OutKast")
tracker.add("Hey Ya! by OutKast")
tracker.list_tracks() # => ["Hey Ya! by OutKast", "Hey Ya! by OutKast"]

"""
Given an empty track
#add raises an exception
"""
tracker = MusicTracker()
track