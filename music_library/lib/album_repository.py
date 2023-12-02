from lib.album import Album

class AlbumRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from albums')
        albums = []

        for row in rows:
            item = Album(row["id"], row["title"], row["release_year"], row["artist_id"])
            albums.append(item)

        return albums

    def find(self, album_id):
        rows = self._connection.execute(f"SELECT * from albums WHERE id = {album_id}")
        
        if rows != []:
            row = rows[0]
            return Album(row["id"], row["title"], row["release_year"], row["artist_id"])
        
        else: return None
    
    def create(self, album):
        self._connection.execute('INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s)', [
            album.title, album.release_year, album.artist_id])
    
    def delete(self, album_id):
        self._connection.execute(f"DELETE FROM albums WHERE id = {album_id}")