import hashlib

key = 'ckczppom'
guess = 0

teststring = key + str(guess)

while hashlib.md5(teststring).hexdigest()[:5] != '00000':
    guess += 1
    teststring = key + str(guess)

print 'Part 1: ', guess
print '-----' * 8

guess = 0
teststring = key + str(guess)
while hashlib.md5(teststring).hexdigest()[:6] != '000000':
    guess += 1
    teststring = key + str(guess)

print 'Part 1: ', guess
