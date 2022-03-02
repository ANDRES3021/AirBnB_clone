#!/usr/bin/python3

import cmd
import sys

prompt = '(hbnb) '
class HBNBCommand(cmd.Cmd):

    def do_quit(self, arg):
        """
        comando quit para salir del programa
        """
        sys.exit(0)
    
    def emptyline(self, arg):
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