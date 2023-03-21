class Rectangle:
    def __init__(self, w, h):
        if type(w) not in (int, float) or type(h) not in (int, float):
            raise TypeError
        if w < 0 or h < 0:
            raise ValueError
        self.w, self.h = w, h

    def get_area(self):
        return self.w * self.h

    def get_perimeter(self):
        return 2 * (self.w + self.h)
