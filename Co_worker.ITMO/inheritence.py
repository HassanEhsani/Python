class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    def be_annuying(self):
        print("annouting")


dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.be_annuying()
