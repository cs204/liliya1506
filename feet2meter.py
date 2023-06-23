def main():
    v = feet2meter(input("Сколько футов:"))
    print(f"Это будет {v:.2f} метров.")

def feet2meter(s):
    f = s.rstrip("ft")
    f = float(f)
    return f*0.3048

main()