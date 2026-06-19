import itertools
import time
import random
from tqdm import tqdm
import sys


Sbox = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]

query_num = 0


def F(input, round, tag, K0,K1,K2,K3,K4,K5,K6,K7):
    if tag == 0:
        output = Sbox[input^K0[round]]
    elif tag == 1:
        output = Sbox[input^K1[round]]
    elif tag == 2:
        output = Sbox[input^K2[round]]
    elif tag == 3:
        output = Sbox[input^K3[round]]
    elif tag == 4:
        output = Sbox[input^K4[round]]
    elif tag == 5:
        output = Sbox[input^K5[round]]
    elif tag == 6:
        output = Sbox[input^K6[round]]
    elif tag == 7:
        output = Sbox[input^K7[round]]
    else:
        print("error")
        output = 0
    return output

def ROUND(in0,in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15,round, K0,K1,K2,K3,K4,K5,K6,K7):
    out0 = in1 ^ F(in0, round, 0, K0,K1,K2,K3,K4,K5,K6,K7)
    out1 = in2
    out2 = in11 ^ F(in10, round, 5, K0,K1,K2,K3,K4,K5,K6,K7)
    out3 = in6
    out4 = in3 ^ F(in2, round, 1, K0,K1,K2,K3,K4,K5,K6,K7)
    out5 = in0
    out6 = in9 ^ F(in8, round, 4, K0,K1,K2,K3,K4,K5,K6,K7)
    out7 = in4
    out8 = in7 ^ F(in6, round, 3, K0,K1,K2,K3,K4,K5,K6,K7)
    out9 = in10
    out10 = in13 ^ F(in12, round, 6, K0,K1,K2,K3,K4,K5,K6,K7)
    out11 = in14
    out12 = in5 ^ F(in4, round, 2, K0,K1,K2,K3,K4,K5,K6,K7)
    out13 = in8
    out14 = in15 ^ F(in14, round, 7, K0,K1,K2,K3,K4,K5,K6,K7)
    out15 = in12

    return out0,out1,out2,out3,out4,out5,out6,out7,out8,out9,out10,out11,out12,out13,out14,out15
    

def SINGLE_QUERY(ax0,ay0,x):
    global query_num
    query_num += 2
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, ax0, x, c12, c13, c14, c15
    y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15 = c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, ay0, x, c12, c13, c14, c15
    for r in range(R):
        x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = ROUND(x0, x1, x2, x3, x4, x5, x6, x7, x8,
                                                                                     x9, x10, x11, x12, x13, x14, x15,
                                                                                     r, K0, K1, K2, K3, K4, K5, K6, K7)
        y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15 = ROUND(y0, y1, y2, y3, y4, y5, y6, y7, y8,
                                                                                     y9, y10, y11, y12, y13, y14, y15,
                                                                                     r, K0, K1, K2, K3, K4, K5, K6, K7)

    res = [x0^y0,x1^y1,x2^y2,x3^y3,x4^y4,x5^y5,x6^y6,x7^y7,x8^y8,x9^y9,x10^y10,x11^y11,x12^y12,x13^y13,x14^y14,x15^y15]
    return res


