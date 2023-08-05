#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel
import re
import json


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

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        class_map = storage.classes()

        if not args:
            print("** class name missing **")
        elif args is not class_map:
            print("** class doesn't exist **")
        else:
            ins = class_map[args]()
            ins.save()
            print(ins.id)

    def do_show(self, args):
        """print rep of an instance"""
        class_map = storage.classes()

        if not args:
            print("** class name missing **")
        else:
            words = args.split(' ')
            if words[0] not in class_map:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{words[0]}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all[key])

    def do_destroy(self, args):

        class_map = storage.classes()

        if is not args:
            print("** class name missing **")
        else:
            words = args.split(" ")
            if words[0] not in class_map:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{words[0]}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, args):
        class_map = storage.classes()

        if args != "":
            words = args.split(" ")
            if words[0] not in class_map:
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)

        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, args):
        if not args:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        if not match:
            print("** class name missing **")
            return

        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)

        if classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        elif not attribute:
            print("** attribute name missing **")
        elif not value:
            print("** value missing **")
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                if hasattr(storage.all()[key], attribute) and \
                   attribute not in ["id", "created_at", "updated_at"]:
                    try:
                        value = eval(value)
                    except NameError:
                        pass
                    setattr(storage.all()[key], attribute, value)
                    storage.all()[key].save()



if __name__ == "__main__":
    HBNBCommand().cmdloop()



