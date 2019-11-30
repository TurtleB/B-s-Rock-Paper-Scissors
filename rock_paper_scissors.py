import random

move_set = ["R", "P", "S"]

# Arrays used for drawing moves. 11 rows x 16 characters
ascii_rock = ["    ________    ", "  */_/____\_\   ", "  /_/______\_\  ", "  \ \ *    / /  ", "  *\ \    / /   ", "    \ \  / /    ", "     \    /     ", "      \  /      ", "       \/       ", "                ", "      ROCK      "]
ascii_paper = ["   _________    ", "  |         |#  ", "  |         |#  ", "  |         |#  ", "  |         |#  ", "  |         |#  ", "  |         |#  ", "  |_________|#  ", "   ###########  ", "                ", "      PAPER     "]
ascii_scissors = ["    __    __    ", "   /  \  /  \   ", "   \__/\/\__/   ", "      \()/      ", "      /\ \      ", "     / /\ \     ", "    / /  \ \    ", "   / /    \ \   ", "   \/      \/   ", "                ", "    SCISSORS    "]
ascii_vs = ["                ", "                ", "                ", "                ", "                ", "          __    ", "    \  / (_     ", "     \/  __)    ", "                ", "                ", "       VS       "]

ascii_moves = [ascii_rock, ascii_paper, ascii_scissors]

def main():

    # Initialize game state.
    playing = True
    player_wins = 0
    cpu_wins = 0
    ties = 0

    # Prompt the player for their name.
    player_name = input("Enter your name (up to 16 characters): ")
    if len(player_name) == 0:
        player_name = "PLAYER"
    elif len(player_name) > 16:
        player_name = player_name[0:16]
    player_name = player_name.upper()

    # Print greeting and instructions.
    print("Welcome to B's Rock Paper Sicissors Game!")
    print_instructions()
    print("")
    print("")

    # Main game loop.
    while playing:

        # Get player move.
        player_move = input("Show ya moves: ")
        player_move = player_move.upper()
        print("")

        # If player chose a valid move, play turn.
        if player_move in move_set:
            cpu_move = random.choice(move_set)

            player_move = move_set.index(player_move)
            cpu_move = move_set.index(cpu_move)

            draw_match(player_move, cpu_move, player_name)
            print("")

            # Get the result of the match.
            winner = get_winner(player_move, cpu_move)

            # Handle result of match.
            if winner == "PLAYER":
                player_wins = player_wins + 1
                print(player_name + " WINS")
            elif winner == "COMPUTER":
                cpu_wins = cpu_wins + 1
                print("COMPUTER WINS")
            else:
                print("IT'S A TIE")
                ties = ties + 1

        # Show the game stats.
        elif player_move == "I":
            print(player_name + "'S SCORE: " + str(player_wins))
            print("COMPUTER'S SCORE: " + str(cpu_wins))
            print("TIED GAMES: " + str(ties))

        elif player_move == "?":
            print_instructions()
            
        # If player chooses to quit, skip turn and stop game.        
        elif player_move == "Q":
            print("Thanks for playing :)")
            playing = False

        # Unkown command entered.
        else:
            print("Unknown command. Type \"?\" for help")

        print("")
        print("")


# Compares the player move and cpu move and returns the winner.
def get_winner(player_move, cpu_move):
    winner = "TIE"

    if move_set[player_move] == "R" and move_set[cpu_move] == "S":
        winner = "PLAYER"
    elif move_set[cpu_move] == "R" and move_set[player_move] == "S":
        winner = "COMPUTER"
    elif player_move > cpu_move:
        winner = "PLAYER"
    elif cpu_move > player_move:
        winner = "COMPUTER"

    return winner


# Prints an ASCII rendering of the match.
def draw_match(player_move, cpu_move, player_name):

    # 16 length string of spaces used to format names.
    name_format = "                "

    # Center player name for display.
    formatted_player_name = name_format[0:((len(name_format) - len(player_name)) // 2)] + player_name
    formatted_player_name = formatted_player_name + name_format[0:(len(name_format) - len(formatted_player_name))]

    # Computer name formatted for display.
    formatted_cpu_name = "    COMPUTER    "

    # Print player names and their moves.
    print(formatted_player_name + name_format + formatted_cpu_name)
    for row in range(11):
        print(ascii_moves[player_move][row] + ascii_vs[row] + ascii_moves[cpu_move][row])


# Prints the game instructions
def print_instructions():
    print("Moves:")
    print("   \"R\" Rock")
    print("   \"P\" Paper")
    print("   \"S\" Scissors")
    print("Options:")
    print("   \"I\" Info - Game stats")
    print("   \"?\" Help - Show these instructions again")
    print("   \"Q\" Quit - End the game")
    
    
main()


# ASCII Scissors
# 11 rows x 16 cols
# "    __    __    "
# "   /  \  /  \   "
# "   \__/\/\__/   "
# "      \()/      "
# "      /\ \      "
# "     / /\ \     "
# "    / /  \ \    "
# "   / /    \ \   "
# "   \/      \/   "
# "                "
# "    SCISSORS    "


# ASCII Paper
# 11 rows x 16 cols
# "   _________    "
# "  |         |#  "
# "  |         |#  "
# "  |         |#  "
# "  |         |#  "
# "  |         |#  "
# "  |         |#  "
# "  |_________|#  "
# "   ###########  "
# "                "
# "      PAPER     "
# 
# TODO - implement template. Adjust template to have margins (5 x 7 array)
# "   _________    "
# "  |         |#  "
# "  | {} |  "
# "  |_________|#  "
# "   ###########  "
# "                "
# "     PAPER      "
# 5 x 7 character array can be used to write a message on the paper.


# ASCII Rock
# 11 rows x 16 cols 
# "    ________    "
# "  */_/____\_\   "
# "  /_/______\_\  "
# "  \ \ *    / /  "
# "  *\ \    / /   "
# "    \ \  / /    "
# "     \    /     "
# "      \  /      "
# "       \/       "
# "                "
# "      ROCK      "


# ASCII Versus
# 11 rows x 16 cols 
# generated with https://www.kammerl.de/ascii/AsciiSignature.php
# "                "
# "                "
# "                "
# "                "
# "                "
# "          __    "
# "    \  / (_     "
# "     \/  __)    "
# "                "
# "                "
# "       VS       "
