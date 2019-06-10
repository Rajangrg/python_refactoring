import class_finder
import File_reader
import output_class


class PrintClass:

    def __init__(self):
        self.classFinder = class_finder.ClassFinder()
        self.fileReader = File_reader.FileReader()
        self.outputClass = output_class.OutputClass(self.classFinder)
        self.relationship_list = []
        self.class_list = []

    def class_handler(self, file_name):
        self.fileReader.class_handler(file_name)
        self.relationship_list = self.fileReader.relationship_list
        self.class_list = self.fileReader.class_list

    def output_classes(self, file_dir):
        files = []
        for classItem in self.class_list:
            files.append(file_dir + self.classFinder.get_class_name(classItem) + '.py')
        for classItem, file in zip(self.class_list, files):
            result = self.outputClass.output_class(classItem)
            self.classFinder = self.outputClass.classFinder
            with open(file, "w") as output:
                output.write(result)
        print("Files are created")

    def get_all_num(self):
        result = self.classFinder.get_all_num()
        return result
