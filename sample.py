class Update:
    name = "siva"
    age = 25
    location = "Fremont"

    def food(self, item):
        return print("Siva had {}".format(item))

    def items(self):
        print([self])


x = Update()
# x.food("noodles")
print(x.items())
