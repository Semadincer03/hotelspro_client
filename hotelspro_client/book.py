import requests
from urlparse import urljoin


class BookProcessor(object):
    def __init__(self, url, username, password):
        if url:
            self.BASE_URL = url
        self.username = username
        self.password = password

    def search(self, params):
        """Search method returns the results of searching parameters."""

        if not params:
            raise ValueError("search method must take the params!")
        if not isinstance(params, dict):
            raise TypeError("params type --> dict!")

        response = requests.get(urljoin(self.BASE_URL, "search"), params,
                                auth=(self.username, self.password))

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise LookupError("search results cannot be found")
        else:
            return "search response status code:%s" % response.status_code

    def availability(self, code):
        """Availability method gets the product code
        that came from search method results and checks it's availability
        status"""

        if not code:
            raise ValueError("availability method must take a product code!")
        if not isinstance(code, (str, unicode)):
            raise TypeError("product code type --> str!")

        response = requests.get(urljoin(self.BASE_URL, "availability/") + code,
                                auth=(self.username, self.password))

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise LookupError("availability results cannot be found")
        else:
            return "availability response status code:%s" \
                   % response.status_code

    def provision(self, code):
        """Provision method gets the product code and makes post for the
        request """

        if not code:
            raise ValueError("provision method must take a product code!")
        if not isinstance(code, (str, unicode)):
            raise TypeError("product code type --> str!")

        response = requests.post(urljoin(self.BASE_URL, "provision/") + code,
                                 auth=(self.username, self.password))

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise LookupError("provision results cannot be found")
        else:
            return "provision response status code:%s" % response.status_code

    def book(self, code, post_data):
        """Book method takes 2 parameters.
        The code parameter is provision code and the post_data is a dictionary
        which have the info about name,pax etc."""

        if not code:
            raise ValueError("book method must take a provision code!")
        if not post_data:
            ValueError("post_data information is required")
        if not isinstance(code, (str, unicode)):
            raise TypeError("provision code type --> str!")
        if not isinstance(post_data, dict):
            raise TypeError("post_data type --> dict!")

        response = requests.post(urljoin(self.BASE_URL, "book/") + code,
                                 post_data,
                                 auth=(self.username, self.password))

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise LookupError("book results cannot be found")
        else:
            return "book response status code:%s" % response.status_code

    def bookings(self, code=""):
        """Bookings method returns the books which is succeeded"""

        if not isinstance(code, (str, unicode)):
            raise TypeError("book code type --> str!")

        response = requests.get(urljoin(self.BASE_URL, "bookings/") + code,
                                auth=(self.username, self.password))

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise LookupError("booking results cannot be found")
        else:
            return "bookings response status code:%s" % response.status_code

    def cancel(self, code):
        """Cancel method takes a parameter which is book code and make
        cancellation for this book. """

        if not code:
            raise StandardError("cancel method must take the book code")
        if not isinstance(code, (str, unicode)):
            raise TypeError("book code type --> str!")

        response = requests.post(urljoin(self.BASE_URL, "cancel/") + code,
                                 auth=(self.username, self.password))

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise LookupError("cancel results cannot be found")
        else:
            return "cancel response status code:%s" % response.status_code




