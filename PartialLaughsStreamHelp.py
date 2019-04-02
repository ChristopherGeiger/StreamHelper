import tkinter
import os
from tkinter import messagebox
from tkinter import filedialog

main_win = tkinter.Tk()
main_win.title("PartialLaughs Stream Help")
#################################   START OF CODE   ############################

# globals
cfg = ("config.txt")
cur_dir = os.getcwd()
config = (cur_dir + "/config.txt")
program_line = (" ")

# Deffinitions to be used in the dropdowns
def loadConfig():
    file_list = os.listdir(cur_dir)
    if cfg in file_list:
        mkButtons = open(config,"r")
        ButtonsList = mkButtons.readlines()
        for lines in ButtonsList:
            def lineCommand(lines):
                program_line = (cur_dir + "/" + lines)
                os.system(program_line)
                print(program_line)
            lineButton = tkinter.Button(main_win, text=lines,command =lambda x=lines: lineCommand(x))
            lineButton.pack()
            lines + "1"
    else:
        tkinter.messagebox.showinfo("Error:","Configuration File Not Found \n Please Select New Configuration In The File Dropdown Menu")
# makes a new config.txt
def makeConfig():
    print(cur_dir)
    mkconfig = open(cur_dir + "/config.txt","a+")
    mkconfig.close()
    tkinter.messagebox.showinfo("Success!","New Configuration File Added! \n You Can Now Add New Programs")
# creates .vbs files for whatever the user defines
def makeLaunchers():
    def clearField():
        Name.delete(0, 100)
        File.delete(0, 100)

    def Obj():
        global vb_pre_name
        vb_pre_name = Name.get()
        vb_name = vb_pre_name + ".vbs"
        print(vb_name)
        Name.delete(0, 100)
        Name.insert(0, vb_name)

        mkFile_check = open((cur_dir + "/"+ vb_name),"a+")
        mkFile_check.close()
        os.remove(cur_dir + "/"+ vb_name)
        mkFile = open((cur_dir + "/"+ vb_name),"a+")
        mkFile.write('CreateObject("WScript.Shell").Run("' + vb_createFile + '")')
        mkFile.close()

        #making the records in the config file
        mkconfig = open((cur_dir) + "/config.txt","a+")
        mkconfig.write(vb_name + "\n")
        mkconfig.close()

    def chooseFile():
        global vb_createFile
        vb_createFile = filedialog.askopenfilename(initialdir= "/", title='Please Select A Program')
        print(vb_createFile)
        File.insert(0, vb_createFile)

    main_win.focus_force()
    tkinter.Label(main_win, text = "Program Name:").grid(row=0,column=1)
    tkinter.Label(main_win, text = "Program Location:").grid(row=1,column=1)
    Name = tkinter.Entry(main_win)
    Name.grid(row=0,column=2)
    File = tkinter.Entry(main_win)
    File.grid(row=1,column=2)
    tkinter.Button(main_win, text='Add Program', command=Obj).grid(row=2,column=2)
    tkinter.Button(main_win, text='Locate', command=chooseFile).grid(row=1,column=3)
    tkinter.Button(main_win, text='Next Program', command=clearField).grid(row=3,column=2)
# making the menu's
loadConfig()
root_menu = tkinter.Menu(main_win)
main_win.config(menu = root_menu)

file_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New Configuration",command=makeConfig)
file_menu.add_command(label="Add New Command",command=makeLaunchers)
file_menu.add_separator()
file_menu.add_command(label="Quit",command=main_win.destroy)

main_win.mainloop()
