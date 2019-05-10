class ClassFinder(object):

    def __init__(self):
        self.compo_1_to_1 = []
        self.aggr_1_to_1 = []
        self.compo_1_to_many = []
        self.aggr_1_to_many = []
        self.association_list = []
        self.dependency_list = []

    def get_class_name(self, class_array):
        for listItem in class_array:
            if "class" in listItem:
                temp_class = listItem[:listItem.index(" {")]
                class_name = temp_class.split(' ')[1]
                return class_name

    def get_attributes(self, class_array, output_array):
        attributes = []
        for listItem in class_array:
            if ":" in listItem and "(" not in listItem:
                result = listItem.split(' ')
                attributes.append(result[4])
        num_attribute = len(attributes)
        output_array.append(num_attribute)
        return attributes

    def get_methods(self, class_array, output_array):
        methods = []
        for listItem in class_array:
            if "(" in listItem:
                methods.append(listItem[:listItem.index("\n") - 2].strip())
        num_method = len(methods)
        output_array.append(num_method)
        return methods

        # Luna

    def get_relationship(self, class_name, relation_array):
        temp_relationship = []
        for a_relationship in relation_array:
            r_class_name = a_relationship.split(" ")
            first_c_name = r_class_name[0]
            second_c_name = r_class_name[-1].replace("\n", "")
            if class_name == first_c_name:
                temp_relationship += self.identify_r_type(a_relationship,
                                                          second_c_name)
        return temp_relationship

        # Luna

    def identify_r_type(self, a_relationship, name):
        a_r = ''
        dictionary = {"*--": "self.compo_1_to_1.append(name)",
                      "o--": "self.aggr_1_to_1.append(name)",
                      "<--": "self.association_list.append(name)",
                      "<..": "self.dependency_list.append(name)",
                      '"1"*--"many"': "self.compo_1_to_many.append"
                                      "(name)",
                      '"1"o--"many"': "self.aggr_1_to_many.append"
                                      "(name)"}
        temp = a_relationship.split(" ")
        if len(temp) == 3:
            for key in dictionary:
                if temp[1] == key:
                    exec(dictionary[key])

        if self.compo_1_to_1 is not None:
            for i in self.compo_1_to_1:
                a_r += "        # self. my_" + i.lower() + " -> " + i \
                    + "\n" + "        self." + i.lower() + " = " + "None\n"
        if self.compo_1_to_many is not None:
            for i in self.compo_1_to_many:
                a_r += "        # self. my_" + i.lower() + ": list" + " -> "\
                      + name + "\n" + "        self." + i.lower() + " = "\
                      + "None\n"
        return a_r
