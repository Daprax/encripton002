

class BOS:
    num = 0

    def code(n_char, text):
        r_text = ''                                            # the text, wat the funktion give back 
        j=0
        for i in text:
            r_text = r_text+chr(BOS.sec(ord(i), n_char))
            ++j
        print (r_text)
        return r_text
    def d_code(n_char, text):
        n_char = -n_char
        r_text = ''                                            # the text, wat the funktion give back 
        j=0
        for i in text:
            r_text = r_text+chr(BOS.sec(ord(i), n_char))
            ++j
        print (r_text)
        return r_text
    def sec(actual_char, n_char):                              #This funktion solv the problem: in asci after 'z' not again 'a' come
        if actual_char<=90 and actual_char>=65:                #Uppercase fall
            if actual_char+n_char<=90 and actual_char+n_char>=65:
                return actual_char+n_char
            else:
                if actual_char+n_char > 90:
                    return actual_char+n_char-26
                else:
                    return actual_char+n_char+26
        elif actual_char<=122 and actual_char>=97:             #Lowercase fall
            if actual_char+n_char<=122 and actual_char+n_char>=97:
                return actual_char+n_char
            else:
                if actual_char+n_char > 122:
                    return actual_char+n_char-26
                else:
                    return actual_char+n_char+26
        else:
            return actual_char


