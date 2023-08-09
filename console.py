#!/usr/bin/python3
"""This is the module for entry points"""

import cmd
import re
import json
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """The class for command interpreter."""

    prompt = "(hbnb) "

    def default(self, line):
        """Catch commands if nothing else matches then."""
        self._precmd(line)

    def do_EOF(self, ar):
        """Exit the program"""
        print()
        """Print a newline before exiting"""
        return True

    def do_quit(self, ar):
        """Exit the program"""
        return True

    def do_create(self, ar):
        """Create a new instance of BaseModel"""
        class_map = storage.classes()

        if not ar:
            print("** class name missing **")
        elif ar not in class_map:
            print("** class doesn't exist **")
        else:
            ins = class_map[ar]()
            ins.save()
            print(ins.id)

    def do_show(self, ar):
        """Print representation of an instance"""
        class_map = storage.classes()

        if not ar:
            print("** class name missing **")
        else:
            words = ar.split(' ')
            if words[0] not in class_map:
                print("** class doesn't exist **")
            elif len(words) < 2:
                print("** instance id missing **")
            else:
                key = f"{words[0]}.{words[1]}"
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, ar):
        """Deletes an instance based on the class name and id.
        """

        class_map = storage.classes()

        if not ar:
            print("** class name missing **")
            return

        words = ar.split(" ")

        if words[0] not in class_map:
            print("** class doesn't exist **")
            return

        if len(words) < 2:
            print("** instance id missing **")
            return

        key = f"{words[0]}.{words[1]}"

        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, ar):
        """Prints all string representation of all instances.
        """

        class_map = storage.classes()

        if ar:
            words = ar.split(" ")
            if words[0] not in class_map:
                print("** class doesn't exist **")
            else:
                nl = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == words[0]]
                print(nl)

        else:
            new_list = [str(obj) for key, obj in storage.all().items()]
            print(new_list)

    def do_update(self, ar):
        """Updates an instance by adding or updating attribute.
        """

        if not ar:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, ar)
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
        else:
            key = f"{classname}.{uid}"
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                    attributes = storage.attributes()[classname]
                    if attribute in attributes:
                        value = attributes[attribute](value)
                    elif cast:
                        try:
                            value = cast(value)
                        except ValueError:
                            pass
                    setattr(storage.all()[key], attribute, value)
                    storage.all()[key].save()

    def do_count(self, ar):
        """Counts the instances of a class.
        """

        class_map = storage.classes()
        words = ar.split(" ")
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

    def _precmd(self, ar):

        match = re.search(r"^(\w*)\.(\w+)(?:\(([^)]*)\))$", ar)
        if not match:
            return ar

        classname = match.group(1)
        method = match.group(2)
        args = match.group(3)
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)

        if method == "update" and attr_or_dict:
            match_dict = re.search('^({.*})$', attr_or_dict)
            if match_dict:
                self.update_dict(classname, uid, match_dict.group(1))
                return ""
            attr_and_value = self.extract_attr_and_value(attr_or_dict)
        else:
            attr_and_value = self.extract_attr_and_value(attr_or_dict)
        command = f"{method} {classname} {uid} {attr_and_value}"
        self.onecmd(command)
        return command

    def extract_uid_and_args(self, ar):
        match_uid_and_args = re.search('^"([^"]*)"(?:, (.*))?$', args)
        if match_uid_and_args:
            uid = match_uid_and_args.group(1)
            attr_or_dict = match_uid_and_args.group(2)
        else:
            uid = args
            attr_or_dict = False
        return uid, attr_or_dict

    def extract_attr_and_value(self, attr_or_dict):

        match_attr_and_value = re.search(
                r'^(?:"([^"]*)")?(?:, (.*))?$', attr_or_dict)

        attr = match_attr_and_value.group(1) if match_attr_and_value else ""
        value = match_attr_and_value.group(2) if match_attr_and_value else ""
        return f'"{attr}" {value}'

    def update_dict(self, classname, uid, s_dict):
        """Helper method for update() with a dictionary."""
        if not self.check_and_print_errors(classname, uid):
            return

        d = json.loads(s_dict.replace("'", '"'))
        key = f"{classname}.{uid}"
        attributes = storage.attributes().get(classname, {})

        instance = storage.all().get(key)
        if instance:
            self.update_instance_with_dict(instance, attributes, d)
            instance.save()
        else:
            print("** no instance found **")

    def check_and_print_errors(self, classname, uid):

        if not classname:
            print("** class name missing **")
            return False
        elif classname not in storage.classes():
            print("** class doesn't exist **")
            return False
        elif uid is None:
            print("** instance id missing **")
            return False
        return True

    def update_instance_with_dict(self, instance, attributes, d):

        for attribute, value in d.items():
            value = attributes[attribute](value)
        setattr(instance, attribute, value)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
