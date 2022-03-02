#!/usr/bin/python3
""""""
import cmd
import sys
from models import storage
from models.base_model import BaseModel

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

    def do_create(self, arg):
        """
        Crea una nueva instancia si los argumentos son validos.
        """
        argum = arg.split()
        if arg == "" or arg is None:
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        elif storage.classes():
            nuevaInstancia = eval("{}()".format(argum[0]))
            nuevaInstancia.save()
            print(nuevaInstancia.id)

    def do_show(self, arg):
        """
        Imprime la representancion de la cadena de una instancia
        """
        argum = arg.split(' ')
        if arg == "" or arg is None:
            print("** class name missing **")
        elif argum[0] not in storage.classes():
            print("** class doesn't exist **")
        elif  len(argum) < 2:
            print("** instance id missing **")
        else:
            llave = "{}.{}".format(argum[0], argum[1])
            if llave not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[llave])

    def do_destroy(self, arg):
        """
        Elimina una instancia según el nombre de la clase y el id.
        """
        argum = arg.split(' ')
        if arg == "" or arg is None:
            print("** class name missing **")
        elif argum[0] not in storage.classes():
            print("** class doesn't exist **")
        elif  len(argum) < 2:
            print("** instance id missing **")
        else:
            llave = "{}.{}".format(argum[0], argum[1])
            if llave not in storage.all():
                print("** no instance found **")
            else:
                storage.all().pop(llave)
                storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
