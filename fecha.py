class Fecha:
    def __init__(self, dd=None, mm=None, aa=None):
        self.dd = dd
        self.mm = mm
        self.aa = aa

    def get_dd(self):
        return self.dd

    def set_dd(self, dd):
        self.dd = dd

    def get_mm(self):
        return self.mm

    def set_mm(self, mm):
        self.mm = mm

    def get_aa(self):
        return self.aa

    def set_aa(self, aa):
        self.aa = aa

    def __str__(self):
        return f"{self.dd} - {self.mm} - {self.aa}"