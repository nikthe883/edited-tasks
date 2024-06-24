# imports

import re

class TextCleaner:
    """A class used to clean text data"""

    @staticmethod
    def clean_new_line(text):
        """
        Cleans the given text by stripping leading and trailing whitespace.

        Parameters
        ----------
        text : str
            The text to be cleaned.

        Returns
        -------
        str
            The cleaned text.
        """

        return text.strip()
    
    @staticmethod
    def clean_text_list_elements_new_line(list_elements, start=0):
        """
        Cleans a list of text elements by stripping leading and trailing whitespace from each element, starting from a specified index.

        Parameters
        ----------
        list_elements : list of str
            The list of text elements to be cleaned.
        start : int, optional
            The index from which to start cleaning the list elements (default is 0).

        Returns
        -------
        list of str
            A list of cleaned text elements.
        """


        return [TextCleaner.clean_new_line(element) for element in list_elements[start:]]
    
    @staticmethod
    def clean_text_only_digits(text):
        """
        Extracts and returns only the numeric value from the given text.

        Parameters
        ----------
        text : str
            The text to be cleaned and from which to extract the numeric value.

        Returns
        -------
        str
            The extracted numeric value.
        """

        numeric_value = re.search(r'\d+(\.\d+)?', TextCleaner.clean_new_line(text)).group()
        return numeric_value

