def count_words(filename):
    """Conta o número aproximado de palavras em um arquivo."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        pass
        #msg = "Sorry, the file " + filename + " does not exist."
        #print(msg)
    else:
        #Conta o número aproximado de palavras no arquivo
        words = contents.split()
        num_words = len(words)
        print("The file "+ filename + " has about "+str(num_words)+ " words.")
filename = 'alice.txt'
count_words(filename)