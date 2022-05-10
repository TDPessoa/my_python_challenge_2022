'''
A certain street has between 50 and 500 houses in a row, numbered 1, 2, 3, 4, … consecutively. There is a certain house
on the street such that the sum of all the house numbers to the left side of it is equal to the sum of all the house
numbers to its right. Find the number of this house.?
ie.
xh =  1 -  2 -  3 -  4 -  5 -  6 -  7 -  8 -  9 - 10 - 11
ls =  0 -  1 -  3 -  6 - 10 - 15 - 21 - 28 - 36 - 45 - 55
rs = 65 - 63 - 60 - 56 - 51 - 45 - 38 - 30 - 21 - 11 -  0
hr = 11 >>>
'''

#x_house, right_sum, left_sum, houses_range
xh, rs, ls, hr = 1, 0, 0, 50

while ( hr != 501 ):
    for grupo in range( hr + 1 ):
        print(grupo)
        for casa in range( hr + 1 ):
            print(f"\t{casa}")
            if ( casa < xh ):
                rs += casa
            elif ( casa > xh ):
                ls += casa
        if ( ls == rs ):
            print(f"A casa nº{xh} é válida se considerada no alcance de {grupo}")