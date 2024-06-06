import tkinter.filedialog as tkfd
import tkinter as tk
from tkinter import *
from tkinter import ttk

class gui():
        def __init__(self):
                ## Root settings
                self.root=Tk()
                self.root.title("n2npyco")
                self.root.geometry("800x600")
                self.root.resizable(width=False, height=False)
                
                
                ## Frames
                ##---> first layer
                self.firstlayer=Frame(self.root)
                self.treeviewframe=Frame(self.firstlayer,bg="")
                self.treeviewControllers=Frame(self.treeviewframe, bg="")
                self.tvInputFrame=Frame(self.treeviewframe, bg="")
                self.tvInputControllersFrame=Frame(self.tvInputFrame, bg="")
                self.tvOutputFrame=Frame(self.treeviewframe, background="")
                self.tvOutputControllersFrame=Frame(self.tvOutputFrame, background="")
                
                ##---> second layer
                self.secondlayer=Frame(self.root,bg="")
                
                ##---> third layer
                self.thirdLayer=Frame(self.root, bg="")
                
                
                ##Functions 
                
                
                def insertInput():
                        files=tkfd.askopenfiles()
                        for file in files:
                                add=True
                                for child in self.treeviewInput.get_children():
                                        text=self.treeviewInput.item(child,'text')
                                        if text==file.name:
                                                add=False    
                                
                                if add:
                                        self.treeviewInput.insert("","end",text=file.name)
                
                
                
                ##----------------------##
                ##      First layer     ##
                ##----------------------##
                
                # Initialization
                self.firstlayer.pack(side="top",fill="x")
                
                self.treeviewframe.pack(side="left", fill="x", expand=True)
                self.tvInputFrame.pack(fill="x", expand=True)
                self.tvInputControllersFrame.pack(side=RIGHT, fill=BOTH)   
                self.tvOutputFrame.pack(fill="x", expand=True)
                self.tvOutputControllersFrame.pack(side=RIGHT, fill=BOTH)   
                             
                ##--------------------------------------##
                ##              Input treeview          ##
                ##--------------------------------------##
                self.treeviewInput=ttk.Treeview(self.tvInputFrame)
                ##--------->  Treeview controll buttons
                self.inputAddButton=Button(self.tvInputControllersFrame, text="Add files", command=insertInput)     # command change here
                self.inputAddButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)
                self.inputDeleteButton=Button(self.tvInputControllersFrame, text="Delete Selected") # command change here
                self.inputDeleteButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)
                self.inputDeleteAllButton=Button(self.tvInputControllersFrame, text="Delete All")     # command change here
                self.inputDeleteAllButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)

                self.treeviewInput.pack(fill=X,padx=10, pady=10)
                self.treeviewInput.configure(height=8)
                
                
                ##--------------------------------------##
                ##             Output treeview          ##
                ##--------------------------------------##
                self.treeviewOutput=ttk.Treeview(self.tvOutputFrame)
                ##--------->  Treeview controll buttons
                self.outputAddButton=Button(self.tvOutputControllersFrame, text="Add directores")     # command change here
                self.outputAddButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)
                self.outputDeleteButton=Button(self.tvOutputControllersFrame, text="Delete Selected") # command change here
                self.outputDeleteButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)
                self.outputDeleteAllButton=Button(self.tvOutputControllersFrame, text="Delete All")     # command change here
                self.outputDeleteAllButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)
                self.tvInputFrame.pack()
                
                self.treeviewOutput.pack(fill=X,padx=10, pady=10)
                self.treeviewOutput.configure(height=8)
                
                ##----------------------##
                ##      Second layer    ##
                ##----------------------##
                
                #Initilization 
                self.secondlayer.pack(side=TOP, fill=BOTH, expand=True)
                
                
                ##------------------------------##
                ##      Third layer             ##
                ##------------------------------##
                
                # Initialization
                self.thirdLayer.pack(fill=X, expand=True)
                
                # Quit button
                self.quitButton = Button(self.thirdLayer, text="Exit", command=self.root.quit)
                self.quitButton.pack(fill=X, side=LEFT, expand=True, padx=50, pady=10)
                
                # Execute button
                self.executeButton = Button(self.thirdLayer, text="Execute task") #----> Add command here ((command=lorem))
                self.executeButton.pack(side=RIGHT,fill=X, expand=True, padx=50, pady=10)
                
                
                
                self.root.mainloop()


g=gui()
