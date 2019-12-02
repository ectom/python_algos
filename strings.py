def remove_blanks(string):
    newstr = ''
    for i in string:
        if i != ' ':
            newstr += i
    print(newstr)


def get_digits(string):
    newstr = ''
    for i in string:
        if i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
            newstr += i
    print(newstr)


def acronyms(string):
    newstr = ''
    prev_blank = True
    for i in string:
        if prev_blank and i != ' ':
            newstr += i.upper()
            prev_blank = False
        if not prev_blank and i == ' ':
            prev_blank = True
    print(newstr)


def count_non_spaces(string):
    count = 0
    for i in string:
        if i != ' ':
            count += 1
    print(count)


def reverse_string(string):
    newstr = ''
    i = 1
    while i <= len(string):
        newstr += string[-i]
        i += 1
    print(newstr)



remove_blanks('Pla   yTh a  t Fun   kyMu si c  ')
get_digits('1u3h645o592t3ug3jt9u3u')
acronyms(' thew\'s no free lunch - gotta pay yer way')
count_non_spaces('Honey pie, you are driving me crazy')
reverse_string('creature')
