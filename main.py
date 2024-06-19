import os
import tkinter.filedialog as tkfd
import tkinter as tk
from tkinter import *
from tkinter import ttk
import fileUtils
import tkfilebrowser

backgroundColor = "#f0f0f0"
class gui():
        def __init__(self):
                self.homePath = os.path.expanduser("~")
                ## Root settings
                self.root=Tk()
                self.root.config(background=backgroundColor)
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
                self.secondlayer=Frame(self.root,bg=backgroundColor)
                
                ##---> third layer
                self.thirdLayer=Frame(self.root, bg=backgroundColor)

                ##---> fourth layer
                self.fourthLayer=Frame(self.root, bg=backgroundColor)
                
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
                self.inputAddButton=Button(self.tvInputControllersFrame, text="Add files", command=self.insertInput) # command change here
                self.inputAddButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)
                
                self.inputDeleteButton=Button(self.tvInputControllersFrame, text="Delete Selected") # command change here
                self.inputDeleteButton['command']=self.deleteSelectedInput
                self.inputDeleteButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)

                self.inputDeleteAllButton=Button(self.tvInputControllersFrame, text="Delete All") # command change here
                self.inputDeleteAllButton['command']=self.deleteAllInput
                self.inputDeleteAllButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)

                self.treeviewInput.pack(fill=X,padx=10, pady=10)
                self.treeviewInput.configure(height=8)
                
                ##--------------------------------------##
                ##             Output treeview          ##
                ##--------------------------------------##
                self.treeviewOutput=ttk.Treeview(self.tvOutputFrame)
                ##--------->  Treeview controll buttons
                self.outputAddButton=Button(self.tvOutputControllersFrame, text="Add directores", command=self.insertOutput)     # command change here
                self.outputAddButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)

                self.outputDeleteButton=Button(self.tvOutputControllersFrame, text="Delete Selected") # command change here
                self.outputDeleteButton['command']=self.deleteSelectedOutput
                self.outputDeleteButton.pack(fill="both", side="top",padx=10, pady=10, expand=True)

                self.outputDeleteAllButton=Button(self.tvOutputControllersFrame, text="Delete All")     # command change here
                self.outputDeleteAllButton['command']=self.deleteAllOutput
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
                self.statusMessage = StringVar()
                self.statusMessage.set("Status: waiting for task to run")
                self.statusLabel = Label(self.thirdLayer, textvariable=self.statusMessage, font=("Courier", 12))
                self.statusLabel.pack()
                
                ##------------------------------##
                ##      Fourth layer            ##
                ##------------------------------##
                
                # Initialization
                self.fourthLayer.pack(fill=X, expand=True)
                
                # Quit button
                self.quitButton = Button(self.fourthLayer, text="Exit", command=self.root.quit)
                self.quitButton.pack(fill=X, side=LEFT, expand=True, padx=50, pady=10)
                
                # Execute button
                self.executeButton = Button(self.fourthLayer, text="Execute task") #----> Add command here ((command=lorem))
                self.executeButton['command']=self.executeTask
                self.executeButton.pack(side=RIGHT,fill=X, expand=True, padx=50, pady=10)
                
                self.root.mainloop()


        def insertInput(self):
                files=tkfilebrowser.askopenfilenames(initialdir=self.homePath)
                print(files)
                for file in files:
                        add=True
                        for child in self.treeviewInput.get_children():
                                text=self.treeviewInput.item(child,'text')
                                if text==file:
                                        add=False    
                        
                        if add:
                                self.treeviewInput.insert("","end",text=file)
        
        def insertOutput(self):
                dirs=tkfilebrowser.askopendirnames(initialdir=self.homePath)
                # print(files)
                add=True

                for dir in dirs:
                        add = True
                        for child in self.treeviewOutput.get_children():
                                text=self.treeviewOutput.item(child,'text')
                                if text==dir:
                                        add=False    
                                
                        if add:
                                self.treeviewOutput.insert("",END,text=dir)
                        
        def deleteSelectedInput(self):
                tree = self.treeviewInput
                selectedItems= tree.selection()
                for selection in selectedItems:
                        tree.delete(selection)          
        
        def deleteSelectedOutput(self):
                tree = self.treeviewOutput
                selectedItems= tree.selection()
                for selection in selectedItems:
                        tree.delete(selection)                
        
        def deleteAllInput(self):
                tree= self.treeviewInput
                items= tree.get_children()
                for item in items:
                        tree.delete(item)            
        
        def deleteAllOutput(self):
                tree= self.treeviewOutput
                items= tree.get_children()
                for item in items:
                        tree.delete(item)                

        def executeTask(self):
                self.statusMessage.set("Status: task running")
                inputTree = self.treeviewInput
                inputItems = inputTree.get_children()
                copyFrom = []
                for item in inputItems:
                        var = inputTree.item(item)["text"]
                        copyFrom.append(var)
                
                outputTree = self.treeviewOutput 
                outputItems = outputTree.get_children()
                copyTo = []
                for item in outputItems:
                        var = outputTree.item(item)["text"]
                        copyTo.append(var)
                
                try:
                        fileUtils.copyAndReplace(copyFrom,copyTo)
                except Exception as e:
                        self.statusMessage.set("Status: error, call the developer")
                        print(e)
                        return

                self.statusMessage.set("Status: task complete")

g=gui()
