import itertools
import time
import random
from tqdm import tqdm


S = [0xC, 0x0, 0xF, 0xA, 0x2, 0xB, 0x9, 0x5, 0x8, 0x3, 0xD, 0x7, 0x1, 0xE, 0x6, 0x4]


def F(input, round, tag, K0,K1,K2,K3,K4,K5,K6,K7):
    if tag == 0:
        output = S[input^K0[round]]
    elif tag == 1:
        output = S[input^K1[round]]
    elif tag == 2:
        output = S[input^K2[round]]
    elif tag == 3:
        output = S[input^K3[round]]
    elif tag == 4:
        output = S[input^K4[round]]
    elif tag == 5:
        output = S[input^K5[round]]
    elif tag == 6:
        output = S[input^K6[round]]
    elif tag == 7:
        output = S[input^K7[round]]
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
    

if __name__ == '__main__':
    R = 9
    end_pos = 5
    invalid = 0
    counter_s = 0
    TESTTIME = 2**4

    X0,X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15 = [-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16
    Y0,Y1,Y2,Y3,Y4,Y5,Y6,Y7,Y8,Y9,Y10,Y11,Y12,Y13,Y14,Y15 = [-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16
    f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15 = [-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16,[-1]*16


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
        ax0,ax1,ax2,ax3,ax4 = [0 for i in range(5)]
        ay0,ay1,ay2,ay3,ay4 = [0 for i in range(5)]
        while ax0 == ay0 or ax1 == ay1 or ax2 == ay2 or ax3 == ay3 or ax4 == ay4:
            ax0, ax1, ax2, ax3, ax4 = [random.randint(0, 15) for i in range(5)]
            ay0, ay1, ay2, ay3, ay4 = [random.randint(0, 15) for i in range(5)]

        for order in range(1):
            for xy in range(16):
                x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15 = c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,ax0,xy,c12,c13,c14,c15
                y0, y1, y2, y3, y4, y5, y6, y7, y8, y9, y10, y11, y12, y13, y14, y15 = c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,ay0,xy,c12,c13,c14,c15
                for r in range(R):
                    x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15 = ROUND(x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15,r, K0,K1,K2,K3,K4,K5,K6,K7)
                    y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15 = ROUND(y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,r, K0,K1,K2,K3,K4,K5,K6,K7)

                X0[xy],X1[xy],X2[xy],X3[xy],X4[xy],X5[xy],X6[xy],X7[xy],X8[xy],X9[xy],X10[xy],X11[xy],X12[xy],X13[xy],X14[xy],X15[xy] = x0,x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13,x14,x15
                Y0[xy],Y1[xy],Y2[xy],Y3[xy],Y4[xy],Y5[xy],Y6[xy],Y7[xy],Y8[xy],Y9[xy],Y10[xy],Y11[xy],Y12[xy],Y13[xy],Y14[xy],Y15[xy] = y0,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15

            for i in range(16):
                f0[i],f1[i],f2[i],f3[i],f4[i],f5[i],f6[i],f7[i],f8[i],f9[i],f10[i],f11[i],f12[i],f13[i],f14[i],f15[i] = X0[i]^Y0[i],X1[i]^Y1[i],X2[i]^Y2[i],X3[i]^Y3[i],X4[i]^Y4[i],X5[i]^Y5[i],X6[i]^Y6[i],X7[i]^Y7[i],X8[i]^Y8[i],X9[i]^Y9[i],X10[i]^Y10[i],X11[i]^Y11[i],X12[i]^Y12[i],X13[i]^Y13[i],X14[i]^Y14[i],X15[i]^Y15[i]

            F_end = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13,f14,f15]
            for s in range(1,16):
                counter = 0
                for x in range(16):
                    if F_end[end_pos][x] == F_end[end_pos][x^s]:
                        counter += 1

                if counter == 16:
                    print('period: %s, site %s' % (str(s), str(end_pos)))
                    counter_s += 1
                    break

    print('success', counter_s/TESTTIME)

