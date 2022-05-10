import random

sgen = randon.randint(1-33000)

randon.seed(sgen)

char_list = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D',
 e, E, f, F, g, G, 
h, H, i, I, j, J, k, K, l, L, m, M, n, N, o, O, p, P, 
q, Q, r, R, s, S, t, T, u, U, v, V, w, W, x, X, y, Y, 
z, Z, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, @, #, $, &, _, -, 
(, ), =, %, ", *, ', :, /, !, ?, +, £, €, ¥, ¢, ©, ®, 
™, ~, ¿, [, ], {, }, <, >, ^, ¡, `, ;, ÷, \, |, ¦, ¬, 
×, §, ¶, °

entry = str(input('Entry:'))

for c in range( len( entry ) ) :
   
    