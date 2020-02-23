# An API for  Elliptical Curve Cryptography arithmetic to implement Public Key Crytography
This project implements Elliptical Curve Cryptography. It provides you with an API to perform basic ECC arithmetic. ECC arithmetic here is used for public key cryptography a  assignment

ECC equation:
<p align="left">
<img src="https://github.com/aijax5/ecc-arithmetic/blob/master/ecc-eq.png" width="20%">
</p>

for the experiment I have written a class which takes a,b,p as parameters for the equation
and values set according to test case which is:
a =  0
b =  -4
p = 
A's private key -> pa
B's private key -> pb

The ecc api has following functions
isPoint(X)  //checks if the point x lies on the ecc
addPoints(X,Y) // adds to valid points to return resultant valid point
allPoints() // all valid points of the EC
encrypt(generator,message) //return the cipher list
decrypt(cipher) //returns the message


references:
  1) Network Security and Cryptography - William Stallings
  2) www.johannes-bauer.com/compsci/ecc/ 
