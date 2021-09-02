from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

def Play(player1, player2):
    if player1.initiative > player2.initiative:
        player1.attack(player2)
    else:
        player2.attack(player1)

    player1.show_stats()
    player2.show_stats()
    
    if player1.health > 0 and player2.health > 0:
        return Play(player1, player2)
    elif player1.health > 0:
        return f"Winner: {player1.name}"
    else:
        return f"Winner: {player2.name}"

print(Play(michelangelo, jack_sparrow))

# Create a play function that would play through the game.
    # Make attacks more complex, but only have the one attack option.
    # Each round, initiative is rolled, speed is the bonus to initiative, higher initiative goes first.
# strength determines damanage.

# Characters only take name as an argument.
# Stats are entered in the code.