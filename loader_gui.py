#!/usr/bin/python3
from tkinter import *
import os
import autocomplete
import random
import loader
from threading import Thread

lista = ["abba", "killer queen", "youth", "arkansas", "arctangent"]

class LoaderGui(Thread):
    def delete2(self):
        screen3.destroy()


    def delete3(self):
        screen4.destroy()


    def delete4(self):
        screen5.destroy()


    def login_sucess(self):
        global screen3
        screen3 = Toplevel(screen)
        screen3.title("Success")
        screen3.geometry("150x100")
        Label(screen3, text="Login Sucess").pack()
        Button(screen3, text="OK", command=delete2).pack()


    def password_not_recognised(self):
        global screen4
        screen4 = Toplevel(screen)
        screen4.title("Success")
        screen4.geometry("150x100")
        Label(screen4, text="Password Error").pack()
        Button(screen4, text="OK", command=delete3).pack()


    def user_not_found(self):
        global screen5
        screen5 = Toplevel(screen)
        screen5.title("Success")
        screen5.geometry("150x100")
        Label(screen5, text="User Not Found").pack()
        Button(screen5, text="OK", command=delete4).pack()


    def register_user(self):
        print("working")

        username_info = username.get()
        password_info = password.get()

        file = open(username_info, "w")
        file.write(username_info+"\n")
        file.write(password_info)
        file.close()

        username_entry.delete(0, END)
        password_entry.delete(0, END)

        Label(screen1, text="Registration Sucess",
            fg="green", font=("calibri", 11)).pack()


    def login_verify(self):

        username1 = username_verify.get()
        password1 = password_verify.get()
        username_entry1.delete(0, END)
        password_entry1.delete(0, END)

        list_of_files = os.listdir()
        if username1 in list_of_files:
            file1 = open(username1, "r")
            verify = file1.read().splitlines()
            if password1 in verify:
                login_sucess()
            else:
                password_not_recognised()

        else:
            user_not_found()


    def start_robot(self):
        pass


    def load(self):
        # global screen2

        # screen2 = Toplevel(screen)
        screen2 = Tk()
        screen2.title("Loader")
        screen2.geometry("300x250")

        id_list = ["test1", "test2", "andepi", "arnold"]

        entry_test = autocomplete.AutocompleteEntryBox(id_list, screen2)

        Label(screen2, text="Fill in all the fields").pack()
        Label(screen2, text="").pack()
        global last_r_id
        global last_uni_id

        last_r_id = str(random.random())

        #   global username_verify
        #   global password_verify

        #   username_verify = StringVar()
        #   password_verify = StringVar()
        default_r_id = StringVar()
        default_r_id.set(last_r_id)
        last_uni_id = StringVar()
        global username_entry1
        global password_entry1

        Label(screen2, text="Robot ID").pack()
        robot_id_entry = Entry(screen2, textvariable=default_r_id)

        # robot_id_entry.setvar("1")
        robot_id_entry.pack()
        Label(screen2, text="").pack()
        Label(screen2, text="Uni ID").pack()

        # make into autocomplete entry
        entry_test.pack()
        # password_entry1 = entry(screen2)
        # password_entry1.pack()
        Label(screen2, text="").pack()
        Button(screen2, text="Start robot", width=10,
            height=1, command=login_verify).pack()


    def main_screen(self):
        global screen
        screen = Tk()

        entry_test = autocomplete.AutocompleteEntryBox(
            list(["item1", "item2", "andepi"]), screen)


        screen.resizable(0, 0)
        # screen.overrideredirect(True)
        screen.wm_attributes('-type', 'splash')

        screen.geometry("600x500+100+100")
        # screen.geometry("+300x+250")

        screen.title("LoaderGui")
        Label(text="LoaderGui V0.01", bg="grey", width="300",
            height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Button(text="Upload code", height="1", width="30", command=load).pack()
        Label(text="").pack()
        Button(text="Stop robot", height="1", width="30", command=load).pack()
        Label(text="").pack()
        Button(text="Fetch output", height="1", width="30", command=load).pack()
        Label(text="").pack()
        Label(screen, text="Uni ID").pack()
        entry_test.pack()

        
        screen.mainloop()


# main_screen()


def main():
    pass
