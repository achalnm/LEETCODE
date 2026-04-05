moves = input("Enter the moves")

vertical = moves.count("U") - moves.count("D")
horizontal = moves.count("L") - moves.count("R")

if vertical == 0  and horizontal == 0:
    print("Robot back at original position")
else:
    print("Robot not at original position")