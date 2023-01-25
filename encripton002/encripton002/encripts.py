

class BOS:
    num = 0

    def code(n_char, text):
        r_text = ''                                            # the text, wat the funktion give back 
        j=0
        for i in text:
            r_text = r_text+chr(ord(i)+n_char)
            ++j
        print (r_text)
        return r_text

