
### Übung ###

erst_summand = int(input("Deine Erste Zahl"))
zwei_summand = int(input("Deine Zweite Zahl"))
rech_art = (input("Rechenart [Mal, Geteilt, Plus, Minus]")).lower()


### Main Programm ###
if rech_art == "mal":
    print(float(erst_summand * zwei_summand))
elif rech_art == "geteilt":
    print(float(erst_summand / zwei_summand))
elif rech_art == "plus":
    print(float(erst_summand + zwei_summand))
elif rech_art == "minus":
    print(float(erst_summand - zwei_summand))
else:
    print("Error!")
