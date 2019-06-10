from validator import Validator


class OutputClass:

    def __init__(self, class_finder_object):
        self.classFinder = class_finder_object
        self.relationship_list = []
        self.class_list = []
        self.result = ""

    def output_class(self, class_item):
        self.add_class_name(class_item)
        self.add_attribute(class_item)
        self.add_method(class_item)
        return self.result

    def add_class_name(self, class_item):
        class_name = self.classFinder.get_class_name(class_item)
        # self.result += self.add_relationship(class_name)
        self.classFinder.class_name_list.append(class_name)
        if self.check_class_name(class_name):
            self.result = "class " + class_name + ":\n    def __init__(self"

    def check_class_name(self, class_name):
        result = False
        if Validator.validate_class_name(class_name):
            result = True
        return result

    def add_attribute(self, class_item):
        result = ""
        attribute_list = self.classFinder.get_attributes(class_item)
        if len(attribute_list) == 0:
            result += "        pass\n"
        else:

            for parameter in attribute_list:
                result += ", " + parameter
            result += "):\n"

            for eachItem in attribute_list:
                result += self.check_attribute(eachItem, result)
            self.result += result

    def check_attribute(self, each_item, result):
        try:
            if Validator.validate_attribute_name(each_item):
                result += '        self.' + \
                         each_item + ' = ' + each_item + '\n'
            else:
                raise NameError('Invalid name: ' + each_item)
        except NameError as e:
            print(e)
        return result

    def add_method(self, class_item):
        method_list = self.classFinder.get_methods(class_item)
        for listItem in method_list:
            if self.check_method(listItem):
                self.result += '\n'
                self.result += 'def ' + listItem + '(self):\n     # Todo: inco' \
                                              'mplete\n        pass\n'
            else:
                self.result += "# method name is invalid\n"

    def check_method(self, list_item):
        return Validator.validate_method_name(list_item)

    def add_relationship(self, class_name):
        result = ""
        relationship_list = self.classFinder.get_relationship(class_name, self.relationship_list)
        for item in relationship_list:
            result += item
        self.result = result
