import os

if __name__ == '__main__':
    file = open("ejemplo2.dla", "r")
    f_content = file.readlines()

    for a_line in f_content:
        a_line = a_line.lstrip()
        print(a_line[:1])

        if a_line[:13] == "@[referential":
            ref_value = a_line[17:-5]
            print(ref_value)
