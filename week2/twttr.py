def twttr():
    '''Remove vowels from a string and return the modified string. '''
    user=input("Input: ")
    vowel='aeiouAEIOU'
    for i in user:
        if i not in vowel:
            print(i, end="")
            
twttr()