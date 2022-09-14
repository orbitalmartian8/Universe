#!/usr/bin/env python
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

import os
from os.path import exists
from os.path import expanduser
from pathlib import Path

import shutil
import subprocess

home = expanduser("~")
user = os.getlogin()
source = "/usr/share/applications/universe.desktop"
dest = home + "/.config/autostart/universe.desktop"
settings = home + "/.config/universe/settings.conf"

# Window 1 - Main Window
class MyWindow1(Gtk.Window):
    def __init__(self):
        super().__init__(title="Universe")

        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)

        frame1 = Gtk.Frame(label="Universe")

        grid1 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = True)

        #image1 = Gtk.Image()
        #image1.set_from_file("/home/dt/nc/Org/test/python-app/image1.png")

        label1 = Gtk.Label(label="Welcome to your Universe!")
        label1.set_hexpand(True)

        label2 = Gtk.Label(label="Your hub to do basically everything.")
        label2.set_hexpand(True)

        label3 = Gtk.Label(label="About:")
        label3.set_hexpand(True)

        label4 = Gtk.Label(label="Things to do:")
        label4.set_hexpand(True)

        button1 = Gtk.Button(label="About Universe")
        button1.set_hexpand(True)
        button1.connect("clicked", self.on_button1_clicked)

        button2 = Gtk.Button(label="Knowledge Base")
        button2.set_hexpand(True)
        button2.connect("clicked", self.on_button2_clicked)

        button3 = Gtk.Button(label="Contribute")
        button3.set_hexpand(True)
        button3.connect("clicked", self.on_button3_clicked)

        launcher = Gtk.Button(label="App Launcher")
        launcher.set_hexpand(True)
        launcher.connect("clicked", self.on_launcher_clicked)

        terminal = Gtk.Button(label="TEST - Terminal (BROKEN)")
        terminal.set_hexpand(True)
        terminal.connect("clicked", self.on_terminal_clicked)

        button7 = Gtk.Button(label="Exit")
        button7.set_hexpand(True)
        button7.connect("clicked", Gtk.main_quit)

        #grid1.attach(image1,  0, 0, 3, 2)
        grid1.attach(label1,  0, 2, 3, 2)
        grid1.attach(label2,  0, 4, 3, 2)
        grid1.attach(label3,  0, 6, 3, 1)
        grid1.attach(button1, 0, 7, 1, 1)
        grid1.attach(button2, 1, 7, 1, 1)
        grid1.attach(button3, 2, 7, 1, 1)
        grid1.attach(launcher, 0, 16, 1, 1)
        grid1.attach(terminal, 1 ,16, 1, 1)
        grid1.attach(button7, 2, 30, 1, 1)
        grid1.attach(label4,  0, 15, 3, 1)

        self.add(frame1)
        frame1.add(grid1)

    def on_terminal_clicked(self, widget):
        print("User chose: Launch Terminal")
        subprocess.run(
        win1.hide(),
        win3.show_all())
        

    def on_button1_clicked(self, widget):
        print("User chose: About Universe")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe"])

    def on_button2_clicked(self, widget):
        print("User chose: Knowledge Base")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe"])

    def on_button3_clicked(self, widget):
        print("User chose: Contribute")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe/blob/main/Docs/CONTRIBUTE.md"])

    def on_launcher_clicked(self, widget):
        print("User chose: App Launcher")
        subprocess.run(
        win1.hide(),
        win2.show_all())

    def save_settings(self, state):
        with open(settings, "w") as f:
            f.write("autostart=" + str(state))
            f.close()

    def load_settings(self):
        line = "True"
        if os.path.isfile(settings):
            with open(settings, "r") as f:
                lines = f.readlines()
                for i in range(len(lines)):
                    if "autostart" in lines[i]:
                        line = lines[i].split("=")[1].strip().capitalize()
                f.close()
        return line

    def startup_toggle(self, widget):
        if widget.get_active() is True:
            if os.path.isfile(source):
                shutil.copy(source, dest)
        else:
            if os.path.isfile(dest):
                os.unlink(dest)
        self.save_settings(widget.get_active())

