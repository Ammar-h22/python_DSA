class Cookie:
    def __init__(self, color):  # Constructor
        self.color = color

    def get_color(self):
        return self.color

    def set_color(self, color):
        self.color = color


cookie_one = Cookie("Blue")
cookie_two = Cookie("Green")

print("Cookie one is", cookie_one.get_color())
print("Cookie two is", cookie_two.get_color())

cookie_one.set_color("Yellow")

print("Cookie one is now changed to", cookie_one.get_color())
print("Cookie two is still", cookie_two.get_color())
