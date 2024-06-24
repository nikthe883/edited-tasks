
# imports

from .text_cleaner import TextCleaner

class ProductExtractor:
    """ A class used to extract and clean product-related data from web pages."""

    @staticmethod
    def extract_name_css(response):
        """
        Extracts and cleans the product name from the given response using CSS selectors.

        Parameters
        ----------
        response : scrapy.http.Response
            The response object containing the HTML of the web page.

        Returns
        -------
        str
            The cleaned product name.
        """

        uncleaned_text = response.css('h1::text').get()
        return TextCleaner.clean_new_line(uncleaned_text)
    
    @staticmethod
    def extract_price_css(response):
        """
        Extracts and cleans the product price from the given response using CSS selectors.

        Parameters
        ----------
        response : scrapy.http.Response
            The response object containing the HTML of the web page.

        Returns
        -------
        float
            The cleaned product price.
        """

        uncleaned_text = response.css('span.value::text').get()
        return float(TextCleaner.clean_text_only_digits(uncleaned_text))
    
    @staticmethod
    def extract_colour_css(response):
        """
        Extracts and cleans the product colour from the given response using CSS selectors.

        Parameters
        ----------
        response : scrapy.http.Response
            The response object containing the HTML of the web page.

        Returns
        -------
        str
            The cleaned product colour.
        """
                
        uncleaned_text = response.css('div.colour-picker::attr(data-colorname)').get()
        return TextCleaner.clean_new_line(uncleaned_text)
    
    @staticmethod
    def extract_sizes_css(response):
        """
        Extracts and cleans the product sizes from the given response using CSS selectors.

        Parameters
        ----------
        response : scrapy.http.Response
            The response object containing the HTML of the web page.

        Returns
        -------
        list of str
            A list of cleaned product sizes.
        """

        uncleaned_list = response.css('select#plp-select option::text').getall()
        return TextCleaner.clean_text_list_elements_new_line(uncleaned_list,1)
    
    @staticmethod
    def extract_reviews_count_text_json(json_data):
        """
        Extracts the reviews count from the given JSON data.

        Parameters
        ----------
        json_data : dict
            The JSON data containing product information.

        Returns
        -------
        int
            The reviews count.
        """

        return  int(json_data.get('AggregateRating', {}).get('reviewCount'))
    
    @staticmethod
    def extract_reviews_score_text_json(json_data):
        """
        Extracts and cleans the reviews score from the given JSON data.

        Parameters
        ----------
        json_data : dict
            The JSON data containing product information.

        Returns
        -------
        float
            The cleaned reviews score.
        """

        uncleaned_text = json_data.get('AggregateRating', {}).get('ratingValue')
        return  float(TextCleaner.clean_new_line(uncleaned_text))
            
        
