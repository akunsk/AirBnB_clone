#!/usr/bin/python3
"""
    Console entry point for Airbnb
"""

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb) '

    def emptyline(self):
        """ Called when the enter button is hit without an input"""
        if self.lastcmd:
            self.lastcmd = ""
            return self.onecmd('\n')

    def do_quit(self, arg):
        sys.exit(1)

    def do_EOF(self, arg):
        sys.exit(1)

    def help_quit(self):
        print('Quit command to exit the program')

    def help_EOF(self):
        print('EOF exits the program')


if __name__ == '__main__':
    HBNBCommand().cmdloop()
