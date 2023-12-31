#!/usr/bin/python3
"""
Created on: Dec. 06, 2023
@authors: Bukola Egberongbe
          Jamiu Olukayode Shomoye
"""
import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
import re


class HBNBCommand(cmd.Cmd):
    """ An entry point of the HBNBCommand command
    interpreter.                           """

    prompt = "(hbnb) "

    def default(self, line):
        """default - called when the inputted command starts
        with a class name.

        args:
            line (str): The inputted line string
        """
        if not re.search(r"\.(\w+)\(", line):
            return
        cl_name = line.split(".")[0]
        cmd = line.split(".")[1].split("(")[0]
        term = line.split("(")[1][:-1]

        if cl_name == "":
            print("** class name missing **")
            return
        elif cl_name not in storage.classes():
            print("** class doesn't exist **")
            return

        if cmd == "all":
            self.do_all(cl_name)

        elif cmd == "count":
            count = sum(1 for k, v in storage.all().items() if
                        v.to_dict()["__class__"] == cl_name)
            print(count)

        elif cmd == "show":
            self.do_show(cl_name + " " + term.strip("\""))

        elif cmd == "destroy":
            self.do_destroy(cl_name + " " + term.strip("\""))

        elif cmd == "update":
            # if starts with 'id, {}', then split into id and dict
            if re.match('"[^"]+", {.+}', term):
                term = term.replace("\'", "\"")
                term_dict = json.loads(term.split(", ", 1)[1])
                term_id = cl_name + "." + term.split(", ")[0].strip("\"")
                if term_id not in storage.all().keys():
                    print("** no instance found **")
                    return
                for k, v in term_dict.items():
                    setattr(storage.all()[term_id], k, v)
            # else update at id the attribute with new_value
            else:
                terms = term.split(", ")
                if terms == ['']:
                    print("** instance id missing **")
                    return
                key = "{}.{}".format(cl_name, terms[0].strip("\""))
                if key not in storage.all().keys():
                    print("** no instance found **")
                    return
                if len(terms) < 2:
                    print("** attribute name missing **")
                    return
                if len(terms) < 3:
                    print("** value missing **")
                    return
                self.do_update(cl_name + " " + terms[0].strip("\"") + " " +
                               terms[1].strip("\"") + " " + terms[2])
        else:
            super().default(line)

    def do_update(self, line):
        """Update an instance based on class name and id.\n"""
        if line == "" or line is None:
            print("** class name missing **")
            return
        terms = shlex.split(line, posix=False)
        if terms[0] not in storage.classes():
            print("** class doesn't exist **")
            return
        elif len(terms) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(terms[0], terms[1])
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(terms) < 3:
            print("** attribute name missing **")
            return
        elif len(terms) < 4:
            print("** value missing **")
            return
        terms[3] = terms[3].strip("\"")
        storage.all()[key].__dict__[terms[2]] = terms[3]
        storage.save()

    def do_show(self, line):
        """Prints an instance by id.\n"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(terms) < 2 or terms[1] == "":
                print("** instance id missing **")
            else:
                key = "{}.{}".format(terms[0], terms[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id.\n"""
        if line == "" or line is None:
            print("** class name missing **")
        else:
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(terms) < 2 or terms[1] == "":
                print("** instance id missing **")
            else:
                key = "{}.{}".format(terms[0], terms[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, line):
        """Displays all instances, display all of a class of instances.\n"""
        if line != "":
            terms = line.split(' ')
            if terms[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                obj_list = [str(obj) for key, obj in storage.all().items() if
                            type(obj).__name__ == terms[0]]
                print(obj_list)
        else:
            obj_list = [str(obj) for key, obj in storage.all().items()]
            print(obj_list)

    def do_create(self, line):
        """Creates a new instance.\n"""
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in storage.classes():
            print("** class doesn't exist **")
        else:
            inst = storage.classes()[line]()
            inst.save()
            print(inst.id)

    def do_EOF(self, line):
        """EOF command to exit the program."""
        pass
        return True

    def do_quit(self, line):
        """Quit command to exit the program."""
        return True

    def emptyline(self):
        """method to do nothing when an empty line is inputed.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
