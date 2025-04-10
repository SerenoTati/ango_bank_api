class UrlDto:
    """
    This class represents a Data Transfer Object (DTO) for URLs.
    It contains the URL and its corresponding exchange rate.
    """

    def __init__(self, url: str):
        self.url = url

        def __sanitize_url(self):
            """
            A private method to sanitize the URL by stripping whitespace
            and ensuring it is in lowercase.
            """
            self.url = self.url.strip().lower()

    def get_url(self):
            """
            A getter method to retrieve the sanitized URL.
            """
            self.__sanitize_url()
            return self.url