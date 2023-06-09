class PlayerCharacter:

    def __int__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")


player1 = PlayerCharacter("Ivan", 20)
print(player1.age, "\t", player1.name)
