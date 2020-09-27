def program(r0):
    r3 = 2**16
    r1 = 10905776

    while(True):
        r1 = (((r1 + (r3 % 2**8)) % 2**24) * 65899) % 2**24

        if 2**8 > r3:
            if r1 == r0:
                print("HALT")
                break
            else:
                r3 = r1 | 2**16
                r1 = 10905776

        else:
            r3 //= 2**8

def mostInstructions():
    r1s = set()

    r3 = 2**16
    r1 = 10905776

    while(True):
        r1 = (((r1 + (r3 % 2**8)) % 2**24) * 65899) % 2**24

        if 2**8 > r3:
            if r1 in r1s:
                print("DONE")
                break
            else:
                print(r1)

                r1s.add(r1)

                r3 = r1 | 2**16
                r1 = 10905776

        else:
            r3 //= 2**8

program(4667)
mostInstructions()
