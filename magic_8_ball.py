import random
import time

def ascii_art_8ball():
    print('''____
    ,dP9CGG88@b,
  ,IP  _   Y888@@b,
 dIi  (_)   G8888@b
dCII  (_)   G8888@@b
GCCIi     ,GG8888@@@
GGCCCCCCCGGG88888@@@
GGGGCCCGGGG88888@@@@...
Y8GGGGGG8888888@@@@P.....
 Y88888888888@@@@@P......
 `Y8888888@@@@@@@P'......
    `@@@@@@@@@P'.......
        """........''')

def possible_outcomes():
    #list containing all possible outcomes
    outcomes = [
    """        ___________
       /           \\
       \  OUTLOOK  /
        \ NOT SO  /
         \ GOOD. /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \           /
        \   YES.  /
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \   CANNOT  /
        \ PREDICT /
         \  NOW. /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \    MOST   /
        \  LIKELY./
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \   IT IS   /
        \ CERTAIN./
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \  MY REPLY /
        \    IS   /
         \   NO. /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \    VERY   /
        \ DOUBTFUL/
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \  AS I SEE /
        \ IT YES. /
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \ BETTER NOT/
        \ TELL YOU/
         \  NOW. /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \ MY SOURCES/
        \ SAY NO. /
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \ REPLY HAZY/
        \TRY AGAIN/
         \       /
          \     /
           \___/ """,
    """         ___________
       /           \\
       \  OUTLOOK  /
        \  GOOD.  /
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \  YOU MAY  /
        \ RELY ON /
         \  IT.  /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \DON'T COUNT/
        \  ON IT. /
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \CONCENTRATE/
        \ AND ASK /
         \ AGAIN./
          \     /
           \___/ """,
    """        ___________
       /           \\
       \  WITHOUT  /
        \ A DOUBT./
         \       /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \  IT IS    /
        \DECIDEDLY/
         \  SO.  /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \   SIGNS   /
        \ POINT TO/
         \  YES. /
          \     /
           \___/ """,
    """        ___________
       /           \\
       \   VERY    /
        \ DOUBTFUL/
         \       /
          \     /
           \___/ """,
    """        ____________
       /            \\
       \    YES -   /
        \DEFINITELY/
         \        /
          \      /
           \____/ """,
    """        ___________
       /           \\
       \ ASK AGAIN /
        \  LATER. /
         \       /
          \     /
           \___/ """]
 


    return outcomes

def user_question():
    question = input("Ask your question and i will answer it: ")
    return question

def loading_time():
    for i in range(3):
        time.sleep(1)
        print(".",end='')
    print('\n')

def random_choice(lst):
    rand_numb = random.randint(0,19)
    print(lst[rand_numb])

def main_8_ball():
    ascii_art_8ball()
    lst = possible_outcomes()
    user_question()
    print("Predicting Outcome ",end='')
    loading_time()
    random_choice(lst)

if __name__ == "__main__":
    main_8_ball()