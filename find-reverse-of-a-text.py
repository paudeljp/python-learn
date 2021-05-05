def reverse (input):
    string = ""
    length = len (input) - 1
    while length >= 0:
        string = string + input [length]
        length = length -1
    return string

str_data = 'Sabita Neupane'

if __name__ == "__main__":
    print ('Reverse =', reverse(str_data))
