##find readme below

class ECC:
    def __init__(self,a,b,p):
        self.a = a 
        self.b = b
        self.p = p
        self.zero=(0,0)
        self.na=41
        self.nb=101
        print(" a = ",a)
        print(" b = ",b)
        print(" p = ",p)
        print(" A's private key : ",self.na)
        print(" B's private key : ",self.nb)

        
    def eqRHS(self,x):
        return (pow(x,3)+self.a*x+self.b)%self.p
    
    def isPoint(self,x,y):
        if((y*y)%self.p == self.eqRHS(x)):
            return True
        else: 
            return False

    def inverse(self,x,p):
        """div on PN modulo a/b mod q as a * inv(b, q) mod q >>> assert n * inv(n, q) % q == 1"""
        for i in range(p):
            if (x * i) % p == 1:
                # print(i,"invv ",x)
                return i
        return p

    def addPoints(self,p,q):
        if p == self.zero: return q
        if q == self.zero: return p

        if p[0] == q[0] and (p[1] != q[1] or p[1] == 0):
            # p + -p == 0
            return self.zero

        if p[0] == q[0]:
            # p + p: use tangent line of p as (p,p) line
            l = (3 * p[0] * p[0] + self.a) * self.inverse(2 * p[1], self.p) % self.p
            
        else:
            l = (q[1] - p[1]) * self.inverse(q[0] - p[0], self.p) % self.p

        x = (l * l - p[0] - q[0]) % self.p
        y = (l * (p[0] - x) - p[1]) % self.p
        return (x,y)
       

    def allPoints(self):
        res=list()
        for y in range(self.p):
            for x in range(self.p):
                if(self.isPoint(x,y)):
                    # print("[",x,",",y,"]")
                    res.append((x,y))
        return res
    
    def mul(self,na,g):
        res=g
        for _ in range(na-1):
            res= self.addPoints(res,g)
        return res

    def encrypt(self,g,m):
        pa = self.mul(self.na,g) #kg
        pb= self.mul(self.nb,g)
        kpb= self.mul(self.na,pb)
        c1=self.addPoints(m,kpb)
        enc=[pa,c1]
        return enc

    def decrypt(self,c):
        c1,c2 = c
        c1 = self.mul(self.nb,c1)
        c1=list(c1)
        c1[1] = -c1[1]
        c1=tuple(c1)
        m = self.addPoints(c1,c2)
        return m

    
e = ECC(0,-4,257)

print(e.allPoints())

x1,y1=input("enter point a for addition \n").split(' ')
x2,y2=input("enter point b for addition \n").split(' ')
x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
point = e.addPoints((x1,y1),(x2,y2))
print(point)
print(point," ",point in e.allPoints())



#(52,194)
cipher = e.encrypt((2,2),(112,26))
print("cipher ", cipher)
plain = e.decrypt(cipher)
print("plain ",plain)

######*********README
# for the experiment I have written a class which takes a,b,p as parameters for the equation
# and values set according to test case which is:
#  a =  0
#  b =  -4
#  p =  257
#  A's private key :  41
#  B's private key :  101

# The ecc api has following functions
# isPoint(X)  //checks if the point x lies on the ecc
# addPoints(X,Y) // adds to valid points to return resultant valid point
# allPoints() // all valid points of the EC
# encrypt(generator,message) //return the cipher list
# decrypt(cipher) //returns the message

