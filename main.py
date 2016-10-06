from hotelspro_client.book import BookProcessor

if __name__ == '__main__':

    book_processor = BookProcessor("http://localhost:8000/api/v2/",
                                   "username", "password")

    print book_processor.search({'checkin': '2016-10-20', 'checkout':
     '2016-10-24', 'pax': '1', 'hotel_code': '11b0dd',
                              'client_nationality': 'tr', 'currency':
                                 'USD'})



