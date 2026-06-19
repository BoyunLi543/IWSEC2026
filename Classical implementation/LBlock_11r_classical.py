
import itertools
import time
import random
from tqdm import tqdm
import sys


S0 = [14, 9, 15, 0, 13, 4, 10, 11, 1, 2, 8, 3, 7, 6, 12, 5]
S1 = [4, 11, 14, 9, 15, 13, 0, 10, 7, 12, 5, 6, 2, 8, 1, 3]
S2 = [1, 14, 7, 12, 15, 13, 0, 6, 11, 5, 9, 3, 2, 4, 8, 10]
S3 = [7, 6, 8, 11, 0, 15, 3, 14, 9, 10, 12, 13, 5, 2, 4, 1]
S4 = [14, 5, 15, 0, 7, 2, 12, 13, 1, 8, 4, 9, 11, 10, 6, 3]
S5 = [2, 13, 11, 12, 15, 14, 0, 9, 7, 10, 6, 3, 1, 8, 4, 5]
S6 = [11, 9, 4, 14, 0, 15, 10, 13, 6, 12, 5, 7, 3, 8, 1, 2]
S7 = [13, 10, 15, 0, 14, 4, 9, 11, 2, 1, 8, 3, 7, 5, 12, 6]

query_num = 0

def F(input, round, tag, K0,K1,K2,K3,K4,K5,K6,K7):
    if tag == 0:
        output = S0[input^K0[round]]
    elif tag == 1:
        output = S1[input^K1[round]]
    elif tag == 2:
        output = S2[input^K2[round]]
    elif tag == 3:
        output = S3[input^K3[round]]
    elif tag == 4:
        output = S4[input^K4[round]]
    elif tag == 5:
        output = S5[input^K5[round]]
    elif tag == 6:
        output = S6[input^K6[round]]
    elif tag == 7:
        output = S7[input^K7[round]]
    else:
        print("error")
        output = 0
    return output

def ROUND(in0,in1,in2,in3,in4,in5,in6,in7,in8,in9,in10,in11,in12,in13,in14,in15,round, K0,K1,K2,K3,K4,K5,K6,K7):
    out0 = in10 ^ F(in1, round, 1, K0,K1,K2,K3,K4,K5,K6,K7)
    out1 = in11 ^ F(in3, round, 3, K0,K1,K2,K3,K4,K5,K6,K7)
    out2 = in12 ^ F(in0, round, 0, K0,K1,K2,K3,K4,K5,K6,K7)
    out3 = in13 ^ F(in2, round, 2, K0,K1,K2,K3,K4,K5,K6,K7)
    out4 = in14 ^ F(in5, round, 5, K0,K1,K2,K3,K4,K5,K6,K7)
    out5 = in15 ^ F(in7, round, 7, K0,K1,K2,K3,K4,K5,K6,K7)
    out6 = in8 ^ F(in4, round, 4, K0,K1,K2,K3,K4,K5,K6,K7)
    out7 = in9 ^ F(in6, round, 6, K0,K1,K2,K3,K4,K5,K6,K7)
    out8 = in0
    out9 = in1
    out10 = in2
    out11 = in3
    out12 = in4
    out13 = in5
    out14 = in6
    out15 = in7

    return out0,out1,out2,out3,out4,out5,out6,out7,out8,out9,out10,out11,out12,out13,out14,out15
    

