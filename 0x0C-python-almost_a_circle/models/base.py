#!/usr/bin/python3
"""
The base class of every other classes in this project
"""


class Base:
    """
    A class named Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the instance of a variable
        """
        self.id = id
        if self.id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        """
        A static method that returns the JSON string representation of
        list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        import json
        """
        A static method that returns the list of the JSON string
        representation json_string
        """
        if json_string is None or len(json_string) == 0:
            return '[]'
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        import sys
        """
        A class method that writes the JSON string representation of list_objs
        to a file:
        """
        dict_list = []
        if list_objs is None:
            list_objs = dict_list

        if list_objs is not None:
            for obj in list_objs:
                dict_list.append(cls.to_dictionary(obj))

            file_name = f"{cls.__name__}.json"

            with open(file_name, "w") as file:
                json_str = cls.to_json_string(dict_list)
                file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
        A class that returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy_instance = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy_instance = cls(1)

        dummy_instance.update(**dictionary)

        return dummy_instance

    def update(self, *args, **kwargs):
        """
        A method that sets the values of attributes
        """
        attribute = ['id', 'width', 'height', 'size', 'x', 'y']

        if attr:
            for attr, value in zip(attribute, args):
                setattr(self, attr, value)

        for key, value_2 in kwargs.item():
            if key in attribute:
                setattr(self, key, value_2)

    def load_from_file(cls):
        """
        class method that returns a list of instances
        """
        file_name = f"cls.__name__.json"
        instances = []

        try:
            with open(file_name, "r") as file:
                json_obj = cls.from_json_string(file.read())

                for obj in json_obj:
                    instance = cls.create(**obj)
                    instances.append(instance)
        except Exception:
            pass

        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        import csv
        """
        save to a CSV file
        """
        file_name = f"cls.__name__.csv"

        with open("filename", "w") as file:
            writer = csv.writer(file)

            if cls.__name__ == "Rectangle":
                for ob in list_objs:
                    writer.writerow([ob.id, ob.width, ob.height, ob.x, ob.y])
            if cls.__name__ == "Square":
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        import csv
        """
        loads a CSV file
        """
        file_name = f"cls.__name__.csv"
        li_st = []

        try:
            with open(file_name, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = {
                            'id': int(row[0]),
                            'width': int(row[1]),
                            'height':int(row[2]),
                            'x': int(row[3]),
                            'y': int(row[4])
                        }
                    if cls.__name__ == "Square":
                        instance = {
                            'id': int(row[0]),
                            'size': int(row[1]),
                            'x': int(row[2]),
                            'y': int(row[3])
                        }
                    o = cls.create(**instance)

                    li_st.append(o)
        except Exception:
            pass

        return li_st
