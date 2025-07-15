# A program that asks a series of questions to determine the type of animal that is required by the user
# Lehlogonolo Tshehla
# 02 March 2025

print("Welcome to the Biology Expert")
print("------------------------------------------------------------------")
print("Answer the following questions by selecting from among the options.")

backbone = input("Does the organism have a backbone? (yes/no):\n")
backbone = backbone.lower()

if backbone == "yes":
    blood = input("Is it warm-blooded? (yes/no):\n")
    blood = blood.lower()
    if blood == "yes":
        feathers = input("Does it have feathers? (yes/no):\n")
        feathers = feathers.lower()
        if feathers == "no":
            fur = input("Does it have fur? (yes/no):\n")
            fur = fur.lower()
            if fur == "yes":
                print("It is a Mammal.")
            else:
                print("It is Other Vertebrate")
        else:
            print("It is a Bird.")
    else:
        scales = input("Does it have scales? (yes/no):\n")
        scales = scales.lower()
        if scales == "yes":
            water = input("Does it live in water? (yes/no):\n")
            water = water.lower()
            if water == "yes":
                print("It is a Fish.")
            else:
                print("It is a Reptile.")
        else:
            print("It is an Amphibian.")
else:
    skeleton = input("Does it have an exoskeleton? (yes/no):\n")
    skeleton = skeleton.lower()
    if skeleton == "yes":
        legs = input("Does it have six legs? (yes/no):\n")
        legs = legs.lower()
        if legs == "no":
            legs_2 = input("Does it have eight legs? (yes/no):\n")
            legs_2 = legs_2.lower()
            if legs_2 == "yes":
                print("It is an Arachnid.")
            else:
                print("It is a Crustacean")
        else:
            print("It is an Insect.")
    else:
        body = input("Does it have a segmented body? (yes/no):\n")
        body = body.lower()
        if body == "no":
            shell = input("Does it have a shell? (yes/no):\n")
            shell = shell.lower()
            if shell == "yes":
                print("It is a Snail or Clam.")
            else:
                print("It is an Octopus or Squid.")
        else:
            print("It is an Annelid (e.g., Earthworm).")
