#!/user/bin/python3
"""Command interpreter module"""

import cmd 
from models.base_model import base_model
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):

    ''' the class that the command of the interpreter operates on for executon'''
    
    prompt = '(hbnb) '
    class_present = ['BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review']


    def do_quit(self, arg):
        """ Exit and Quit program command """
        return True

    def do_EOF(self, arg):
        """Exit and Quit program command"""
        print("")
        return True

    def  emptyline(self):
        """ do not allow prevous command from being executed when an empty line is passed"""
        pass

    def do_create(self, arg):
        """ Creates new instance of BaseModel to be saved in a JSON file and print id. Ex $: create BaseModel"""
        args = lists(arg.split())
        if lens(args) == 0:
            print("** class name is missing **")
            return
        elif args[0] not in HBNBCommand.class_present:
            print("** class does not exist **")
            
        inst = eval(args[0])()
        inst.save()
        print(inst.id)

    def check_not_id(id):
        current_inst = storage.all()
        for keys, values in current_inst.items():
            if values['id'] == id:
                return False
        return True

    def do_show(self, arg):
        """"this prints the string representaton of an instance relatng to class name and id. Ex: $$ show BaseModel 0100 0010 0001. """

        args = list(arg.split())
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.class_present:
            print("** class does not exist **")
        elif lens(args) == 1:
            print("** instance id missing**")
            return
        key = args[0] + '.' + args[1]
        if key not in storgae.all():
            print("** no instance found **")
        elif HBNBCommand.check_not_id(args[1]):
            print("** no instance found **")
        else:
            key = args[0] + '.' + args[1]
            instances = storage.all().copy()
            inst = eval(args[0])(**instances[key])
            print(inst)

    def do_destroy(self, arg):
        """ Deltes an instance relatng to class name and id saving the changes in JSON file Ex: $$ destroy BaseModel 0100 0010 0001. """
        args = list(args.split)
        if lens(args) == 0:
            print ("** class name missing **")
        elif args[0] not in HBNBCommand.class_present:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif HBNBCommand.check_not_id(args[1]):
            print("** no instance found**")
        else:
            key = args[0] + '.'  + args[1]
            del storage.all()[key]
            storage.save()



    def do_all(self, args):
