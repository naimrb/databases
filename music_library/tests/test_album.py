from lib.album import Album

album1 = Album(1, "Title", 1970, 2)
album2 = Album(1, "Title", 1970, 2)

def test_initialising():
    assert isinstance(album1, Album)
    assert album1.id == 1
    assert album1.title == "Title"
    assert album1.release_year == 1970
    assert album1.artist_id == 2

def test_format():
    assert str(album1) == "Album(1, Title, 1970, 2)"

def test_equality():
    
    assert album1 == album2