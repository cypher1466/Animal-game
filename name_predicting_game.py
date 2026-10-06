import random

name = ["Lion","Tiger","Elephant","Giraffe","Zebra","Leopard","Cheetah","Hippopotamus","Rhinoceros","Gorilla","Chimpanzee","Monkey",
    "Baboon","Kangaroo","Koala","Panda","Bear", "Wolf","Fox","Deer","Horse","Donkey","Cow","Goat","Sheep","Pig","Dog",
    "Cat","Rabbit","Mouse","Rat","Squirrel","Camel","Buffalo""Antelope","Hyena","Crocodile","Alligator","Snake","Lizard","Turtle",
    "Tortoise","Frog","Toad","Eagle","Hawk","Parrot","Owl","Penguin","Ostrich","Peacock","Chicken","Duck","Goose",
    "Swan","Dolphin","Whale","Shark","Octopus","Crab"]

word = random.choice(name).lower()
dash = "-" * len(word)
for _ in dash:
    print(_,end=" ")
print()


placing = list(dash)
while placing != list(word):
            try:
                text = input("Enter letters: ").lower()
                if not text:
                    print("")
                else:
                        if text in word:
                            list(word)
                            for _ in word:
                                indexing = word.index(text)
                                placing[indexing] = text  
                                if text in placing:
                                    indexing = word.rfind(text)
                                    placing[indexing] = text
                                else:
                                     pass 
                        else:
                             print("Letter not in word")    
                        for i in placing:
                            print(i,end=" ")
                        print()
                    
            except ValueError:
                pass
    
    

