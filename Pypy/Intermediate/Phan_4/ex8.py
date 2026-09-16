class TaiKhoanNganHang:
    def __init__(self, so_du = 0):
        self.so_du = so_du

    def gui_tien(self, so_tien):
        if so_tien > 0:
            self.so_du += so_tien
    def rut_tien(self, so_tien):
        if 0 < so_tien <= self.so_du:
            self.so_du -= so_tien
    def xem_so_du(self):
        return self.so_du

if __name__ == "__main__":
    n = int(input())
    tknh = TaiKhoanNganHang()
    for _ in range(n):
        parts = input().split()
        lenh = parts[0].upper()
        money = int(parts[1])
        if lenh == "GUI":
            tknh.gui_tien(money)

        elif lenh == "RUT":
            tknh.rut_tien(money)

        elif lenh == "XEM":
            print(tknh.xem_so_du())