if __name__ == '__main__':
    R = 9
    n = 4
    p = 0
    t1 = 0
    t2 = 1
    branch = 16
    end_pos = 5
    invalid = 0
    counter_s = 0
    TESTTIME = 2**p

    X = [[-1] * (2 ** n) for _ in range(branch)]
    Y = [[-1] * (2 ** n) for _ in range(branch)]
    XOR_XY = [[-1] * (2 ** n) for _ in range(branch)]

    c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,c11,c12,c13,c14,c15 = [random.randint(0,15) for i in range(16)]


    K0 = [random.randint(1, 15) for i in range(20)]
    K1 = [random.randint(1, 15) for i in range(20)]
    K2 = [random.randint(1, 15) for i in range(20)]
    K3 = [random.randint(1, 15) for i in range(20)]
    K4 = [random.randint(1, 15) for i in range(20)]
    K5 = [random.randint(1, 15) for i in range(20)]
    K6 = [random.randint(1, 15) for i in range(20)]
    K7 = [random.randint(1, 15) for i in range(20)]

    for thistime in range(TESTTIME):
        check = True
        ax0,ax1,ax2,ax3,ax4 = [0 for i in range(5)]
        ay0,ay1,ay2,ay3,ay4 = [0 for i in range(5)]
        while ax0 == ay0 or ax1 == ay1 or ax2 == ay2 or ax3 == ay3 or ax4 == ay4:
            ax0, ax1, ax2, ax3, ax4 = [random.randint(0, 15) for i in range(5)]
            ay0, ay1, ay2, ay3, ay4 = [random.randint(0, 15) for i in range(5)]

        for xy in range(9):
            enc = SINGLE_QUERY(ax0, ay0, xy)
            for d in range(branch):
                XOR_XY[d][xy] = enc[d]


        if len(set(XOR_XY[end_pos][:9:])) == 9:
            continue
        else:
            if XOR_XY[end_pos][8] not in XOR_XY[end_pos][:8:]:
                for z in range(1, 8):
                    counter = 0
                    for x in range(8):
                        if XOR_XY[end_pos][x] == XOR_XY[end_pos][x ^ z]:
                            counter += 1
                    if counter == 8:
                        Q = []
                        for t in range(t1):
                            if check:
                                xt = random.randint(0, 7)
                                while xt in Q:
                                    xt = random.randint(0, 7)
                                enc = SINGLE_QUERY(ax0, ay0, 8 + xt)
                                XOR_XY[end_pos][8 + xt] = enc[end_pos]
                                enc = SINGLE_QUERY(ax0, ay0, (8 + xt)^z)
                                XOR_XY[end_pos][(8 + xt)^z] = enc[end_pos]
                                Q.append(xt)
                                if XOR_XY[end_pos][8+xt] != XOR_XY[end_pos][(8 + xt)^z]:
                                    check = False
                        if check:
                            print('period: %s, site %s' % (str(z), str(end_pos)))
                            print('query number:', query_num)
                            exit()


            else:
                for z in range(1, 8):
                    counter = 0
                    for x in range(8):
                        if XOR_XY[end_pos][x] == XOR_XY[end_pos][x ^ z]:
                            counter += 1
                    if counter == 8:
                        Q = []
                        for t in range(t1):
                            if check:
                                xt = random.randint(0, 7)
                                while xt in Q:
                                    xt = random.randint(0, 7)
                                enc = SINGLE_QUERY(ax0, ay0, 8 + xt)
                                XOR_XY[end_pos][8 + xt] = enc[end_pos]
                                enc = SINGLE_QUERY(ax0, ay0, (8 + xt)^z)
                                XOR_XY[end_pos][(8 + xt)^z] = enc[end_pos]
                                Q.append(xt)
                                if XOR_XY[end_pos][8+xt] != XOR_XY[end_pos][(8 + xt)^z]:
                                    check = False

                        if check:
                            print('period: %s, site %s' % (str(z), str(end_pos)))
                            print('query number:', query_num)
                            exit()

                d = 0
                S = []
                for i in range(8):
                    if XOR_XY[end_pos][i] == XOR_XY[end_pos][8]:
                        d += 1
                        S.append(i ^ 8)
                for t in range(t2):
                    if check:
                        enc = SINGLE_QUERY(ax0, ay0, 8 + t + 1)
                        XOR_XY[end_pos][8 + t + 1] = enc[end_pos]
                        for s in S:
                            if XOR_XY[end_pos][8 + t] != XOR_XY[end_pos][(8 + t) ^ s]:
                                S.remove(s)
                        if len(S) == 0:
                            check = False
                if len(S) > 0:
                    for z in S:
                        print('period: %s, site %s' % (str(z), str(end_pos)))
                    print('query number:', query_num)
                    exit()



