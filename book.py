import requests


class BookProcessor(object):
    def __init__(self, username, password, params):
        main_url = 'http://localhost:8000/api/v2'
        self.username = username
        self.password = password
        self.search_url = main_url + '/search'
        self.availability_url = main_url + '/availability'
        self.provision_url = main_url + '/provision'
        self.book_url = main_url + '/book'
        self.cancel_url = main_url + '/cancel'
        self.booking_url = main_url + '/bookings'
        self.join_url = '/?'
        self.params = params

    def search(self):
        """Search method returns the results of searching parameters."""
        for item in self.params:
            self.join_url += (item + "=" + self.params[item] + "&")
        complete_url = '{}{}'.format(self.search_url, self.join_url)
        r = requests.get(complete_url, auth=(self.username, self.password))
        if r.status_code == 200:
            return r.json()
        else:
            print "search:", r.status_code


    def availability(self, code):
        """Availability method gets the product code
        that came from search method results and checks it's availability status"""
        r = requests.get(self.availability_url + "/" + code, auth=(self.username, self.password))
        if r.status_code == 200:
            return r.json()
        else:
            print "availability:", r.status_code

    def provision(self, code):
        """Provision method gets the product code and makes post for the request """
        r = requests.post(self.provision_url + "/" + code, auth=(self.username, self.password))
        if r.status_code == 200:
            return r.json()
        else:
            print "provision:", r.status_code

    def book(self, code, post_data):
        """Book method takes 2 parameters.
        The code parameter is provision code and the post_data is a dictionary which have the info about name,pax etc."""
        if not code or not post_data:
            StandardError("provision code and postdata information\
                                             is required!")
        if not isinstance(post_data, dict):
            raise StandardError("postdata must be a dictionary!")

        r = requests.post(self.book_url + "/" + code, post_data, auth=(self.username, self.password))

        if r.status_code == 200:
            return r.json()
        else:
            print "book:", r.status_code


    def bookings(self, code=""):
        """Bookings method returns the books which is succeeded"""
        r = requests.get(self.booking_url + "/" + code, auth=(self.username, self.password))
        if r.status_code == 200:
            print r.json()
        else:
            r.status_code

    def cancel(self, code):
        """Cancel method takes a parameter which is book code and make cancellation for this book. """
        r = requests.post(self.cancel_url + "/" + code, auth=(self.username, self.password))
        print "cancel:", r.status_code