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
    list_class = ['BaseModel']

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

    def do_update(self, arg):
        """
        """
        argum = arg.split()
        args_size = len(argum)

        if arg == "" or arg is None:
            print("** class name missing **")
        elif argum[0] not in storage.classes():
            print("** class doesn't exist **")
        elif  len(argum) < 2:
            print("** instance id missing **")
        else:
            llave = "{}.{}".format(argum[0], argum[1])
            busqueda = storage.all().get(llave)
            if busqueda is None:
                print("** no instance found **")
            elif args_size == 2:
                    print('** attribute name missing **')
            elif args_size == 3:
                print('** value missing **')
            else:


    def do_all(self, arg):
        """Prints all string representation of all instances based or not
        on the class name.do_all
        """
        args = arg.split()
        list_strings = []
        objects = storage.all()
        for key in objects.keys():
            value = objects.get(key)
            if args:
                # por si pide objetos de alguna clase
                if args[0] in self.list_class:
                    # para crear algun tipo de objeto
                    if value.__class__.__name__ == args[0]:
                        # si la clase de objeto coincide
                        list_strings.append(value.__str__())
                else:
                    print("** class doesn't exist **")
                    return
            else:
                list_strings.append(objects[key].__str__())
        print(list_strings)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
