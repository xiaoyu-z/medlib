#!/usr/bin/python

import cgitb                      # Always remember to do this first.
cgitb.enable()

import cgi
form = cgi.FieldStorage()
page = 0
sentence_data = ['The NOUN had to VERB the ADJ thing','I hate the ADJ NOUN','You should VERB the ADJ dog','The NOUN and NOUN are all ADJ','We should VERB the NOUN ADV']


def printCategory(category):
    '''return the HTML of input page
    '''
    str ='''<form action="medlib.cgi">'''
    for i in category:
        str += categoryHTML(i)
    return str+hiddenHTML(page)+'''<input type=submit value="Okay."></form>'''
def checkInput(replaceList,sentence_category):
    '''check weather the input is correct or wrong
       >>> checkInput([['ADJ','cute'],['NOUN','dog']],['ADJ','NOUN'])
       True
    '''
    for i in range(len(replaceList)-1):
        for j in replaceList[i]:
            if sum(k.isalpha() for k in j)!=len(j) or not j:
                return False
    replace_category = [i[0] for i in replaceList]
    for i in sentence_category:
        if i not in replace_category:
            return False
    return True

def hiddenHTML(pageNum):
    '''return th hidden HTML statement
    >>> hiddenHTML(3)
    '<input type=hidden name = page value = 4>'
    '''
    return '''<input type=hidden name = page value = '''+ str(pageNum+1)+'''>'''

def categoryHTML(category):
    '''
    return the category HTML statment
    >>> categoryHTML('NOUN')
    'input NOUN<input type=text name=NOUN><br>'
    '''
    if category=='NOUN':
        return '''input NOUN<input type=text name=NOUN><br>'''
    if category=='ADV':
        return '''input ADVERB<input type=text name=ADV><br>'''
    if category=='ADJ':
        return '''input ADJECTIVE<input type=text name=ADJ><br>'''
    if category=='VERB':
        return '''input VERB<input type=text name=VERB><br>'''
    return ''''''

def pringBasic():
    print 'Content-Type: text/html'
    print

def getALLcategory(sentence):
    ''':return: the category list
    >>> getALLcategory('The NOUN had to VERB the ADJ thing')
    ['NOUN', 'VERB', 'ADJ']
    '''
    category = ['NOUN','VERB','ADJ','ADV']
    sentence_category = []
    words = sentence.strip().split(' ')
    for word in words:
        if word in category:
            sentence_category.append(word)
    return sentence_category
def printSentence(replaceList, sentence):
    '''replace the sentence
    >>> printSentence([['ADJ','cute']],'I like the ADJ dog')
    'I like the cute dog'
    '''
    result_sentence = sentence
    for i in replaceList:
        for j in range(len(i)-1):
            result_sentence = result_sentence.replace(i[0],i[j+1],1)
    return result_sentence
try:
    page = int(form['page'].value) % (2*len(sentence_data))
except:pass
#print printCategory(['ADJ'])
pringBasic()
import doctest
doctest.testmod()

if page%2==0:
    print printCategory(getALLcategory(sentence_data[page/2]))

else:
    #print [[i]+form.getlist(i) for i in form.keys()]
    input = [[i]+form.getlist(i) for i in form.keys()]
    if checkInput(input,getALLcategory(sentence_data[(page-1)/2])):
        print printSentence([[i]+form.getlist(i) for i in form.keys()], sentence_data[(page-1)/2])
        print "<br>Try another one<br>"
        print printCategory([])
    else:
        print "<br>Error Input, retry another one<br>"
        print printCategory([])

