class athlete:
    """Athlete class, with only name attribute"""
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"athlete('{self.name}')"

    def __repr__(self):
        return f"athlete('{self.name}')"

    def display(self):
        print(self.name)

if __name__ == '__main__':
    a = athlete("Ana G.")
    a.display()
    print(a)
    print(repr(a))
    print(f"a: {id(a)}")
    b = repr(a)
    print(b)
    b = eval(b)
    print(b)
    print(f"b: {id(b)}")