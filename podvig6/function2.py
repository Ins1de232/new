tp = input().strip()

if tp == "RECT":
    def get_sq(length, width):
        return length * width
else:
    def get_sq(side):
        return side * side