#zelle 5.11.4 acronym

def main():
    word = input('word: ')

    wordList = word.split()

    acr = ""
    
    for w in wordList:
        acr += w[0]

    print(acr.upper() )

main()
