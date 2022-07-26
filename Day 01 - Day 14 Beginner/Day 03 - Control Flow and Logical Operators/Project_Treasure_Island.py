'''
Welcome to treasure island
Write a game of choices to reach the treasure which the Flying Dutchman captain hide

'You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."
'''


print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\n")
print("Your mission is to find the treasure.\n")


# Write your code below

fst_choice = input(
    "You're at a crossroad. Where do you want to go? Type 'left' or 'right' ")


if fst_choice.lower() == "left":
    print('''
                      __..-----')
        ,.--._ .-'_..--...-'
       '-"'. _/_ /  ..--''""'-.
       _.--""...:._:(_ ..:"::. \
    .-' ..::--""_(##)#)"':. \ \)    \ _|_ /
   /_:-:'/  :__(##)##)    ): )   '-./'   '\.-'
   "  / |  :' :/""\///)  /:.'    --(       )--
     / :( :( :(   (#//)  "       .-'\.___./'-.
    / :/|\ :\_:\   \#//\            /  |  \
    |:/ | ""--':\   (#//)              '
    \/  \ :|  \ :\  (#//)
         \:\   '.':. \#//\
          ':|    "--'(#///)
                     (#///)
                     (#///)         ___/""\
                      \#///\           oo##
                      (##///)         `-6 #
                      (##///)          ,'`.
                      (##///)         // `.\
                      (##///)        ||o   \\
                       \##///\        \-+--//
                       (###///)       :_|_(/
                       (sjw////)__...--:: :...__
                       (#/::''        ""--
                     """__;: :            "-._
          __..--""                  `---/ ;                '._
 ___..--""                             `-'                    "-..___
   (_ ""---....___                                     __...--"" _)
     ""--...  ___""-----......._______......----"" - -""
                   """" - --.....   ___....----


    ''')
    scd_choice = input(
        "You've come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.  ")
    if scd_choice.lower() == "wait":
        print(
            '''
            __________   __________   __________
           |  __  __  | |  __  __  | |  __  __  |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |__||__| | | |__||__| | | |__||__| |
           |  __  __()| |  __  __()| |  __  __()|
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |  ||  | | | |  ||  | | | |  ||  | |
           | |__||__| | | |__||__| | | |__||__| |
           |__________| |__________| |__________|
            '''
        )
        trd_choice = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One 'red', one 'yellow' and one 'blue'. Which colour do you choose?  ")
        if trd_choice == "yellow":
            print(
                '''
                                     o
                                   $""$o
                                  $"  $$
                                   $$$$
                                   o "$o
                                  o"  "$
             oo"$$$"  oo$"$ooo   o$    "$    ooo"$oo  $$$"o
o o o o    oo"  o"      "o    $$o$"     o o$""  o$      "$  "oo   o o o o
"$o   ""$$$"   $$         $      "   o   ""    o"         $   "o$$"    o$$
  ""o       o  $          $"       $$$$$       o          $  ooo     o""
     "o   $$$$o $o       o$        $$$$$"       $o        " $$$$   o"
      ""o $$$$o  oo o  o$"         $$$$$"        "o o o o"  "$$$  $
        "" "$"     """""            ""$"            """      """ "
         "oooooooooooooooooooooooooooooooooooooooooooooooooooooo$
          "$$$$"$$$$" $$$$$$$"$$$$$$ " "$$$$$"$$$$$$"  $$$""$$$$
           $$$oo$$$$   $$$$$$o$$$$$$o" $$$$$$$$$$$$$$ o$$$$o$$$"
           $"""""""""""""""""""""""""""""""""""""""""""""""""""$
           $"                                                  o
           $"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$"$$
                '''
            )
            print("You found the treasure! You Win!")
        elif trd_choice == "red":
            print(
                '''
                (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                '''
            )
            print("It's a room full of fire. Game Over.")
        elif trd_choice == "blue":
            print(
                '''
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

                '''
            )
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")
    else:
        print(
            '''
      _///_
     / o    \/
     >))_. /
       <
            ''')
        print("You get attacked by an angry trout. Game Over.\n")
else:
    print(
        '''
                                      +---+
                                      |\   \
  +-----------------------------+     | +---+
   \                      +-----------+ |   |
    \                      \            |   |
     \                 |/   +-----------+   |
      \                (c_      |   \ | |   |
       \                \       |    \| |   |
        \                       |     | |   |
         \                      |     + |   |
          \                     |      \| DM|
           \--------------------+       +---+
            \                    \        \
             \                    \        \
              +-----------------------------+

        '''
    )
    print("You fell into a hole. Game Over.\n")
