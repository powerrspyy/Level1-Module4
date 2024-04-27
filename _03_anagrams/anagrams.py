"""
Create an anagram game!
"""
import random
import tkinter as tk

# TODO Use this dictionary of anagrams to create an anagrams GUI word game.
#  Look at 'anagrams_game_example.png' in this folder for an example.
word_anagrams = {
    "action": ["cation"],
    "agree": ["eager"],
    "calm": ["clam"],
    "charming": ["marching"],
    "clean": ["lance"],
    "cool": ["loco"],
    "creative": ["reactive"],
    "delight": ["lighted"],
    "earnest": ["eastern", "nearest"],
    "easy": ["ayes", "yeas"],
    "free": ["reef"],
    "great": ["grate"],
    "green": ["genre"],
    "grin": ["ring"],
    "hearty": ["earthy"],
    "idea": ["aide"],
    "ideal": ["ailed"],
    "keen": ["knee"],
    "lively": ["evilly", "vilely"],
    "lovely": ["volley"],
    "merit": ["miter", "remit", "timer"],
    "open": ["nope", "peon", "pone"],
    "prepared": ["dapperer"],
    "quiet": ["quite"],
    "refined": ["definer"],
    "restored": ["resorted", "rostered"],
    "reward": ["drawer", "redraw", "warder", "warred"],
    "rewarding": ["redrawing", "wardering"],
    "right": ["girth"],
    "secure": ["rescue"],
    "simple": ["impels"],
    "smile": ["limes", "miles", "slime"],
    "super": ["puers", "purse"],
    "tops": ["opts", "post", "pots", "spot", "stop"],
    "unreal": ["neural"],
    "wonderful": ["underflow"],
    "zeal": ["laze"]}

class Anagrams(tk.Tk):
    WIDTH = 500
    HEIGHT = 200
    def __init__(self):
        super().__init__()
        self.choice = random.sample(word_anagrams.keys(),1)[0]
        self.title =tk.Label(text = f"Guess The Anagram Of {self.choice}")
        self.title.place(x=0,y = 0, width = 200, height = 15)

        self.text_field = tk.Text(background="#d9d9d9", font=('arial', 15))
        self.text_field.place(x=0,y=17, width = 200, height=24)

        self.button = tk.Button(self, text='Submit', fg='black', font=('arial', 10, 'bold'))
        self.button.place(x=75,y=43,width=50,height=15)
        self.button.bind("<ButtonPress>", self.retrieve_input)

        self.label_2 = tk.Label(text = 'Correct', background="green")

        self.next_button = tk.Button(self, text='Next Word', fg='black', font=('arial', 10, 'bold'))
        self.next_button.place(x=75,y=150,width=50,height=15)
        self.next_button.bind("<ButtonPress>", self.button_refresh)



    def retrieve_input(self, button):
        inputValue=self.text_field.get("1.0","end-1c")
        if inputValue in word_anagrams[self.choice]:
            print(True)
            self.label_2.configure(text = 'Correct', background="green")
            self.label_2.place(x=50, y=100, height=20,width=100)
        else:
            print(False)
            self.label_2.configure(text = 'Incorrect', background="#f0756c")
            self.label_2.place(x=50, y=100, height=20,width=100)
    def button_refresh(self,button):
        self.choice = random.sample(word_anagrams.keys(),1)[0]
        self.title =tk.Label(text = f"Guess The Anagram Of {self.choice}")
        self.title.place(x=0,y = 0, width = 200, height = 15)

        self.text_field = tk.Text(background="#d9d9d9", font=('arial', 15))
        self.text_field.place(x=0,y=17, width = 200, height=24)

        self.label_2.configure(text = '', background="white")
        self.label_2.place(x=50, y=100, height=20,width=100)




game = Anagrams()
game.title = "Anagram Guesser 2000"
game.geometry("200x200")
game.mainloop()
