#!/usr/bin/env python3

import sys
import cmd
from models.base_model import BaseModel
import models

class HBNBCommand(cmd.Cmd):
	prompt = "(hbnb) "

	def do_quit(self, arg):
		"""Quit command to exit the program
		"""        
		sys.exit()

	def do_EOF(self, arg):
		"""EOF command to exit the program
		"""
		sys.exit()

	def emptyline(self):
		pass

	def do_create(self, arg):
		if len(arg) <= 0:
			print("** class name missing **")
		else:
			if arg == "BaseModel":
				new_obj = BaseModel()
				new_obj.save()
				print(new_obj.id)
			else:
				print("** class doesn't exist **")
	
	def do_show(self, arg):
		if len(arg) <= 0:
			print("** class name missing **")
		else:
			arguments = arg.split()
			if len(arguments) == 1:
				print("** instance id missing **")
			else:
				if arguments[0] != "BaseModel":
					print("** class doesn't exist **")
				else:
					objects = models.storage.all()
					try:
						print(objects[".".join(arguments)])
					except:
						print("** no instance found **")

	def do_destroy(self, arg):
		if len(arg) <= 0:
			print("** class name missing **")
		else:
			arguments = arg.split()
			if arguments[0] != "BaseModel":
				print("** class doesn't exist **")
			else:
				if len(arguments) == 1:
					print("** instance id missing **")
				else:
					objects = models.storage.all()
					try:
						del objects[".".join(arguments)]
						models.storage.save()
						models.storage.reload()
					except:
						print("** no instance found **")
	
	def do_all(self, arg):
		my_arr = []
		if len(arg) > 0:
			if arg == "BaseModel":
				my_dict = models.storage.all()
				for key, value in my_dict.items():
					my_arr.append(str(value))
				print(my_arr)
			else:
				print("** class doesn't exist **")
		else:
			my_dict = models.storage.all()
			for key, value in my_dict.items():
				my_arr.append(str(value))
			print(my_arr)
	
	def do_update(self, arg):
		arguments = arg.split()
		class_name = arguments[0]
		id = arguments[1]
		attribute_name = arguments[2]
		attribute_value = arguments[3]
		my_dict = models.storage.all()
		my_dict[class_name+"."+id].attribute_name = attribute_value
		print(my_dict[class_name+"."+id].attribute_name)

if __name__ == "__main__":
	HBNBCommand().cmdloop()