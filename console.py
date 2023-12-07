#!/usr/bin/python3
"""
Created on: Dec. 06, 2023
@authors: Bukola Egberongbe
          Jamiu Olukayode Shomoye
"""
import cmd
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    def do_EOF(self, line):
        return True
    def help_EOF(self):
        pass
    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()
    def emptyline(self):
        return

    def do_create(self, line):
        if HBNBCommand.identchars == "BaseModel":
            my_model = BaseModel()
            my_model.save()
            print(my_model.id)
        else:
            HBNBCommand.default(self, line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
