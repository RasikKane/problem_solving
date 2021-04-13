import unittest


def is_sum_present_in_list(int_list):
    """
    :param int_list:
    :return True or False:

    The is_sum_present_in_list() function accepts a list of integers and check if the sum of any two integers
    is not contained in the list. If the above criteria is met, then True is returned, else False is returned.
    It uses a brute force to iterate elements one-by-one and check if their sum is present in list or not.
    If the sum is present, then a boolean flag ('is_sum_present') is set to true. The termination of the program
    is dependant on this boolean flag.
    """
    try:
        # Check if only list is provided as args
        if not isinstance(int_list, list):
            return False

        # Check if list contains 3 or more than 3 elements
        if len(int_list) < 3:
            return False

        # Check if all the elements in the list are integers (not chars, floating points etc)
        if not all(isinstance(item, int) for item in int_list):
            return False

        # Declare a flag with default value as false for checking the presence of sum in list
        is_sum_present = False

        # Using brute force to iterate element by element
        for elem1 in range(0, len(int_list)):
            for elem2 in range(elem1 + 1, len(int_list)):
                elem1_val = int_list[elem1]
                elem2_val = int_list[elem2]
                if (elem1_val + elem2_val) in int_list:
                    
                    # if sum is present in list then setting the flag as true
                    is_sum_present = True
                    break

            # If element is found then criteria is not satisfied
            if is_sum_present:
                return not is_sum_present

        # If element is not found then criteria is satisfied
        return not is_sum_present

    except Exception as exception:
        print("Error in is_sum_present_in_list() function:", exception)
        return False


"""
----------------------------------- UNIT TESTS -----------------------------------------
"""


class TestSumPresentInList(unittest.TestCase):
    def test_satisfies_criteria(self):
        self.assertTrue(is_sum_present_in_list([4, 5, 15, 2, 8]),
                        "Should satisfy the criteria as no pair is present")
        self.assertTrue(is_sum_present_in_list([-4, -5, -15, -2, -8]),
                        "Should satisfy the criteria as no pair is present")
        self.assertTrue(is_sum_present_in_list([-3, 8, -5]),
                        "Should satisfy the criteria as no pair is present")

    def test_does_not_satisfies_criteria(self):
        self.assertFalse(is_sum_present_in_list([8, 7, 5, 3]),
                         "Should not satisfy the criteria as pair is present")
        self.assertFalse(is_sum_present_in_list([-8, -3, -5]),
                         "Should not satisfy the criteria as pair is present")
        self.assertFalse(is_sum_present_in_list([-8, 3, -5]),
                         "Should not satisfy the criteria as pair is present")

    def test_list_length_validity(self):
        self.assertFalse(is_sum_present_in_list([]), "Should not satisfy the criteria as list is empty")
        self.assertFalse(is_sum_present_in_list([2]),
                         "Should not satisfy the criteria as list contains only one element")
        self.assertFalse(is_sum_present_in_list([2, 3]),
                         "Should not satisfy the criteria as list contains only two elements")

    def test_list_elements_validity(self):
        self.assertFalse(is_sum_present_in_list(['a', 2, 3]),
                         "Should not satisfy the criteria as list contains invalid elements")
        self.assertFalse(is_sum_present_in_list([2, 3, 3.25]),
                         "Should not satisfy the criteria as list contains invalid elements")

    def test_function_args_validity(self):
        self.assertFalse(is_sum_present_in_list(12345),
                         "Should not satisfy the criteria as the function arguments are invalid")
        self.assertFalse(is_sum_present_in_list([[1, 2, 3, 4, 5], [1, 2, 3], [1, 2, 3, 4]]),
                         "Should not satisfy the criteria as the function arguments are invalid")


if __name__ == '__main__':
    unittest.main()
