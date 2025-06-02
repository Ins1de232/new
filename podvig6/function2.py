def get_square(tp, *args):
    if tp == "RECT":
        length, width = args
        return length * width
    else:
        side = args[0]
        return side * side

def main():
    tp = input("Введите тип фигуры (RECT или другой): ").strip()
    if tp == "RECT":
        length = float(input("Введите длину: "))
        width = float(input("Введите ширину: "))
        area = get_square(tp, length, width)
    else:
        side = float(input("Введите сторону: "))
        area = get_square(tp, side)
    
    print(f"Площадь: {area}")

if __name__ == "__main__":
    main()