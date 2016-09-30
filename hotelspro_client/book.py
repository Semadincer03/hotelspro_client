import requests


class BookProcessor(object):
    def __init__(self, username, password):
        MAIN_URL = 'http://localhost:8000/api/v2'
        self.username = username
        self.password = password
        self.SEARCH_URL = MAIN_URL + '/search/'
        self.AVAILABILITY_URL = MAIN_URL + '/availability/'
        self.PROVISION_URL = MAIN_URL + '/provision/'
        self.BOOK_URL = MAIN_URL + '/book/'
        self.CANCEL_URL = MAIN_URL + '/cancel/'
        self.BOOKING_URL = MAIN_URL + '/bookings/'
        self.join_url = '?'

    def search(self, params):
        """Search method returns the results of searching parameters."""

        if not params or not isinstance(params, dict):
            raise StandardError("params information is required and must be a dictionary")
        else:
            for item in params:
                self.join_url += (item + "=" + params[item] + "&")
            complete_url = '{}{}'.format(self.SEARCH_URL, self.join_url)

            r = requests.get(complete_url, auth=(self.username, self.password))
            if r.status_code == 200:
                return r.json()

    def availability(self, code):
        """Availability method gets the product code
        that came from search method results and checks it's availability status"""

        if not code or not isinstance(code, str):
            raise StandardError("availability method must take a product code(str)")
        else:
            r = requests.get(self.AVAILABILITY_URL + code, auth=(self.username, self.password))
            if r.status_code == 200:
                return r.json()

    def provision(self, code):
        """Provision method gets the product code and makes post for the request """

        if not code:
            raise StandardError("provision method must take a product code")
        else:
            r = requests.post(self.PROVISION_URL + code, auth=(self.username, self.password))
            if r.status_code == 200:
                return r.json()

    def book(self, code, post_data):
        """Book method takes 2 parameters.
        The code parameter is provision code and the post_data is a dictionary which have the info about name,pax etc."""

        if not code or not post_data:
            StandardError("provision code and post_data information is required!")
        if not isinstance(post_data, dict):
            raise StandardError("post_data must be a dictionary!")

        r = requests.post(self.BOOK_URL + code, post_data, auth=(self.username, self.password))
        if r.status_code == 200:
            return r.json()

    def bookings(self, code=""):
        """Bookings method returns the books which is succeeded"""

        r = requests.get(self.BOOKING_URL + code, auth=(self.username, self.password))
        if r.status_code == 200:
            return r.json()

    def cancel(self, code):
        """Cancel method takes a parameter which is book code and make cancellation for this book. """

        if not code:
            raise StandardError("cancel method must take the book code")
        else:
            r = requests.post(self.CANCEL_URL + code, auth=(self.username, self.password))
            return r.json()


