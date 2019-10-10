#!/usr/bin/python3
from tkinter import *
import os
import autocomplete
import random
import loader
from threading import Thread
import signal
import getpass

lista = []

password = ""


def sigint_handler(sig, frame):
    gui.screen.quit()
    gui.screen.update()


class LoaderGui(Thread):
    def __init__(self):
        self.current_uniid = ""
        self.current_robotid = ""

    # def add_uniid(self):

    def delete2(self):
        screen3.destroy()

    def delete3(self):
        screen4.destroy()

    def delete4(self):
        screen5.destroy()

    def start_robot(self):
        pass

    def load_code(self):
        # self.code_loader.(self.current_uniid, self.current_robotid, task_id)
        pass

    def stop_robot(self):
        self.code_loader(self.)
        pass

    def stop(self):

        screen3 = Toplevel(self.screen)
        screen3.title("Stop")
        screen3.geometry("300x250")

        Label(screen3, text="Enter robot ID to stop").pack()

        Label(screen3, text="").pack()

        Label(screen3, text="Robot ID").pack()
        self.robot_id_entry = Entry(screen3, textvariable=StringVar(self.current_robotid))
        Label(screen3, text="").pack()

        Button(screen3, text="Stop robot", width=10,
               height=1, command=self.stop_robot).pack()

    def load(self):
        # global screen2

        screen2 = Toplevel(self.screen)
        screen2.title("Loader")
        screen2.geometry("300x250")

        lista.append(self.entry_test.get())

        Label(screen2, text="Fill in all the fields").pack()
        Label(screen2, text="").pack()
        global last_r_id
        global last_uni_id

        last_r_id = self.current_robotid

        default_r_id = StringVar()
        default_r_id.set(last_r_id)
        last_uni_id = StringVar()
        default_assignment_id = StringVar()

        default_assignment_id.set("L1")

        Label(screen2, text="Robot ID").pack()
        self.robot_id_entry = Entry(screen2, textvariable=default_r_id)
        assignment_entry = Entry(screen2, textvariable=default_assignment_id)

        # robot_id_entry.setvar("1")
        self.robot_id_entry.pack()
        Label(screen2, text="").pack()
        Label(screen2, text="Assignment ID").pack()

        # make into autocomplete entry
        assignment_entry.pack()
        # password_entry1 = entry(screen2)
        # password_entry1.pack()
        Label(screen2, text="").pack()
        Button(screen2, text="Start robot", width=10,
               height=1, command=login_verify).pack()

    def main_screen(self):
        # global screen
        self.screen = Tk()

        # self.code_loader = loader.Loader(password)

        self.entry_test = autocomplete.AutocompleteEntryBox(lista, self.screen)

        self.screen.resizable(0, 0)
        # screen.overrideredirect(True)
        self.screen.wm_attributes('-type', 'splash')

        self.screen.geometry("600x500+100+100")

        self.screen.title("LoaderGui")

        Label(text="LoaderGui V0.01", bg="grey", width="300",
              height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Label(self.screen, text="Uni ID").pack()
        self.entry_test.pack()
        Label(text="").pack()

        Button(text="Upload code", height="1",
               width="30", command=self.load).pack()
        Label(text="").pack()
        Button(text="Stop robot", height="1",
               width="30", command=self.stop).pack()
        Label(text="").pack()
        Button(text="Fetch output", height="1",
               width="30", command=self.load).pack()
        Label(text="").pack()

        self.screen.mainloop()

# main_screen()


password = getpass.getpass("Enter password: ")

gui = LoaderGui()

signal.signal(signal.SIGINT, sigint_handler)

gui.main_screen()
