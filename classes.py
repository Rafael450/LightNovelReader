from functions import symbol, is_top_white,line_concat

class Line:
    def __init__(self,image,text,prev_line=None):
        self.image = image
        self.prev_line = prev_line
        self.symbol = symbol(self.image)
        self.text = text if self.symbol == 'Text' else self.symbol
        self.next_line = None
        if prev_line != None:
            self.prev_line.next_line = self

        if is_top_white(self.image) or (self.prev_line.text[-1] == '。' and (self.text[0] == '『' or self.text[0] == '【')) \
                                    or self.text[0] == '「' or self.prev_line.symbol != 'Text':
            self.is_line_start = True
        else: 
            self.is_line_start = False
    
    def find_next_first(self):
        if self.next_line == None:
            return None
        return self.next_line if self.next_line.is_line_start else self.next_line.find_next_first()
            

class Phrase:
    def __init__(self,first_line,prev_phrase=None):
        self.prev_phrase = prev_phrase
        self.text = line_concat(first_line)
        self.next_phrase = None
        if prev_phrase != None:
            self.prev_phrase.next_phrase = self
    
    def print_all(self, file):
        file.write(self.text)
        self.print_all(self.next_phrase, file)

