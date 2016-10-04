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

        if not params or not isinstance(params, dict):
            raise StandardError("params information is required and must "
                                "dictionary")
        response = requests.get(urljoin(self.BASE_URL, "search"), params,
                                auth=(self.username, self.password))
        if response.status_code == 200:
            return response.json()
        else:
            return "search response status code:%s" % response.status_code

    def availability(self, code):
        """Availability method gets the product code
        that came from search method results and checks it's availability
        status"""

        if not code or not isinstance(code, str):
            raise StandardError("availability method must take a product "
                                "code(str)")

        response = requests.get(urljoin(self.BASE_URL, "availability/") + code,
                                auth=(self.username, self.password))
        if response.status_code == 200:
            return response.json()
        else:
            return "availability response status code:%s" \
                   % response.status_code

    def provision(self, code):
        """Provision method gets the product code and makes post for the
        request """

        if not code:
            raise StandardError("provision method must take a product code")

        response = requests.post(urljoin(self.BASE_URL, "provision/") + code,
                                 auth=(self.username, self.password))
        if response.status_code == 200:
            return response.json()
        else:
            return "provision response status code:%s" % response.status_code

    def book(self, code, post_data):
        """Book method takes 2 parameters.
        The code parameter is provision code and the post_data is a dictionary
        which have the info about name,pax etc."""

        if not isinstance(code, str):
            raise StandardError("provision code must be string")

        if not post_data:
            StandardError("post_data information "
                          "is required")
        if not isinstance(post_data, dict):
            raise StandardError("post_data must be dictionary!")

        response = requests.post(urljoin(self.BASE_URL, "book/") + code,
                                 post_data,
                                 auth=(self.username, self.password))
        if response.status_code == 200:
            return response.json()
        else:
            return "book response status code:%s" % response.status_code

    def bookings(self, code=""):
        """Bookings method returns the books which is succeeded"""

        response = requests.get(urljoin(self.BASE_URL, "bookings/") + code,
                                auth=(self.username, self.password))
        if response.status_code == 200:
            return response.json()
        else:
            return "bookings response status code:%s" % response.status_code

    def cancel(self, code):
        """Cancel method takes a parameter which is book code and make
        cancellation for this book. """

        if not code:
            raise StandardError("cancel method must take the book code")

        response = requests.post(urljoin(self.BASE_URL, "cancel/") + code,
                                 auth=(self.username, self.password))
        if response.status_code == 200:
            return response.json()
        else:
            "cancel response status code:%s" % response.status_code




