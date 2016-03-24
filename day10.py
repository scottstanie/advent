
def look_and_say(string):
    current = string[0]
    new_output = ''
    count = 1
    for letter in string[1:]:
        if current == letter:
            count += 1
        else:
            new_output += '%s%s' % (str(count), current)
            current = letter
            count = 1

    new_output += '%s%s' % (str(count), current)
    return new_output


if __name__ == '__main__':
    string = '1113122113'
    print 'Start: ', string

    for iterations in xrange(50):
        string = look_and_say(string)

    print len(string)
