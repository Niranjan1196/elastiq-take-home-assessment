class AssertionHelper:

    def verify_strings_equal(self, expected_string, actual_string):
        # Compare the expected_string with actual_string
        if expected_string == actual_string:
            print(f"Strings matched: Expected string: '{expected_string}' with actual string: '{actual_string}'")
        else:
            print(f"Strings do not match. Expected: '{expected_string}', but got: '{actual_string}'")