def SINGLE_QUERY(ax0,ay0,ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,ax5,ay5,ax6,ay6,x):
    global query_num
    query_num += 2
    x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = c0, c1, c2, c3, ax0, ax1, ax2, c7, ax3, x, ax4, c11, ax5, c13, ax6, c15
    y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15 = c0, c1, c2, c3, ay0, ay1, ay2, c7, ay3, x, ay4, c11, ay5, c13, ay6, c15
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
    R = 11
    n = 4
    p = 12
    t1 = 0
    t2 = 4
    branch = 16
    end_pos = 8
    invalid = 0
    counter_s = 0
    TESTTIME = 2**p


    X = [[-1] * (2 ** n) for _ in range(branch)]
    Y = [[-1] * (2 ** n) for _ in range(branch)]
    XOR_XY = [[-1] * (2 ** n) for _ in range(branch)]


    for thistime in range(TESTTIME):
        check = True
        ax0, ax1, ax2, ax3, ax4, ax5, ax6, ax7 = [random.randint(0, 15) for i in range(8)]
        ay0 = ax0 ^ 0x1
        ay1 = ax1 ^ 0x1
        ay2 = ax2 ^ 0x6
        ay3 = ax3 ^ 0x1
        ay4 = ax4 ^ 0x2
        ay5 = ax5 ^ 0x4
        ay6 = ax6 ^ 0x1
        c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15 = [random.randint(0, 15) for i in
                                                                                range(16)]

        K0 = [random.randint(1, 15) for i in range(20)]
        K1 = [random.randint(1, 15) for i in range(20)]
        K2 = [random.randint(1, 15) for i in range(20)]
        K3 = [random.randint(1, 15) for i in range(20)]
        K4 = [random.randint(1, 15) for i in range(20)]
        K5 = [random.randint(1, 15) for i in range(20)]
        K6 = [random.randint(1, 15) for i in range(20)]
        K7 = [random.randint(1, 15) for i in range(20)]

        for xy in range(9):
            enc = SINGLE_QUERY(ax0,ay0,ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,ax5,ay5,ax6,ay6,xy)
            for d in range(branch):
                XOR_XY[d][xy] = enc[d]


        if len(set(XOR_XY[end_pos][:9:])) == 9:
            continue
        else:
            if XOR_XY[end_pos][8] not in XOR_XY[end_pos][:8:]:
                for z in range(1,8):
                    counter = 0
                    for x in range(8):
                        if XOR_XY[end_pos][x] == XOR_XY[end_pos][x^z]:
                            counter += 1
                    if counter == 8:
                        Q = []
                        for t in range(t1):
                            if check:
                                xt = random.randint(0, 7)
                                while xt in Q:
                                    xt = random.randint(0, 7)
                                enc = SINGLE_QUERY(ax0,ay0,ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,ax5,ay5,ax6,ay6, 8 + t)
                                XOR_XY[end_pos][8 + t] = enc[end_pos]
                                enc = SINGLE_QUERY(ax0,ay0,ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,ax5,ay5,ax6,ay6, (8 + t)^z)
                                XOR_XY[end_pos][(8 + t)^z] = enc[end_pos]
                                Q.append(xt)
                                if XOR_XY[end_pos][8+t] != XOR_XY[end_pos][(8 + t)^z]:
                                    check = False
                        if check:
                            print('period: %s, site %s' % (str(z), str(end_pos)))
                            print('query number:', query_num)
                            exit()



            else:
                for z in range(1,8):
                    counter = 0
                    for x in range(8):
                        if XOR_XY[end_pos][x] == XOR_XY[end_pos][x^z]:
                            counter += 1
                    if counter == 8:
                        Q = []
                        for t in range(t1):
                            if check:
                                xt = random.randint(0, 7)
                                while xt in Q:
                                    xt = random.randint(0, 7)
                                enc = SINGLE_QUERY(ax0,ay0,ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,ax5,ay5,ax6,ay6, 8 + t)
                                XOR_XY[end_pos][8 + t] = enc[end_pos]
                                enc = SINGLE_QUERY(ax0,ay0,ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,ax5,ay5,ax6,ay6, (8 + t)^z)
                                XOR_XY[end_pos][(8 + t)^z] = enc[end_pos]
                                Q.append(xt)
                                if XOR_XY[end_pos][8+t] != XOR_XY[end_pos][(8 + t)^z]:
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
                        S.append(i^8)
                for t in range(t2):
                    if check:
                        enc = SINGLE_QUERY(ax0,ay0,ax1,ay1,ax2,ay2,ax3,ay3,ax4,ay4,ax5,ay5,ax6,ay6, 8 + t + 1)
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


