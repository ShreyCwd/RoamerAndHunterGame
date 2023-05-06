# Roamer and Hunter game for where Roamer is 🌞 and Hunter is 🌛, and 42 specific area

# importing of modules
import random
import os
import time

# declaration of class: Field
class Field: 
    list = [['🌚' for i in range (20)] for x in range (10)]


    def __init__ (self):
        # starting position of R and H as Field.list[r][c]
        Field.list[0][0] = '🌞'
        Field.list [9][19] = '🌛'

        # declare count for the declarion of 40 '🪐'
        count = 0
        while True:
            if count == 40:
                break

            else:
                c = random.randint (1, 18)
                r = random.randint (1, 8)

                # declaration where '🪐' can be:

                if Field.list [r][c] != '🪐':
                    Field.list[r][c] = '🪐'
                    count += 1


    # define display function
    def display(self):
        # print each row
        for r in range(len(Field.list)):
            # for each row, iterate through the column
            for c in range(len(Field.list[r])):
                print(Field.list[r][c], end=" ")
            print()
        # wait half a second and clear the console
        time.sleep(0.5)
        os.system('clear')


    @staticmethod
    def main():
        # create an instance of Roamer and Field
        r = Roamer()
        h = Hunter ()
        f = Field()


        # keep navigating Roamer and Hunter and updating the display until the endpoint '🌛' is reached
        f.display()
        while True:
            r.navigate(f)
            h.navigate (f)
            f.display()
            if (r.row, r.col) == (h.row, h.col):
                break



class Roamer:
    def __init__ (self):
        self.row = 0
        self.col = 0

        # for direction be 1 - Up / 2 - Down / 3 - Left / 4 - Right
        self.direction = 1

    def navigate (self, Field):
        # Field.list[self.row][self.col] = '🌚'
        moved = False

        while moved == False:
            # 20% chance of changing direction
            self.chance = random.randint (1, 5)

            # 80% chance
            if self.chance <= 4:
                # assuming that player fell in 80% chance and  his previous direction was up, down, left, right.
                if self.direction == 1:
                    if self.row-1 >= 0 and Field.list[self.row-1][self.col]== '🌚':
                        Field.list [self.row][self.col] = '🌚'
                        self.row -=1
                        Field.list [self.row][self.col] = '🌞'
                        break

                elif self.direction == 2:
                    if self.row+1 < 10 and Field.list[self.row+1][self.col]== '🌚':
                        Field.list [self.row] [self.col] = '🌚'
                        self.row += 1
                        Field.list [self.row] [self.col] = '🌞'
                        break

                elif self.direction == 3:
                    if self.col-1 >= 0 and Field.list[self.row][self.col-1]== '🌚':
                        Field.list [self.row][self.col] = '🌚'
                        self.col -=1
                        Field.list [self.row][self.col] = '🌞'
                        break

                elif self.direction == 4:
                    if self.col+1 < 20 and Field.list[self.row][self.col+1]== '🌚':
                        Field.list [self.row][self.col] = '🌚'
                        self.col +=1
                        Field.list [self.row][self.col] = '🌞'
                        break

                
            else:
                while True:
                    if moved: break
                    # 1 - Up / 2 - Down / 3 - Left / 4 - Right
                    self.direct = random.randint (1,4)
                    if self.direct != self.direction:
                        if self.direct == 1:
                            if self.row-1 >= 0 and Field.list[self.row-1][self.col]== '🌚':
                                self.direction = self.direct
                                Field.list [self.row][self.col] = '🌚'
                                self.row -=1
                                Field.list [self.row][self.col] = '🌞'
                                moved = True
                                break

                        elif self.direct == 2:
                            if self.row+1 < 10 and Field.list[self.row+1][self.col]== '🌚':
                                self.direction = self.direct
                                Field.list [self.row] [self.col] = '🌚'
                                self.row += 1
                                Field.list [self.row] [self.col] = '🌞'
                                moved = True
                                break

                        elif self.direct == 3:
                            if self.col-1 >= 0 and Field.list[self.row][self.col-1]== '🌚':
                                self.direction = self.direct
                                Field.list [self.row][self.col] = '🌚'
                                self.col -=1
                                Field.list [self.row][self.col] = '🌞'
                                moved = True
                                break

                        elif self.direct == 4:
                            if self.col+1 < 20 and Field.list[self.row][self.col+1]== '🌚':
                                self.direction = self.direct
                                Field.list [self.row][self.col] = '🌚'
                                self.col +=1
                                Field.list [self.row][self.col] = '🌞'
                                moved = True
                                break
                
