import pytest


# TODO: put some of this code into a pre-function

PHOTOS_DB = "./tests/Test-10.14.6.photoslibrary/database/photos.db"
PHOTOS_DB_PATH = "/Test-10.14.6.photoslibrary/database/photos.db"
PHOTOS_LIBRARY_PATH = "/Test-10.14.6.photoslibrary"

ALBUMS = ["Pumpkin Farm", "Test Album", "Test Album (1)"]
ALBUM_DICT = {"Pumpkin Farm": 3, "Test Album": 1, "Test Album (1)": 1}


def test_album_names():
    import osxphotos

    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    albums = photosdb.album_names

    assert len(albums) == len(ALBUMS)
    for album in albums:
        assert album in ALBUMS


def test_albums_names_shared():
    import osxphotos

    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    albums_shared = photosdb.album_names_shared

    assert len(albums_shared) == 0


def test_albums_as_dict():
    import osxphotos

    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    albums_as_dict = photosdb.albums_as_dict

    for album in albums_as_dict:
        assert album in ALBUM_DICT
        assert albums_as_dict[album] == ALBUM_DICT[album]


def test_albums_shared_as_dict():
    import osxphotos

    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    albums_shared_as_dict = photosdb.albums_shared_as_dict

    assert albums_shared_as_dict == {}


def test_shared():
    import osxphotos

    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    photos = [p for p in photosdb.photos() if p.shared]
    assert len(photos) == 0


def test_not_shared():
    import osxphotos

    photosdb = osxphotos.PhotosDB(dbfile=PHOTOS_DB)
    photos = [p for p in photosdb.photos() if not p.shared]
    assert len(photos) == 7
