class SinhVien:
    def __init__(self):
        pass
    def nhap(self):
        self.ten, self.ma, self.dToan,self.dTriet, self.dLTC = input().split()
        self.ma = int(self.ma)
        self.dToan = float(self.dToan)
        self.dTriet = float(self.dTriet)
        self.dLTC = float(self.dLTC)
        self.dTB = (self.dToan+self.dTriet+self.dLTC)/3
    def xuat(self):
        print("{0} {1} {2:.2f} {3:.2f} {4:.2f} {5:.2f}".format(self.ma,self.ten, self.dToan, self.dTriet, self.dLTC,self.dTB))
n = int(input())
ds = []
for i in range(n):
    sinhvien = SinhVien()
    sinhvien.nhap()
    if (sinhvien.dLTC<4 and sinhvien.dToan <4) or (sinhvien.dLTC<4 and sinhvien.dTriet <4) or(sinhvien.dTriet<4 and sinhvien.dToan <4):
        ds.append(sinhvien)
print("Danh sach sinh vien hoc lai")
for sv in ds:
    sv.xuat()
print("Danh sach nay co {0} sinh vien phai hoc lai".format(len(ds)))