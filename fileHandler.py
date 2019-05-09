import docx
from validator import Validator
import class_finder
import os


class PrintClass:

    def __init__(self):
        self.x = class_finder.ClassFinder()
        self.relationship_list = []
        self.class_name_list = []
        self.num_all_attribute_list = []
        self.num_all_method_list = []
        self.class_list = []

    # Luna: load data from .docx file
    # Clement: exception
    def read_word_file(self, file_name):
        try:
            if os.path.isfile(file_name):
                file = docx.Document(file_name)
                content = []
                for para in file.paragraphs:
                    content.append(para.text + "\n")
                return content
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print("Cannot find this file")

    # Clement: load data from .txt file
    # Rajan: exception
    def read_txt_file(self, file_name):
        try:
            if os.path.isfile(file_name):
                file = open(file_name, 'r').readlines()
                return file
            else:
                raise FileNotFoundError
        except FileNotFoundError:
            print(".txt File doesn't exist")

    def class_handler(self, file_name):
        class_list = [[]]
        file_content = []
        if ".txt" in file_name[-4:]:
            file_content = self.read_txt_file(file_name)
        elif ".docx" in file_name[-5:]:
            file_content = self.read_word_file(file_name)
        for i, m in enumerate(file_content[1:-1]):
            if m == "\n":
                if i != len(file_content[1:-1]) - 1:
                    class_list.append([])
            else:
                class_list[-1].append(m)
        self.relationship_list = class_list[0]
        self.class_list = class_list[1:]
        return self.class_list

    def return_string(self, array, addon):

        result = ""
        for line in array:
            if addon is None:
                result += line
            else:
                result += addon + line
        return result

    def validateAtt(self, array):

        result = ""
        for line in array:
            try:
                if Validator.validate_attribute_name(line):
                    result += self.attrib_line(line)
                else:
                    raise NameError('Invalid name: ' + line)
            except NameError as e:
                print(e)

        return result

    def attrib_line(self, line):
        result = '        self.' + \
                  line + ' = ' + line + '\n'
        return result
    # Clement

    def output_class(self, class_item):

        class_name = self.x.get_class_name(class_item)
        self.class_name_list.append(class_name)
        attribute_list = self.x.get_attributes(class_item, self.num_all_attribute_list)
        method_list = self.x.get_methods(class_item, self.num_all_method_list)
        relationship_list = self.x.get_relationship(class_name, self.relationship_list)
        result = "class " + class_name + ":\n    def __init__(self"

        result += self.return_string(attribute_list, ", ")

        result += '):\n'

        if Validator.validate_class_name(class_name):
            pass

            result += self.validateAtt(attribute_list)

        if len(attribute_list) == 0:
            result += "        pass\n"

            result += self.return_string(relationship_list, None)

        for listItem in method_list:
            if Validator.validate_method_name(listItem):
                result += '\n'
                result += 'def ' + listItem + '(self):\n     # Todo: inco' \
                                              'mplete\n        pass\n'
            else:
                result += "# method name is invalid\n"
        return result

    def output_classes(self, file_dir):
        files = []
        for classItem in self.class_list:
            files.append(file_dir + self.x.get_class_name(classItem) + '.py')
        for classItem, file in zip(self.class_list, files):
            result = self.output_class(classItem)
            with open(file, "w") as output:
                output.write(result)
        print("Files are created")

    def get_all_num(self):
        class_num = len(self.class_name_list)
        attribute_num = sum(self.num_all_attribute_list)
        method_num = sum(self.num_all_method_list)
        all_num = [class_num, attribute_num, method_num]
        return all_num
