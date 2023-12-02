from lib.album_repository import AlbumRepository
from lib.album import Album


def test_get_all_records(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    albums = repo.all()

    assert albums == [
        Album(1, 'Doolittle', 1989, 1),
        Album(2, 'Surfer Rosa', 1988, 1),
        Album(3, 'Waterloo', 1974, 2),
        Album(4, 'Super Trouper', 1980, 2),
        Album(5, 'Bossanova', 1990, 1),
        Album(6, 'Lover', 2019, 3),
        Album(7, 'Folklore', 2020, 3),
        Album(8, 'I Put a Spell on You', 1965, 4),
        Album(9, 'Baltimore', 1978, 4),
        Album(10, 'Here Comes the Sun', 1971, 4),
        Album(11, 'Fodder on My Wings', 1982, 4),
        Album(12, 'Ring Ring', 1973, 2)
    ]

def test_get_single_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)
    
    album = repo.find(3)
    assert album == Album(3, "Waterloo", 1974, 2)

def test_create_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    new_album = Album(None, "Title", 1980, 2)
    repo.create(new_album)

    new_album = Album(None, "Title 2", 1999, 1)
    repo.create(new_album)

    album = repo.find(13)
    assert album == Album(13, "Title", 1980, 2)

    album = repo.find(14)
    assert album == Album(14, "Title 2", 1999, 1)

def test_delete_record(db_connection):
    db_connection.seed("seeds/music_library.sql")
    repo = AlbumRepository(db_connection)

    repo.delete(2)
    album = repo.find(2)

    assert album == None