import base64
import hashlib
import sys

g = 5
p = 23

a = 6
b = 15

A = (g**a) % p
B = (g**b) % p

print 'g: ', g,' (a shared value), n: ', p, ' (a prime number)'

print '\nAlice computes:'
print 'a (Alice random): ', a
print 'Alice value (A): ', A

print '\nBob computes:'
print 'b (Bob random): ', b
print 'Bob value (B): ', B

print '\nAlice computes:'
keyA = (B**a) % p
print 'Key: ', keyA
print 'Key: ', hashlib.sha256(str(keyA)).hexdigest()

print '\nBob computes:'
keyB = (A**b) % p
print 'Key: ', keyB
print 'Key: ', hashlib.sha256(str(keyB)).hexdigest()
