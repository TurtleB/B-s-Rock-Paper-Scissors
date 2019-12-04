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
    current_pattern = init_move_pattern(3)
    player_wins = 0
    cpu_wins = 0
    ties = 0
    player_pattern_map = {}

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

        # Get CPU move.
        cpu_move = get_cpu_move(player_pattern_map, current_pattern)

        # Get player move.
        player_move = input("Show ya moves: ")
        player_move = player_move.upper()
        print("")

        # If player chose a valid move, play turn.
        if player_move in move_set:

            player_move = move_set.index(player_move)

            # Update current move pattern and pattern map.
            update_pattern_map(player_pattern_map, current_pattern, player_move)
            current_pattern = get_updated_pattern(current_pattern, player_move)
            
            draw_match(player_move, cpu_move, player_name)

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

        # Show instructions.
        elif player_move == "?":
            print_instructions()
            
        # If player chooses to quit, don't do another turn.        
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


# Pattern stuff


# Returns a blank move pattern of size n.
def init_move_pattern(n):
    new_move_pattern = ["N"] * n
    return new_move_pattern


# Returns a move pattern with the oldest move dropped and move added.
def get_updated_pattern(pattern, move):
    move_token = move_set[move]
    updated_pattern = pattern[1:len(pattern)]
    updated_pattern.append(move_token)
    return updated_pattern


# Creates a key for a move pattern.
def get_pattern_key(pattern):
    key = ""
    for m in pattern:
        key = key + m
    return key


# Updates the move distribution for a given pattern.
def update_pattern_map(pattern_map, pattern, move):
    pattern_key = get_pattern_key(pattern)
    
    if pattern_key not in pattern_map:
        new_move_distribution = [0] * len(move_set)
        pattern_map[pattern_key] = new_move_distribution

    move_distribution = pattern_map[pattern_key]
    move_distribution[move] = move_distribution[move] + 1


# Tries to counter the most likely next move based on the pattern. Returns a random move if pattern isn't in pattern_map.
def get_cpu_move(pattern_map, pattern):

    # Pick a random move.
    cpu_move = random.randint(0, len(move_set) - 1)

    
    pattern_key = get_pattern_key(pattern)

    if pattern_key in pattern_map:

        # Find the most likely move to come next and pick the counter.
        move_distribution = pattern_map[pattern_key]
        likely_player_move = move_distribution.index(max(move_distribution))

        cpu_move = (likely_player_move + 1) % len(move_set)

    return cpu_move

 
main()


# ASCII drawings


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
# TODO - implement template.
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
