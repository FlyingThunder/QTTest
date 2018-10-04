import testing

class bar:
    def barmethod(self):
        testing.foo().foomethod()
        print("test2")


if __name__ == "__main__":
    bar().barmethod()