# Window 2 - App Launcher
class MyWindow2(Gtk.Window):
    def __init__(self):
        super().__init__(title="Universe: App Launcher")

        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)

        frame2 = Gtk.Frame(label="App Launcher")

        grid2 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = True)

        #image1 = Gtk.Image()
        #image1.set_from_file("/home/dt/nc/Org/test/python-app/image1.png")

        label1 = Gtk.Label(label="App Launcher")
        label1.set_hexpand(True)

        label2 = Gtk.Label()
        label3 = Gtk.Label()

        firefox = Gtk.Button(label="Firefox")
        firefox.set_hexpand(True)
        firefox.connect("clicked", self.on_firefox_clicked)

        alacritty = Gtk.Button(label="Alacritty")
        alacritty.set_hexpand(True)
        alacritty.connect("clicked", self.on_alacritty_clicked)

        code = Gtk.Button(label="Visual Studio Code")
        code.set_hexpand(True)
        code.connect("clicked", self.on_code_clicked)

        blender = Gtk.Button(label="Blender")
        code.set_hexpand(True)
        code.connect("clicked", self.on_blender_clicked)

        writer = Gtk.Button(label="Libreoffice Writer")
        writer.set_hexpand(True)
        writer.connect("clicked", self.on_writer_clicked)

        nitrogen = Gtk.Button(label="Nitrogen")
        nitrogen.set_hexpand(True)
        nitrogen.connect("clicked", self.on_nitrogen_clicked)

        emacs = Gtk.Button(label="Emacs")
        emacs.set_hexpand(True)
        emacs.connect("clicked", self.on_emacs_clicked)

        dolphin = Gtk.Button(label="Dolphin")
        dolphin.set_hexpand(True)
        dolphin.connect("clicked", self.on_dolphin_clicked)

        gimp = Gtk.Button(label="GIMP")
        gimp.set_hexpand(True)
        gimp.connect("clicked",self.on_gimp_clicked)

        button20 = Gtk.Button(label="Back To Main Menu")
        button20.set_hexpand(True)
        button20.connect("clicked", self.on_button20_clicked)

        button21 = Gtk.Button(label="Exit")
        button21.set_hexpand(True)
        button21.connect("clicked", Gtk.main_quit)

        #grid2.attach(image1,   0, 0, 4, 2)
        grid2.attach(label1,   0, 2, 4, 2)
        grid2.attach(label2,   0, 4, 4, 2)
        grid2.attach(firefox,  0, 7, 1, 1)
        grid2.attach(alacritty,  0, 6, 1, 1)
        grid2.attach(code, 0, 8, 1, 1)
        grid2.attach(blender, 1, 6, 1, 1)
        grid2.attach(writer, 2, 7, 1, 1)
        grid2.attach(nitrogen, 3, 7, 1, 1)
        grid2.attach(emacs, 2, 6, 1, 1)
        grid2.attach(dolphin, 3, 6, 1, 1)
        grid2.attach(gimp, 1, 7, 1, 1)
        grid2.attach(label3,   0, 9, 4, 1)
        grid2.attach(button20, 0, 10, 2, 1)
        grid2.attach(button21, 2, 10, 2, 1)

        self.add(frame2)
        frame2.add(grid2)

    def on_firefox_clicked(self, widget):
        print("Launcher: Firefox")
        subprocess.run(["firefox"])

    def on_alacritty_clicked(self, widget):
        print("Launcher: Alacritty")
        subprocess.run(["alacritty"])

    def on_code_clicked(self, widget):
        print("Launcher: Visual Studio Code")
        subprocess.run(["code"])

    def on_blender_clicked(self, widget):
        print("Launcher: Blender")
        subprocess.run(["blender"])
    
    def on_writer_clicked(self, widget):
        print("Launcher: Libreoffice Writer")
        subprocess.run(["libreoffice --writer"])

    def on_nitrogen_clicked(self, widget):
        print("Launcher: Nitrogen")
        subprocess.run(["nitrogen"])

    def on_emacs_clicked(self, widget):
        print("Launcher: Emacs")
        subprocess.run(["emacs"])
    
    def on_dolphin_clicked(self, widget):
        print("Launcher: Dolphin")
        subprocess.run(["dolphin"])
    
    def on_gimp_clicked(self, widget):
        print("Launcher: GIMP")
        subprocess.run(["gimp"])

    def on_button20_clicked(self, widget):
        print("Back To Main Menu")
        win2.hide()
        win1.show_all()

    def on_button21_clicked(self, widget):
        print("Exit")
        button21.connect("clicked", Gtk.main_quit)

# Window 3 - Terminal
class MyWindow3(Gtk.Window):
    def __init__(self):
        super().__init__(title="Universe: Terminal Emulator")

        self.set_border_width(10)
        self.set_default_size(640, 300)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_resizable(False)

        frame3 = Gtk.Frame(label="Terminal Emulator")

        grid3 = Gtk.Grid(row_spacing    = 10,
                         column_spacing = 10,
                         column_homogeneous = True)

        exit = Gtk.Button(label="Exit")
        exit.set_hexpand(True)
        exit.connect("clicked", Gtk.main_quit)
        
        label1 = Gtk.Label(label="Terminal")
        label1.set_hexpand(True)

        grid3.attach(label1, 1, 1, 1, 1)
        grid3.attach(exit, 1, 6, 1, 1)
        
        self.add(frame3)
        frame3.add(grid3)

        def on_exit_clicked(self, widget):
            print("Exit")
            exit.connect("clicked", Gtk.main_quit)

win1 = MyWindow1()
win2 = MyWindow2()
win3 = MyWindow3()

win1.connect("destroy", Gtk.main_quit)
win2.connect("destroy", Gtk.main_quit)
win3.connect("destroy", Gtk.main_quit)


win1.show_all()
Gtk.main()