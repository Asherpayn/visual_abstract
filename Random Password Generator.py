#Password Generator

from random import *
pcs = ["ab", "bc", "gd", "uh", "fd", "td", "te", "yg"]
pds = ["!", "£", "$", "%", "^", "&", "*", "(", ")", "@"]
pes = ["ab", "bc", "gd", "uh", "fd", "td", "te", "yg"]
print("Type \'new\' for a new password")
while True:
    parta = randint(0, 300)
    partb = randint(0, 300)
    partc = choice(pcs)
    partd = choice(pds)
    parte = choice(pes)
    input(">>> ")
    print(parta, partb, partc, partd, parte)


    
