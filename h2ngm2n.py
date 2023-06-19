import os
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen


def sieunhangao():

  def end():
    print("\nPlay again?\n")
    while True:
      user_input = (input("(y/N): "))
      user_input = (user_input).lower()
      if user_input == "y":
        print(sieunhangao())
      if user_input == "n":
        exit()
      else:
        print("Please re-enter! y(Yes) or N (No).")

  def banner():
    print(""" 
   (     (      )    ) :        (      )   
   )\    )\    ((.  ())) ( (    )\    ((.  
  ((_)  ((_))  ))\ ()(()))\)\  ((_))  ))\  
  | |_  (|_  )((_))/ _` |_((_) (|_  )((_)) 
  |   \   / / | ' \)__. | '  \   / / | ' \)
  |_||_| /___||_||_|___/|_|_|_| /___||_||_|
  
  """)
    print("                                        # made with Python")
    return ""

  def batdau():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner())
    print(
      "Welcome to H6ngmaN2p! Let's see what you will type.\n\nPlayer 1 turn.\n"
    )
    print("""
                          o
       _ 0  .-----\-----.  ,_0 _
     o' / \ |\     \     \    \ `o
     __|\___|_`-----\-----`__ /|____
       / |     |          |  | \
  
               |          |
      """)
    random_tu = input(
      "Type secret word(can't add line spacing and capital letters): "
    ).replace(" ", "")
    random_tu = random_tu.lower()

    sokytu = len(random_tu)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner())
    print(
      "Welcome to H6ngmaN2p! Let's see what you will type.\n\nPlayer 1 turn.\n"
    )
    print("Your secret word :", random_tu)
    print("""
                          o
       _ 0  .-----\-----.  ,_0 _
     o' / \ |\     \     \    \ `o
     __|\___|_`-----\-----`__ /|____
       / |     |          |  | \
  
               |          |
      """)
    while True:
      mang = (input("\nEnter the number of incorrect guesses: "))
      if mang.isnumeric():
        mang = int(mang)
        break
      else:
        print("Please re-enter! Only number.")
    # mang = (input("Enter the number of incorrect guesses: "))
    # if mang.isdigit():
    #   mang = int(mang)

    else:
      print("Only number.")
      quit()
    if mang == 0:
      print("Can't be 0.")
      quit()
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner())
    print(
      "Welcome to H6ngmaN2p! Let's see what you will type.\n\nPlayer 1 turn.\n"
    )
    print("Your secret word :", random_tu)
    print("Total number of wrong guesses : ", mang, "\n")
    print("Type not if you don't want to give suggestions .")
    print("""
                          o
       _ 0  .-----\-----.  ,_0 _
     o' / \ |\     \     \    \ `o
     __|\___|_`-----\-----`__ /|____
       / |     |          |  | \
  
               |          |
      """)
    goiy = input("\nGive suggestions or not: ")

    space2 = []

    for i in range(sokytu):
      space2.append('_')
    os.system('cls' if os.name == 'nt' else 'clear')
    print(banner())
    print("Welcome to Hangman! Let's see if you can guess this word!\n")
    print("Player 2 turn.\n")
    print("You have", mang, "incorrect guesses left.", "\n")
    print("Your word is...")
    print(' '.join(space2))
    if goiy == "not":
      print("\nNo suggestions at all!")
    else:
      print("\nSuggestion : ", goiy)
    print("""
                          o
       _ 0  .-----\-----.  ,_0 _
     o' / \ |\     \     \    \ `o
     __|\___|_`-----\-----`__ /|____
       / |     |          |  | \
  
               |          |
      """)
    while ('_' in space2) and (mang > 0):
      # print("see if there is an error: ", random_tu)
      chon = input("\nGuess a letter: ")
      chon = chon.lower()
      os.system('cls' if os.name == 'nt' else 'clear')

      for i, kytu in enumerate(random_tu):
        if chon == kytu:
          space2[i] = kytu
      print(banner())
      print("Welcome to Hangman! Let's see if you can guess this word!\n")
      print("Player 2 turn.\n")
      print(' '.join(space2))
      if goiy == "not":
        print("\nNo suggestions at all!")
      else:
        print("\nSuggestion : ", goiy)

      if len(chon) == 1:
        if chon in random_tu:
          print("\nYes! The letter", chon, "is part of the secret word.")
        else:
          mang -= 1
          print("\nNo! The letter", chon, "is not part of the secret word.")
      else:
        print("\nPlease input only 1 letter.")

      print("\nYou have", mang, "incorrect guesses left.", "\n")
      print("""
                          o
       _ 0  .-----\-----.  ,_0 _
     o' / \ |\     \     \    \ `o
     __|\___|_`-----\-----`__ /|____
       / |     |          |  | \
  
               |          |
        """)

    if mang == 0:
      print("Player 1 won!")
      print("The secret word: ", random_tu)
    else:
      print("Player 2 won!")
    print(end())

  print(batdau())


def doit(screen):
  effects = [
    Cycle(screen, FigletText("Welcome to", font='big'),
          int(screen.height / 2 - 8)),
    Cycle(screen, FigletText("H2NGM2N!", font='big'),
          int(screen.height / 2 + 3)),
    Stars(screen, 200)
  ]
  screen.play([
    Scene(effects, int(screen.width / 2)),
    Scene(effects,
          int(screen.width / 2) + 1)
  ],
              repeat=False)
  screen.clear()
  screen.print_at("Made by Dam Duc Huy", int(screen.width / 2 - 3),
                  int(screen.height / 2))
  screen.refresh()
  screen.wait_for_input(1)


Screen.wrapper(doit)

print(sieunhangao())
