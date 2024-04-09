import unittest


def is_palindrome(value):
      
    if not isinstance(value, str):
        value = str(value)
    
    clean_value = ''.join(char.lower() for char in value if char.isalnum())
    
    if clean_value:
        return clean_value == clean_value[::-1]
    else:

        return True

class TestIsPalindrome(unittest.TestCase):
    def test_with_a(self):
        input = "a"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_ala(self):
        input = "ala"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_neuquen(self):
        input = "neuquen"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_hola(self):
        input = "hola"
        result = is_palindrome(input)
        self.assertFalse(result)

    def test_with_spaces(self):
        input = "anita lava la tina"
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_case_insensitivity(self):
        input = "La ruta nos aportó otro paso natural"
        result = is_palindrome(input)
        self.assertFalse(result)

    def test_with_special_characters(self):
        input = "¡Hola, qué tal!"
        result = is_palindrome(input)
        self.assertFalse(result)

    def test_with_empty_string(self):
        input = ""
        result = is_palindrome(input)
        self.assertTrue(result)

    def test_with_different_data_types(self):
        input_list = [1, 2, 3, 2, 1]
        result = is_palindrome(input_list)
        self.assertTrue(result)

unittest.main()