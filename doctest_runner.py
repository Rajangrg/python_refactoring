# from test.unit_test_validator import TestDataExtraction
# import unittest


def doc_test():
    import doctest
    doctest.testfile("test/doc_test_validator.txt", verbose=1)


# def unit_test():  # pragma: no cover
#     the_suite = unittest.TestSuite()
#     the_suite.addTest(unittest.makeSuite(TestDataExtraction))
#     return the_suite


if __name__ == "__main__":
    doc_test()
