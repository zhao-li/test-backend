"""Define Batch Transaction Upload File Validator"""
import magic


class Validator():
    """
    A validator for batch transactdion upload file
    Input: Django In-Memory File Object
    Example:
        validator = UploadFileValidator(request.FILES['file'])
        validator.validity()
    """

    WHITELIST_OF_FILETYPES = [
        'text/csv',
        'text/plain',
    ]
    WHITELIST_OF_FILE_HEADERS_AND_CONTENT = [
        'UTF-8 Unicode (with BOM) text, with very long lines',
    ]

    def __init__(self, file):
        self.file = file

    def validity(self):
        return(
            self._filetype_validity()
            and self._file_headers_and_content()
        )

    def _filetype_validity(self):
        return self.file.content_type in self.WHITELIST_OF_FILETYPES

    def _file_headers_and_content(self):
        return(
            magic.from_buffer(self.file.read()) in
            self.WHITELIST_OF_FILE_HEADERS_AND_CONTENT
        )

