import phep_tinh as pt
try:
    a, b = map(int, input().split())

    print(pt.tinh_tong(a, b))
    print(pt.tinh_hieu(a, b))
    print(pt.tinh_tich(a, b))
    print(pt.tinh_thuong(a, b))
except Exception as e:
    print(f"Error: {e}")

finally:
    print("Done!")