from hotelspro_client.book import BookProcessor

if __name__ == '__main__':
    params = {'checkin': '2016-10-03', 'checkout': '2016-10-05', 'pax': '1',
              'destination_code': '11260',
              'client_nationality': 'tr', 'currency': 'USD'}

    book_processor = BookProcessor("http://localhost:8000/api/v2/",
                                   "username", "password")

    print book_processor.search({'checkin': '2016-10-10', 'checkout':
     '2016-10-11', 'pax': '1', 'hotel_code': '10370d',
                              'client_nationality': 'tr', 'currency':
                                 'USD'})



