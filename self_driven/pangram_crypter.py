import random

string = 'thequickbrownfoxjumpsoveralazydog'
code_string = '0t0h0e0q0u0i0c0k0b0r0o0w0n0f0o0x0j0u0m0p0s0o0v0e0r0a0l0a0z0y0d0o0g'
code = []
check = ['a']
count = 0

for i in range (len(string)+1):

    while True:
        letter = random.randint(0, len(string)+1)

        while count == 0:
            for c in range(len(check)):
                if check[c] != letter:
                    count +=1

                if count == len(check):
                    print('OK')
                    if ( letter <= 9 ):
                        code += str(0)
                    check.append(str(letter))
                    break
    code += str(letter)

print (code)
print (code_string)