from stack_implementation import ArrayStack

def is_matched_html(raw):
    """Return True if all HTML tags are properly matched; Fales otherwise """

    S = ArrayStack()
    j = raw.find('<')     # find first '<' (if any)
    while j != -1:
        k = raw.find('>',j+1) # find next '>'
        if k == -1:
            return False  # invalid tag

        tag = raw[j+1:k]  # strip away < >

        if not  tag.startswith('/'):    # this is opening tag
            S.push(tag)

        else:                           # this is Closing tag
            if S.is_empty():
                return False            # nothing to match with
            if  tag[1:] != S.pop():
                return False            # mismatched delimiter

        j = raw.find('<',k+1)           # find next '<' if any

    return S.is_empty()




if __name__ == '__main__':
    print is_matched_html("""<html><head><title>Paragraph</title></head><body><p>A Computer Science portal for geeks.</p><p>It contains well written, well thought articles.</p></body></html>""" )
