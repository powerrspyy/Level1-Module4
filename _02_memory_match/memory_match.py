"""
Create a memory match game!
"""
import random
import time
import tkinter as tk

# TODO: First, run this code. You should see a grid with 52 buttons.
#   Your task is to:
#   1. Create a dictionary with each button as a key and a number from 1 to 13
#      as the corresponding value. There are 52 buttons, so there should be EXACTLY
#      4 copies of each number from 1 ot 13.
#   2. Show the value of the button (a number from 1 to 13) when it's clicked.
#   3. After the second button is clicked, check if the number from the first button
#      matches the number of the second button.
#      a. If they match, show the two numbers and disable them so they can't be clicked again.
#         There is an example of how to disable the button in the code below.
#      b. If they don't match, remove the text from the two buttons. The two buttons should
#         still be clickable.
#   4. End the game with a congratulations message when all the numbers have been matched.
#   5. See 'memory_match_example.png' in this folder for an example of what the game should
#      look like.
class MemoryMatch(tk.Tk):
    WIDTH = 1090
    HEIGHT = 500
    TOTAL_BUTTONS = 52
    def __init__(self, buttons=None):
        super().__init__()
        self.buttons = {}
        # 4 copies of each value
        num_copies_each_value = 4
        buttons_per_row = MemoryMatch.TOTAL_BUTTONS / 4
        button_width, button_height = self.setup_buttons(buttons_per_row)

        for i in range(MemoryMatch.TOTAL_BUTTONS):
            row_num = int(i / buttons_per_row)
            col_num = int(i % buttons_per_row)
            row_y = row_num * button_height
            col_x = col_num * button_width

            button = tk.Button(self, text='', fg='black', font=('arial', 24, 'bold'))
            button.place(x=col_x, y=row_y, width=button_width, height=button_height)

            button.bind('<ButtonPress>', self.on_button_press)
            fours = dict()
            for i in range(13):
                fours[i+1] = 0
            all = 0
            while all != 52:
                rand = random.randint(1,13)
                if fours[rand] == 4:
                    pass
                else:
                    self.buttons[button] = rand
                    fours[rand] += 1
                    all+=1
            self.lastbutton = None
            self.numpressed = 0
    def on_button_press(self, event):
        button_pressed = event.widget
        print('Button ' + str(button_pressed) + ' was pressed')
        button_pressed_list = list(str(button_pressed))
        num = "".join(button_pressed_list[8::])
        print(num)
        if button_pressed['state'] == tk.NORMAL:
            button_pressed.configure(state=tk.NORMAL, text=f'{self.buttons[button_pressed]}')
        if self.numpressed == 0:
            self.numpressed = 1
            if self.lastbutton == button_pressed:
                self.numpressed = 0
            else:
                self.lastbutton = button_pressed
        elif self.numpressed == 1:
            self.numpressed = 0
            if self.buttons[button_pressed] == self.buttons[self.lastbutton]:
                if self.lastbutton != button_pressed:
                    button_pressed.configure(state=tk.DISABLED)
                    self.lastbutton.configure(state=tk.DISABLED)
            else:
                if button_pressed['state'] == tk.NORMAL:
                    button_pressed.configure(text="")
                if self.lastbutton['state'] == tk.NORMAL:
                    self.lastbutton.configure(text="")
                self.lastbutton = None



    def setup_buttons(self, buttons_per_row):
        # Window size needs to be updated immediately here so the
        # window width/height variables can be used below
        self.geometry('%sx%s' % (MemoryMatch.WIDTH, MemoryMatch.HEIGHT))
        self.update_idletasks()

        num_rows = int(MemoryMatch.TOTAL_BUTTONS / buttons_per_row)
        if MemoryMatch.TOTAL_BUTTONS % buttons_per_row != 0:
            num_rows += 1

        button_width = int(self.winfo_width() / buttons_per_row)
        button_height = int(self.winfo_height() / num_rows)

        return button_width, button_height

if __name__ == '__main__':
    game = MemoryMatch()
    game.title('League Python Memory Game')
    game.mainloop()