# allPoints:
# [(64, 0), (210, 1), (2, 2), (100, 3), (76, 4), (52, 5), (163, 6), (164, 7), 
# (137, 8), (56, 9), (200, 10), (5, 11), (90, 12), (185, 13), (49, 14), (10, 15), (147, 16), 
# (59, 17), (245, 18), (192, 19), (45, 20), (170, 21), (29, 22), (171, 23), (97, 24), (161, 25), 
# (112, 26), (83, 27), (223, 28), (53, 29), (158, 30), (188, 31), (0, 32), (183, 33), (252, 34), 
# (177, 35), (30, 36), (23, 37), (214, 38), (34, 39), (84, 40), (122, 41), (139, 42), (233, 43),
#  (13, 44), (254, 45), (4, 46), (231, 47), (47, 48), (169, 49), (160, 50), (176, 51), (75, 52), 
#  (63, 53), (127, 54), (155, 55), (80, 56), (234, 57), (3, 58), (178, 59), (109, 60), (179, 61),
#  (217, 62), (221, 63), (101, 64), (44, 65), (236, 66), (99, 67), (249, 68), (36, 69), (226, 70), 
#  (70, 71), (218, 72), (253, 73), (243, 74), (104, 75), (219, 76), (165, 77), (19, 78), (203, 79), 
#  (31, 80), (213, 81), (11, 82), (246, 83), (68, 84), (20, 85), (93, 86), (60, 87), (174, 88), 
#  (9, 89), (197, 90), (143, 91), (157, 92), (201, 93), (149, 94), (15, 95), (129, 96), (202, 97), 
#  (113, 98), (51, 99), (86, 100), (125, 101), (225, 102), (150, 103), (228, 104), (92, 105), 
#  (120, 106), (126, 107), (82, 108), (69, 109), (153, 110), (117, 111), (216, 112), (54, 113),
#   (229, 114), (141, 115), (55, 116), (42, 117), (61, 118), (17, 119), (156, 120), (193, 121),
#    (168, 122), (240, 123), (94, 124), (39, 125), (24, 126), (159, 127), (136, 128), (136, 129), 
#    (159, 130), (24, 131), (39, 132), (94, 133), (240, 134), (168, 135), (193, 136), (156, 137), 
#    (17, 138), (61, 139), (42, 140), (55, 141), (141, 142), (229, 143), (54, 144), (216, 145), 
#    (117, 146), (153, 147), (69, 148), (82, 149), (126, 150), (120, 151), (92, 152), (228, 153), 
#    (150, 154), (225, 155), (125, 156), (86, 157), (51, 158), (113, 159), (202, 160), (129, 161),
#     (15, 162), (149, 163), (201, 164), (157, 165), (143, 166), (197, 167), (9, 168), (174, 169),
#      (60, 170), (93, 171), (20, 172), (68, 173), (246, 174), (11, 175), (213, 176), (31, 177),
#     (203, 178), (19, 179), (165, 180), (219, 181), (104, 182), (243, 183), (253, 184), (218, 185),
#     (70, 186), (226, 187), (36, 188), (249, 189), (99, 190), (236, 191), (44, 192), (101, 193),
#      (221, 194), (217, 195), (179, 196), (109, 197), (178, 198), (3, 199), (234, 200), (80, 201), (155, 202), (127, 203), (63, 204), (75, 205), (176, 206), (160, 207), (169, 208), (47, 209), (231, 210), (4, 211), (254, 212), (13, 213), (233, 214), (139, 215), (122, 216), (84, 217), (34, 218), (214, 219), (23, 220), (30, 221), (177, 222), (252, 223), (183, 224), (0, 225), (188, 226), (158, 227), (53, 228), (223, 229),
#      (83, 230), (112, 231), (161, 232), (97, 233), (171, 234), (29, 235), (170, 236), (45, 237), (192, 238),
#      (245, 239), (59, 240), (147, 241), (10, 242), (49, 243), (185, 244), (90, 245), (5, 246), (200, 247), (56, 248), (137, 249), (164, 250), (163, 251), (52, 252), (76, 253), (100, 254), (2, 255), (210, 256)]

# addPoints:
#     enter point a for addition 
#     246 174
#     enter point a for addition 
#     68 -84
# result:
#     (112, 26)

# cipher return by encrypt:
#     cipher  [(136, 128), (246, 174)]

# plain message returned by decrypt:
#     plain  (112, 26)