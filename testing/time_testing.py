import time

init_time = time.time()

x, y_a, y_b, r = 0, 1, 1, 0

for r in range ( 0, 999999 ):

    r += 1
    elap_time = (time.time() - init_time + r ) // 1
    if (elap_time < 60):

        print(f'{r + 1}/1000000 completed \n {elap_time:.0f} seconds passed.')
    elif (elap_time > 60 and elap_time < 3600):

        print(f'{r + 1}/1000000 completed \n {elap_time // 60:.0f} minutes and {elap_time % 60:.0f} seconds passed.')
    elif (elap_time >= 3600):
        elap_time_h = elap_time // 3600
        elap_time_m = elap_time % 3600
        print(
            f'{r + 1}/1000000 completed \n {elap_time // 3600:.0f} hours,  {(elap_time - (elap_time // 3600)) // 60:.0f} minutes and {elap_time % 60:.0f} seconds passed.')
    print(time.ctime(elap_time))