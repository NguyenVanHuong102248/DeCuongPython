class NhanVien:
    def __init__(self):
        pass
    def nhap(self):
        self.ten,self.ma,self.hsl,self.pc = input().split()
        self.ma = int(self.ma)
        self.hsl = float(self.hsl)
        self.pc = int(self.pc)
        self.luong = self.hsl * 2000000+self.pc
    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma, self.ten, self.hsl, self.pc, self.luong))
n = int(input())
ds = []
for i in range(n):
    nhanvien = NhanVien()
    nhanvien.nhap()
    ds.append(nhanvien)
ds.sort(key=lambda x: x.luong, reverse=True)
print("Danh sach nhan vien da sap xep: ",n)
for a in ds:
    a.xuat()