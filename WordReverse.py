
'''This program will reverse words from a text file.
Provide the program with a text file in the same dir,
then this will create an output.txt file in the same dir.'''

with open(input("Please enter the filename you wish to use.\nUse just the full filename.\nFilename: "), encoding='utf-8') as input_file:
    in_words = input_file.read()
    print(in_words)
    in_words = in_words.replace('\n', ' \n ')
    symbol_list = ['.', ',', '!', '?', ':', ';', '@', '$', '&']
    for c in in_words:
        if c in symbol_list:
            in_words = in_words.replace(c, ' ' + c)
    spl = in_words.split(' ')
    out_words = ['']
    for word in spl:
        out_words.insert(0, word)
        out_words.insert(0, ' ')
    out_sentance = ''.join(out_words)
    with open('output.txt', mode='w', encoding='utf-8') as output_file:
        output_file.write(out_sentance)
