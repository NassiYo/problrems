def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return is_start_with_2letters(s) and is_appropriate_width(s) and is_appropriate_numbers_positions(s) and is_allowd_characters(s)



def is_start_with_2letters(s):
    return s[0:2].isalpha()

def is_appropriate_width(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def is_appropriate_numbers_positions(s):
    if len(s) > 2:
        s = s[2:len(s)]
        counter = 0
        answer = True
        for i in range(len(s) - 1):
            if s[i].isdecimal() and answer:
                if s[i] == "0" and counter == 0: return False
                answer = s[i:len(s)].isdecimal()
                counter += 1
        return answer
    else:
        return True

def is_allowd_characters(s):
    return s.isalnum()

main()