class Hunter:

    def __init__ (self):
        self.row = 9
        self.col = 19

        # for direction be 1 - Up / 2 - Down / 3 - Left / 4 - Right
        self.direction = 1

    def navigate (self, Field):
        moved = False

        if (self.row+1 < 10 and Field.list[self.row+1][self.col]== '🪐') or \
            (self.row + 1 < 10 and Field.list[self.row+1][self.col]== '🌞'):
                Field.list [self.row][self.col] = '🌚'
                self.row +=1
                Field.list [self.row][self.col] = '🌛'
                moved = True
                
        elif (self.row-1 >= 0 and Field.list[self.row-1][self.col]== '🪐') or \
            (self.row - 1 >= 0 and Field.list[self.row-1][self.col]== '🌞') :   
                Field.list [self.row][self.col] = '🌚'
                self.row -=1
                Field.list [self.row][self.col] = '🌛'
                moved = True
                

        elif (self.col-1 >= 0 and Field.list[self.row][self.col-1]== '🪐') or \
            (self.col-1 >= 0 and Field.list[self.row][self.col-1]== '🌞'):
                Field.list [self.row][self.col] = '🌚'
                self.col -=1
                Field.list [self.row][self.col] = '🌛'
                moved = True
                

        elif (self.col+1 < 20 and Field.list[self.row][self.col+1]== '🪐') or \
            (self.col + 1 < 20 and Field.list[self.row][self.col+1]== '🌞') :
                Field.list [self.row][self.col] = '🌚'
                self.col +=1
                Field.list [self.row][self.col] = '🌛'
                moved = True
                
        while not moved:
            
                # 20% chance of changing direction
                self.chance = random.randint (1, 5)

                # 80% chance
                if self.chance <= 4:
                    # assuming that player fell in 80% chance and  his previous direction was up, down, left, right.
                    if self.direction == 1:
                        if self.row-1 >= 0 and Field.list[self.row-1][self.col]== '🌚':
                            Field.list [self.row][self.col] = '🌚'
                            self.row -=1
                            Field.list [self.row][self.col] = '🌛'
                            moved = True
                            break

                    elif self.direction == 2:
                        if self.row+1 < 10 and Field.list[self.row+1][self.col]== '🌚':
                            Field.list [self.row] [self.col] = '🌚'
                            self.row += 1
                            Field.list [self.row] [self.col] = '🌛'
                            moved = True
                            break

                    elif self.direction == 3:
                        if self.col-1 >= 0 and Field.list[self.row][self.col-1]== '🌚':
                            Field.list [self.row][self.col] = '🌚'
                            self.col -=1
                            Field.list [self.row][self.col] = '🌛'
                            moved = True
                            break

                    elif self.direction == 4:
                        if self.col+1 < 20 and Field.list[self.row][self.col+1]== '🌚':
                            Field.list [self.row][self.col] = '🌚'
                            self.col +=1
                            Field.list [self.row][self.col] = '🌛'
                            moved = True
                            break

                    
                else:
                    while True:
                        if moved: break
                        # 1 - Up / 2 - Down / 3 - Left / 4 - Right
                        self.direct = random.randint (1,4)
                        if self.direct != self.direction:
                            if self.direct == 1:
                                if self.row-1 >= 0 and Field.list[self.row-1][self.col]== '🌚':
                                    self.direction = self.direct
                                    Field.list [self.row][self.col] = '🌚'
                                    self.row -=1
                                    Field.list [self.row][self.col] = '🌛'
                                    moved = True
                                    break

                            elif self.direct == 2:
                                if self.row+1 < 10 and Field.list[self.row+1][self.col]== '🌚':
                                    self.direction = self.direct
                                    Field.list [self.row] [self.col] = '🌚'
                                    self.row += 1
                                    Field.list [self.row] [self.col] = '🌛'
                                    moved = True
                                    break

                            elif self.direct == 3:
                                if self.col-1 >= 0 and Field.list[self.row][self.col-1]== '🌚':
                                    self.direction = self.direct
                                    Field.list [self.row][self.col] = '🌚'
                                    self.col -=1
                                    Field.list [self.row][self.col] = '🌛'
                                    moved = True
                                    break

                            elif self.direct == 4:
                                if self.col+1 < 20 and Field.list[self.row][self.col+1]== '🌚':
                                    self.direction = self.direct
                                    Field.list [self.row][self.col] = '🌚'
                                    self.col +=1
                                    Field.list [self.row][self.col] = '🌛'
                                    moved = True
                                    break



                        



Field.main()
