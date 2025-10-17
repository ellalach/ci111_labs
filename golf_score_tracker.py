print("Welcome to the golf score tracker!")

#set par strokes and hole amount
total_par=0
total_strokes=0
hole_amount=int(input("How many holes are you playing? "))
if hole_amount!=18:
    hole_amount=9

#print start of simulation
print("\nReady to start golfing!")
for i in range(hole_amount):
    #determine par and stroke amount for certain hole
    par=int(input(f"\nWhat is the par for hole {i+1}? "))
    strokes=int(input(f"How many strokes did it take you to complete hole {i+1}? "))
    total_par+=par
    total_strokes+=strokes
    #determine golf phrase
    if strokes==1:
        print("Congratulations you got a hole in one!")
    elif strokes==par:
        print("You got par.")
    elif strokes==par-1:
        print("Congratulations you got a birdie!")
    elif strokes==par-2:
        print("Congratulations you got an eagle!")
    elif strokes==par-3:
        print("Congratulations you got an albatross!")
    elif strokes==par-4:
        print("Congratulations you got a condor!")
    elif strokes==par+1:
        print("You got a bogey.")
    elif strokes==par+2:
        print("You got a double bogey.")
    elif strokes==par+3:
        print("You got a triple bogey...")
    elif strokes==par+4:
        print("You got a quadruple bogey...")
    else:
        print(f"You completed the hole in {strokes} strokes.")

#print summary
print("\nYour game of golf is complete!")
print(f"The overall par: {total_par}")
print(f"Your total number of strokes: {total_strokes}")

#print how good they are at golf
if strokes<par:
    print("\nWow you are awesome at golf!")
elif stokres>par:
    print("\nOh... you're pretty bad at golf.")
else:
    print("\nWell you shot par, you're pretty average.")
