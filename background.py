import ConfigParser

import Tkinter as tk
import ttk


Config = ConfigParser.ConfigParser()
parse = ConfigParser.SafeConfigParser()
parse.read('./cnf.ini')

class Win(tk.Frame):
    """
    Displays a series of buttons that change the colour of the Tkinter 
    frame when pressed.
    """
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.master = master

        self.mainf = tk.Frame(master, height=200, width=200, pady=50, padx=50)
        self.mainf.grid(row=0, column=0)

        self.colour_btns()
        self.theme_btns()

        self.save_btn = ttk.Button(self.mainf, text='Save',
                                   command=self.write_settings)
        self.save_btn.grid(row=5)

        self.s = ttk.Style()
        self.color_choice = parse.get('theme', 'choice')
        self.theme_type = parse.get('theme', 'layout')
        self.s.theme_use(self.theme_type)
        self.mainf.configure(background=self.color_choice)
        
        self.colors = ['red', 'green', 'blue', 'orange']

    def colour_btns(self):
        self.red = ttk.Button(self.mainf, text="red",
                              command=lambda: self.change_background(
                                  self.colors[0]))
        self.green = ttk.Button(self.mainf, text="green",
                                command=lambda: self.change_background(
                                  self.colors[1]))
        self.blue = ttk.Button(self.mainf, text="blue",
                               command=lambda: self.change_background(
                                  self.colors[2]))
        self.orange = ttk.Button(self.mainf, text="orange",
                                 command=lambda: self.change_background(
                                  self.colors[3]))
        self.red.grid(row=0, column=0)
        self.green.grid(row=1, column=0)
        self.blue.grid(row=2, column=0)
        self.orange.grid(row=3, column=0)

    def theme_btns(self):
        self.alt = ttk.Button(self.mainf, text="alt",
                              command=lambda: self.change_theme('alt'))

        self.aqua = ttk.Button(self.mainf, text="aqua",
                              command=lambda: self.change_theme('aqua'))
        self.clam = ttk.Button(self.mainf, text="clam",
                              command=lambda: self.change_theme('clam'))
        self.deflt = ttk.Button(self.mainf, text="default",
                              command=lambda: self.change_theme('default'))
        self.classic = ttk.Button(self.mainf, text="classic",
                              command=lambda: self.change_theme('classic'))
        self.alt.grid(row=0, column=1)
        self.aqua.grid(row=1, column=1)
        self.clam.grid(row=2, column=1)
        self.deflt.grid(row=3, column=1)
        self.classic.grid(row=4, column=1)

    def change_background(self, color):
        self.color_choice = color
        self.mainf.configure(background='{}'.format(self.color_choice))

    def change_theme(self, theme):
        """
        Changes theme of gui. Input is name of theme as string.
        """
        self.theme_type = theme
        self.s.theme_use(self.theme_type)

    def write_settings(self):

        self.cnffile = open('cnf.ini', 'w')
        Config.add_section('theme')
        Config.set('theme', 'choice', self.color_choice)
        Config.set('theme', 'layout', self.theme_type)
        Config.write(self.cnffile)
        self.cnffile.close()
        root.destroy()

root = tk.Tk()
root.title('Background')
root.update()

app = Win(root)

root.mainloop()
