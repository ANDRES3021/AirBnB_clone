#!/usr/bin/python3
""""""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = '(hbnb) '
    
    def do_quit(self, arg):
        """
        Quit command to exit the program
        """
        sys.exit(0)
    
    def emptyline(self):
        """
        si pasan un ina linea vacia seguida de un enter no hace nada
        """
        pass


    def do_EOF(self, arg):
        """
        comando para salir una vez leido todo
        """
        sys.exit(0)

    


if __name__ == '__main__':
    HBNBCommand().cmdloop()