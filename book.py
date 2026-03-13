class Book:
    def __init__(self, id_buku, judul, penulis, tahun):
        self.__id_buku = id_buku
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun
        self.status = "tersedia"
