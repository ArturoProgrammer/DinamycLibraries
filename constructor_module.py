# -*- coding: utf-8 -*-

file = open("data_to_structure.cache", "r+")


BUFFER = []

for i in file.readlines():
    print(i)
    counter = 0
    before  = 0
    after   = 2

    for pair in i:
        counter += 1

        if counter == 2:
            print(i[before:after])
            after += 2

file.close()
