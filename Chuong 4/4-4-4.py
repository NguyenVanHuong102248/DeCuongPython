class NhanVien:
    def __init__(self):
        pass

    def nhap(self):
        self.ma, self.ten, self.hsl, self.pc = input().split()
        self.ma = int(self.ma)
        self.hsl = float(self.hsl)
        self.pc = int(self.pc)
        self.luong = self.hsl * 2000000 + self.pc

    def xuat(self):
        print("{0} {1} {2:.2f} {3} {4:.2f}".format(self.ma, self.ten, self.hsl, self.pc, self.luong))

n = int(input())
ds = []
for _ in range(n):
    nhanvien = NhanVien()
    nhanvien.nhap()
    ds.append(nhanvien)
min_luong = min(ds, key=lambda x: x.luong)

print("Nhan vien co luong thap nhat")
min_luong.xuat()
