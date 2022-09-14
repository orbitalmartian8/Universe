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

        # This worked but had deprecation warnings!
        # label1 = Gtk.Label("Welcome to DTOS! Need help using DTOS or customizing it?")
        label1 = Gtk.Label(label="Welcome to Universe!")
        label1.set_hexpand(True)

        label2 = Gtk.Label(label="Your hub to do basically everything.")
        label2.set_hexpand(True)

        label3 = Gtk.Label()
        label4 = Gtk.Label()

        button1 = Gtk.Button(label="About Universe")
        button1.set_hexpand(True)
        button1.connect("clicked", self.on_button1_clicked)

        button2 = Gtk.Button(label="Knowledge Base")
        button2.set_hexpand(True)
        button2.connect("clicked", self.on_button2_clicked)

        button3 = Gtk.Button(label="Contribute")
        button3.set_hexpand(True)
        button3.connect("clicked", self.on_button3_clicked)

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
        grid1.attach(button7, 2, 10, 1, 1)
        grid1.attach(label4,  0, 10, 3, 1)

        self.add(frame1)
        frame1.add(grid1)

    def on_button1_clicked(self, widget):
        print("User chose: About Universe")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe"])

    def on_button2_clicked(self, widget):
        print("User chose: Knowledge Base")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe"])

    def on_button3_clicked(self, widget):
        print("User chose: Contribute")
        subprocess.run(["xdg-open", "https://github.com/LinuxGamer/Universe/blob/main/Docs/CONTRIBUTE.md"])

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

win1 = MyWindow1()


win1.connect("destroy", Gtk.main_quit)


win1.show_all()
Gtk.main()
