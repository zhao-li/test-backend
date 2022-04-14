"""Define tests for Batch Transaction Upload File Validator"""
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import tag, TestCase
from ...services.validator import Validator


class ValidatorTest(TestCase):
    """Test Batch Transaction Upload File Validator"""

    @tag('unit')
    def test_validating_valid_file(self):
        """test validating valid batch transaction upload file"""

        current_path = os.path.dirname(__file__)
        read_mode = 'r'
        binary_format = 'b'
        with open(
                os.path.join(current_path, 'portfolio.csv'),
                read_mode + binary_format
        ) as file_pointer:
            file = SimpleUploadedFile(
                file_pointer.name,
                file_pointer.read(),
            )
            validator = Validator(file)
            valid = True
            self.assertEqual(
                validator.validity(),
                valid
            )

    @tag('unit')
    def test_validating_invalid_file(self):
        """test validating valid batch transaction upload file"""

        current_path = os.path.dirname(__file__)
        read_mode = 'r'
        binary_format = 'b'
        with open(
                os.path.join(current_path, 'bad_file.jpg'),
                read_mode + binary_format
        ) as file_pointer:
            file = SimpleUploadedFile(
                file_pointer.name,
                file_pointer.read(),
            )
            validator = Validator(file)
            invalid = False
            self.assertEqual(
                validator.validity(),
                invalid
            )

