#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):
    
    prompt = "(hbnb)"

    def do_EOF(self, args):
        """exit the program"""

        print()
        """Print a newline before exiting"""
        return True

    def do_quit(self, args):
        """exit the program"""
        return True

if __name__ == "__main__":
    HBNBCommand().cmdloop()



