class Alphabet:
    
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters
    
    def aprint(self):
        print(self.lang)
        for i in self.letters:
            print(i)
        
    def letters_num(self):
        self.len = len(self.letters)
        print(f"количество букв алфавита: {self.len}")
        
alph = Alphabet("asdggf", 
                ("as",
                "asdfgfd",
                "sdfgd",
                "sdfsg",
                "sdfs",
                "sdfgfs",
                "sdfgf",
                "sdfgfgd"))
alph.aprint()
alph.letters_num()

      
    
        