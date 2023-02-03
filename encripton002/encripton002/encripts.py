import sys

class BOS:
    num = 0

    def code(n_char, text):
        r_text = ''                                            # the text, wat the funktion give back 
        for i in text:
            r_text = r_text+chr(BOS.sec(ord(i), n_char))
        print (r_text)
        return r_text
    def d_code(n_char, text):
        n_char = -n_char
        r_text = ''                                            # the text, wat the funktion give back 
        for i in text:
            r_text = r_text+chr(BOS.sec(ord(i), n_char))
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


class SCYTALE:

    def code(size, text):
        r_text = ['']                                            # the text, wat the funktion give back
        ix = 0
        while ix != size-1:
            r_text.append('')
            ix=ix+1
        j=0
        for i in text:
            r_text[j] = r_text[j]+i
            j = j+1
            if j>=size:
                j = 0
        r_text_ = ''
        for i in r_text:                                        # This part make ohne string from the string list.
            r_text_=r_text_ + i
        print (r_text_)
        return r_text

    def d_code(size, text):                                     #size mean number of container
        SizeOfContainer = int(len(text)/size)
        num_norm_run = (SizeOfContainer-len(text)%size)*size
        pos_text = 0                                            #the position of next character in encripting
        normal = 0
        ret = ''
        while normal < num_norm_run:
            ret = ret + text[pos_text]
            pos_text = pos_text + 1
            normal = normal+1
            if pos_text >= len(text):
                pos_text = pos_text - len(text)
        while pos_text < len(text):



        r_text_ = ''
        for i in r_text:                                        # This part make ohne string from the string list.
            r_text_=r_text_ + i
        
            print (r_text_)
        return r_text
