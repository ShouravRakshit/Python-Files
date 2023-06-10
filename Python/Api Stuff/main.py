class PlayerCharacter:
    # By instantiating we are creating a object
    def __init__(self, name, age):
        self.name = "i"
        self.age = 17

    def run(self):
        print("run")


player1 = PlayerCharacter("Ivan", 20)
print(player1.age, "\t", player1.name)
