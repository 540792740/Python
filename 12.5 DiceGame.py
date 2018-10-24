import random


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        print("The game initialize successfully!")


    def start_game(self):
        self.player1.drop()
        self.player2.drop()
        # player1_dice_count_list = [self.player1.dice[0].count, self.player1.dices[1], self.player1.dices[2]]
        # player2_dice_count_list = [self.player2.dice[0].count, self.player2.dices[1], self.player2.dices[2]]
        # print("The counter of Player1 drop dices : %s"%str(player1_dice_count_list))
        print(self.player2)
        print(self.player1)

class Player:
    def __init__(self, name, sex, *dice):   #*dice is a tuple
        self.name = name
        self.sex = sex
        self.dicess = dice

    def drop(self):
       for dice in self.dicess:
           dice.moveTo()

    def guess_dice(self):
        return(4,2)  #for 4 point 2

    def __str__(self):
        play_dice_count_list = [self.dicess[0].count, self.dicess[1].count, self.dicess[2].count]
        return "Name is: %s, Counter contains: %s"%(self.name, str(play_dice_count_list))

class Dice:
    def __init__(self):
        self.count = 0


    def moveTo(self):
        self.count = random.randint(1,6)
        # From 1 to 7 with no include eage
        # print(self.count)

    def __str__(self):
        return "%s"%(self.count)


# There are six Dices in the game
d1 = Dice()
d2 = Dice()
d3 = Dice()
d4 = Dice()
d5 = Dice()
d6 = Dice()

p1 = Player("Jiawei", "Male", d1,d2,d3)
p2 = Player("Yongjian", "Male", d4,d5,d6)



for i in range(0,5):
    print("Game %d ----------------------------" % i)
    game = Game(p1, p2)
    game.start_game()
    print()
    print()
