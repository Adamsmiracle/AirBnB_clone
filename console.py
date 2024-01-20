#!/usr/bin/python3
"""
model for the interface
"""
import cmd


class HBNBCommand(cmd.Cmd):
    """

    Args:
        cmd (_class_): _for creating command line interface for the user_
    """
    prompt = "(hbnb)"

    def do_quit(self, *args):
        """
        functions to close the program
        """
        return True

    def help_quit(self, *args):
        """
        help info on the quit command
        """
        print("quit command exits the programm")

    def do_EOF(self, *args):
        """
        function for the end of file
        """
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()
