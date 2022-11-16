import contractions
import string #about strings
import re #for regular expression

def clean_text(text):
    text = contractions.fix(text)
    print(text)

    #transform to lower case
    text = text.lower()
    print(text)

    #look at the text and removes puntuations in text
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)

    #find and remove a numbers in the string -->regex101.com --> '\w*\d\w*'
    text = re.sub(r'\w*\d\w*', '', text)
    print(text)

    #read a text and make a list out of it --> 'r' means read
    #stopwords is file located in nov14 folder
    #strip() removes white space and backslash before and after the words 
    """
    stopwords = []
      for word in open('./stopwords_en.txt', 'r'):
        stopwords.append(word.strip())
        print(stopwords)

        this can be re-written as below:
    """
    stopwords = [word.strip() for word in open('./stopwords_en.txt', 'r')]
    print(stopwords)

    #find words inside words basically filter words in stopwords list
    text = ' '.join([word for word in text.split() if word not in stopwords])
    print(text)

    return text

def main():
    text = "I read this book for the first time in 1987, and it's one of my favorites!"
    print(clean_text(text))
    #print(contractions.fix(text))

if __name__ == '__main__':
    main()