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
        self.current_robotid = "1"
        self.current_taskid = "L1"

    # def add_uniid(self):

    def delete2(self):
        screen3.destroy()

    def delete3(self):
        screen4.destroy()

    def delete4(self):
        screen5.destroy()

    def start_robot(self):
        self.update_ids()
        print (self.current_taskid)
        print(self.current_uniid)
        print(self.current_robotid)

        self.code_loader.load(self.current_uniid,
                              self.current_robotid, self.current_taskid)

    # def load_code(self):
    #     self.code_loader.(self.current_uniid, self.current_robotid, task_id)

    def stop_robot(self):
        self.code_loader.stop(self.stop_id.get())

    def update_ids(self):
        self.current_uniid = self.robot_id_entry.get()
        self.current_taskid = self.assignment_entry.get()

    def stop(self):

        screen3 = Toplevel(self.screen)
        screen3.title("Stop")
        screen3.geometry("300x250")

        Label(screen3, text="Enter robot ID to stop").pack()

        Label(screen3, text="").pack()

        Label(screen3, text="Robot ID").pack()
        self.stop_id = Entry(
            screen3, textvariable=StringVar(self.current_robotid))

        stop_id.pack()
        Label(screen3, text="").pack()

        Button(screen3, text="Stop robot", width=10,
               height=1, command=self.stop_robot).pack()

    def load_screen(self):
        # global screen2
        self.current_uniid = self.entry_test.get()

        screen2 = Toplevel(self.screen)
        screen2.title("Loader")
        screen2.geometry("300x250")

        print(self.current_uniid)
        print(self.current_taskid)
        print(self.current_robotid)

        if (self.current_uniid not in lista):
            lista.append(self.current_uniid)

        Label(screen2, text="Fill in all the fields").pack()
        Label(screen2, text="").pack()

        last_r_id = self.current_robotid

        default_r_id = StringVar()
        default_r_id.set(last_r_id)
        default_assignment_id = StringVar()

        default_assignment_id.set(self.current_taskid)

        Label(screen2, text="Robot ID").pack()
        self.robot_id_entry = Entry(screen2, textvariable=default_r_id)
        self.assignment_entry = Entry(
            screen2, textvariable=default_assignment_id)

        # robot_id_entry.setvar("1")
        self.robot_id_entry.pack()
        Label(screen2, text="").pack()
        Label(screen2, text="Assignment ID").pack()

        # make into autocomplete entry
        self.assignment_entry.pack()
        # password_entry1 = entry(screen2)
        # password_entry1.pack()
        print(self.current_taskid)
        print(self.current_robotid)
        Label(screen2, text="").pack()
        Button(screen2, text="Start robot", width=10,
               height=1, command=self.start_robot).pack()

    def main_screen(self):
        self.screen = Tk()

        self.code_loader = loader.Loader(password)

        self.entry_test = autocomplete.AutocompleteEntryBox(lista, self.screen)

        self.screen.geometry("600x500+100+100")

        self.screen.title("LoaderGui")

        Label(text="LoaderGui V0.01", bg="grey", width="300",
              height="2", font=("Calibri", 13)).pack()
        Label(text="").pack()
        Label(self.screen, text="Uni ID").pack()
        self.entry_test.pack()
        Label(text="").pack()

        Button(text="Upload code", height="1",
               width="30", command=self.load_screen).pack()
        Label(text="").pack()
        Button(text="Stop robot", height="1",
               width="30", command=self.stop).pack()
        Label(text="").pack()
        Button(text="Fetch output", height="1",
               width="30", command=self.load_screen).pack()
        Label(text="").pack()

        self.screen.mainloop()


# main_screen()
if __name__ == "__main__":

    password = getpass.getpass("Enter password: ")
    gui = LoaderGui()
    signal.signal(signal.SIGINT, sigint_handler)
    gui.main_screen()
