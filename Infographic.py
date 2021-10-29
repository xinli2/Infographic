###
### Author: Xin Li
### Description:  In this programming assignment,
### i have wrote a program that reads in
### a text file (perhaps containing the contents
### of a book, poem, article, etc) and produces
### an infographic based on the text.
###
from graphics import graphics
def words_list():
    words=[]
    file_name = input('The file name:\n')
    file = open(file_name, 'r')
    lines = file.readlines()
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for word in line:
            words.append(word)
    return words, file_name

def count_words(words):
    dictionary = {}
    for word in words:
        if word in dictionary:
            dictionary[word] += 1
        else:
            dictionary[word] = 1
    if ''in dictionary:
        del dictionary['']
    return dictionary

def finding_most_occurrences(dictionary):
    small = 0
    medium = 0
    large = 0
    small_dictionary = {}
    medium_dictionary = {}
    large_dictionary = {}
    smallmost = ''
    mediummost = ''
    largemost =''
    for word in dictionary:
        if len(word) < 5:
            small += dictionary[word]
            small_dictionary[word]= dictionary[word]

        elif 4 <len(word) < 8:
            medium += dictionary[word]
            medium_dictionary[word] = dictionary[word]
        elif len(word) >= 8:
            large += dictionary[word]
            large_dictionary[word] = dictionary[word]
    smallcount = 0
    smallmost_word = ''
    for word in small_dictionary:
        if small_dictionary[word] > smallcount:
            smallcount = small_dictionary[word]
            smallmost_word = word
       # if small_dictionary[word] == smallcount and word not in smallmost_word:
        #    smallmost_word +=' '+word
    smallmost = smallmost_word+' ('+str(smallcount)+'x'+') '

    mediumcount  = 0
    mediummost_word = ''
    for word in medium_dictionary:
        if medium_dictionary[word] > mediumcount:
            mediumcount = medium_dictionary[word]
            mediummost_word = word
        #if medium_dictionary[word] == mediumcount and word not in mediummost_word:
         #   mediummost_word +=', '+word
    mediummost = mediummost_word+' ('+str(mediumcount)+'x'+') '

    largecount = 0
    largemost_word = ''
    for word in large_dictionary:
        if large_dictionary[word] > largecount:
            largecount = large_dictionary[word]
            largemost_word = word
        #if large_dictionary[word] == largecount and word not in largemost_word:
         #   largemost_word +=' '+word
    largemost = largemost_word+' ('+str(largecount)+'x'+') '
    small = len(small_dictionary)
    medium = len(medium_dictionary)
    large = len(large_dictionary)

    return small, medium, large, smallmost, mediummost, largemost

def counting_capitalized(dictionary):
    capitalized = 0
    non_capitalized = 0
    for word in dictionary:
        print('"' + word + '"')
        if word[0].isalpha() ==True:
            if word[0].isupper() == True:
                capitalized += 1
            else:
                non_capitalized += 1
    print(capitalized, non_capitalized)
    return capitalized, non_capitalized

def count_punctuated(dictionary):
    punctuated = 0
    non_punctuated = 0
    print(dictionary)
    for word in dictionary:
            if word[len(word)-1].isalnum() == True:
                non_punctuated += 1
            else:
                punctuated += 1
    print(punctuated, non_punctuated)
    return punctuated, non_punctuated

def draw_board(file_name, dictionary, smallmost, mediummost ,largemost, small, medium, large, capitalized, non_capitalized, punctuated, non_punctuated, gui):
    gui.rectangle(-10,-10 ,750 ,750, 'grey41')
    gui.text(50, 50, file_name, 'Cyan',25)
    gui.text(50, 100, 'Total Unique Words:'+str(len(dictionary)), 'white', 15)
    gui.text(50, 125, 'Most used words(s/m/l):', 'white', 10)
    gui.text(200, 125, smallmost+mediummost+largemost, 'Cyan',10)
    gui.text(50, 150,'Word Lengths', 'white', 20)
    gui.text(250, 150,'Cap/Non-Cap', 'white', 20)
    gui.text(450, 150,'Punct/Non-Punct', 'white', 20)

    #Word Lengths
    gui.rectangle(50, 200, 150, small*450 / (small+medium+large), 'DodgerBlue')
    gui.text(50,200,'small words', 'white', 10)
    gui.rectangle(50, 200+small*450 / (small+medium+large), 150, medium*450 / (small+medium+large), 'green')
    gui.text(50,200+small*450 / (small+medium+large),'medium words', 'white', 10)
    gui.rectangle(50, 200+small*450 / (small+medium+large)+medium*450 / (small+medium+large), 150, large*450 / (small+medium+large), 'DodgerBlue')
    gui.text(50,200+small*450 / (small+medium+large)+medium*450 / (small+medium+large),'large words', 'white', 10)

    #Cap/Non-Cap
    gui.rectangle(250, 200, 150, capitalized*450 / (capitalized+non_capitalized), 'DodgerBlue')
    gui.text(250,200,'Capitalized', 'white', 10)
    gui.rectangle(250, 200+capitalized*450 / (capitalized+non_capitalized), 150, non_capitalized*450 / (capitalized+non_capitalized), 'green')
    gui.text(250,200+capitalized*450 / (capitalized+non_capitalized),'Non Capitalized', 'white', 10)

    #Punct/Non-Punct
    gui.rectangle(450, 200, 150, punctuated*450 / (punctuated+non_punctuated), 'DodgerBlue')
    gui.text(450,200,'Punctuated', 'white', 10)
    gui.rectangle(450, 200+punctuated*450 / (punctuated+non_punctuated), 150, non_punctuated*450 / (punctuated+non_punctuated), 'green')
    gui.text(450,200+punctuated*450 / (punctuated+non_punctuated),'Non Punctuated', 'white', 10)



def main():
    gui = graphics(650, 700, 'Infographic')
    words, file_name = words_list()

    dictionary = count_words(words)
    small, medium, large, smallmost, mediummost, largemost = finding_most_occurrences(dictionary)
    capitalized, non_capitalized = counting_capitalized(dictionary)
    punctuated, non_punctuated = count_punctuated(dictionary)

    draw_board(file_name, dictionary, smallmost, mediummost ,largemost, small, medium, large, capitalized, non_capitalized, punctuated, non_punctuated, gui)
main()
