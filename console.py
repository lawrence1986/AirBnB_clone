#!/usr/bin/python3
"""This is the module for entry points"""

import cmd
from models import storage
from models.base_model import BaseModel
import re
import json


class HBNBCommand(cmd.Cmd):
    """The class for command interpreter."""
    
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

        if not args:
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
        match = re.search(rex, args)
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

    def do_count(self, args):

        class_map = storage.classes()
        words = args.split(" ")
        class_name = words[0]

        if not class_name:
            print("** class name missing **")
        elif class_name not in class_map:
            print("** class doesn't exist **")
        else:
            matches = [
                    k for k in storage.all() if k.startswith(
                class_name + ".")]
            print(len(matches))

    def _precmd(self, arg):
        """Intercepts commands to test for class.syntax()"""
        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", arg)
        if not match:
            return arg

        classname, method, args = match.groups()
        uid, attr_or_dict = extract_uid_and_args(args)

        attr_and_value = ""

        if method == "update" and attr_or_dict:
            update_dict_match = re.search('^({.*})$', attr_or_dict)
            if update_dict_match:
                self.update_dict(classname, uid, update_dict_match.group(1))
                return ""

            attr_and_value = extract_attr_and_value(attr_or_dict)

            command = f"{method} {classname} {uid} {attr_and_value}"
            self.onecmd(command)
            return command

        def extract_uid_and_args(args):

            match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
            if match_uid_and_args:
                uid = match_uid_and_args.group(1)
                attr_or_dict = match_uid_and_args.group(2)
            else:
                uid = args
                attr_or_dict = False

                return uid, attr_or_dict

        def extract_attr_and_value(attr_or_dict):
            match_attr_and_value = re.search(
            '^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)

            if match_attr_and_value:
                attr_and_value = (match_attr_and_value.group(1) or "") + " " + (match_attr_and_value.group(2) or "")
            else:
                attr_and_value = ""

                return attr_and_value

        def update_dict(self, classname, uid, s_dict):
            """Helper method for update() with a dictionary."""
            s = s_dict.replace("'", '"')
            d = json.loads(s)
            if not classname:
                print("** class name missing **")
            elif classname not in storage.classes():
                print("** class doesn't exist **")
            elif uid is None:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(classname, uid)
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    attributes = storage.attributes()[classname]
                    for attribute, value in d.items():
                        if attribute in attributes:
                            value = attributes[attribute](value)
                            setattr(storage.all()[key], attribute, value)
                            storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
