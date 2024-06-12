print('data type')
def datatypefunc():
    print(10)
    print(-10)
    print(1.000332)
    print(1.3434)
    complex_data = complex(0,2)
    print(complex_data)
    tf_bool = True
    print(tf_bool)
    print("Harry_potter")
    print('game of thrones')
    empty =""
    print(empty)
    multiple_lines ='''Triple quotes 
    for multiple lines'''
    print(multiple_lines)
    print(len(multiple_lines))
    batman ='Bruce Wayne'
    first = batman[0]
    print(first)
    last = batman[len(batman)-1]
    print(last)
    print(batman[-1])
    print(batman[-2])
    string ="Immutability"
    # string[0] = '1'
    str1 = 'hello'
    print(id(str1))
    str2 ='world'
    print(id(str2))
    unicodestring = u"This is unicode"
    print(unicodestring)
    my_string = 'This is MY string'
    print(my_string[0:4])
    print(my_string[1:2])
    print(my_string[8:len(my_string)])
    print(my_string[0:7:3])
    print(my_string[13:2:-2])
    print(my_string[::-1])
datatypefunc()
