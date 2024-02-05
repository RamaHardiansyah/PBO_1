from db import DBConnection as mydb

class Apotek:

    def __init__(self):
        self.__id = None
        self.__kdobat = None
        self.__nama = None
        self.__berat = None
        self.__bentuk_obat = None
        self.conn = None
        self.affected = None
        self.result = None

    @property
    def id(self):
        return self.__id

    @property
    def kdobat(self):
        return self.__kdobat

    @kdobat.setter
    def kdobat(self, value):
        self.__kdobat = value

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, value):
        self.__nama = value

    @property
    def berat(self):
        return self.__berat

    @berat.setter
    def berat(self, value):
        self.__berat = value

    @property
    def bentuk_obat(self):
        return self.__bentuk_obat

    @bentuk_obat.setter
    def bentuk_obat(self, value):
        self.__bentuk_obat = value

    def simpan(self):
        self.conn = mydb()
        val = (self.__kdobat, self.__nama, self.__berat, self.__bentuk_obat)
        sql = "INSERT INTO obat_obatan (kdobat, nama, berat, bentuk) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect()
        return self.affected

    def update(self, id):
        self.conn = mydb()
        val = (self.__kdobat, self.__nama, self.__berat, self.__bentuk_obat, id)
        sql = "UPDATE obat_obatan SET kdobat = %s, nama = %s, berat=%s, bentuk=%s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected

    def updateBykdobat(self, kdobat):
        self.conn = mydb()
        val = (self.__nama, self.__berat, self.__bentuk_obat, kdobat)
        sql = "UPDATE obat_obatan SET nama = %s, berat=%s, bentuk=%s WHERE kdobat=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect()
        return self.affected
        

    def delete(self, id):
        self.conn = mydb()
        sql = "DELETE FROM obat_obatan WHERE id=%s"
        self.affected = self.conn.delete(sql, (id,))
        self.conn.disconnect()
        return self.affected

    def deleteBykdobat(self, kdobat):
        self.conn = mydb()
        sql = "DELETE FROM obat_obatan WHERE kdobat=%s"
        self.affected = self.conn.delete(sql, (kdobat,))
        self.conn.disconnect()
        return self.affected

    def getByID(self, id):
        self.conn = mydb()
        sql = "SELECT * FROM obat_obatan WHERE id=%s"
        self.result = self.conn.findOne(sql, (id,))
        self.__kdobat = self.result[1]
        self.__nama = self.result[2]
        self.__berat = self.result[3]
        self.__bentuk_obat = self.result[4]
        self.conn.disconnect()
        return self.result

    def getBykdobat(self, kdobat):
        self.conn = mydb()
        sql = "SELECT * FROM obat_obatan WHERE kdobat=%s"
        self.result = self.conn.findOne(sql, (kdobat,))
        if self.result is not None:
            self.__kdobat = self.result[1]
            self.__nama = self.result[2]
            self.__berat = self.result[3]
            self.__bentuk_obat = self.result[4]
            self.affected = self.conn.cursor.rowcount
        else:
            self.__kdobat = ''
            self.__nama = ''
            self.__berat = ''
            self.__bentuk_obat = ''
            self.affected = 0
        self.conn.disconnect()
        return self.result

    def getAllData(self):
        self.conn = mydb()
        sql = "SELECT * FROM obat_obatan"
        self.result = self.conn.findAll(sql)
        return self.result

# Tampilkan Data
A = Apotek()
B = A.getAllData()
print(B)
