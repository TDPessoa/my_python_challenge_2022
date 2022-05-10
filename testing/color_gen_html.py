import time

r, g, b, count, count_lines, code_html, epoch_init, x= 0, 0, 0, 0, 0, '\n', time.time(), 1

for r in range ( 0, 256 ):

    for g in range ( 0, 256 ):

        '''if ( count_lines % 70 == 0 ):
            
            print(200 * '-', '\n', code_html, '\n', 200 * '-')
            while True:
            
                print('waiting')
                x = int(input())
                break'''
        count_lines += 1
        for b in range ( 0, 256 ):

            count +=1
            count_str = str(count)
            code_html += '<p style= "color: rgb('
            letter_r = str(r)
            code_html += letter_r
            code_html += ','
            letter_g = str(g)
            code_html += letter_g
            code_html += ','
            letter_b = str(b)
            code_html += letter_b
            code_html += ');">'
            code_html += "cor "
            code_html += count_str
            code_html += " "
            code_html += letter_r
            code_html += ','
            code_html += letter_g
            code_html += ','
            code_html += letter_b
            code_html += '</p>\n'
    epoch_fnal = (time.time() - epoch_init)//1
    if ( epoch_fnal < 60):

        print( f'{ r + 1 }/256 completed and { epoch_fnal:.0f } seconds passed.')
    elif ( epoch_fnal > 60 and epoch_fnal < 3600):

        print( f'{ r + 1 }/256 completed and { epoch_fnal // 60:.0f } minutes and { epoch_fnal % 60:.0f } seconds passed.')
    elif ( epoch_fnal >= 3600 ):

        print(f'{ r + 1 }/256 completed and { epoch_fnal // 3600:.0f } hours,  { (epoch_fnal - epoch_fnal//3600) // 60:.0f } minutes and'
              f' { epoch_fnal % 60:.0f } seconds passed.')
print( 200 * '-', '\n', code_html, '\n', 200 * '-')