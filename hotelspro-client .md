hotelspro-client
==================

A python client library for <a href="https://api.hotelspro.com">HotelsPro</a>

### Installation
===================

```bash
$ python setup.py install
```

### Usage
```python
from hotelspro_client.book import BookProcessor

if __name__ == '__main__':
    params = {'checkin': '2016-09-30', 'checkout': '2016-10-03', 'pax': '1', 'destination_code': '11260',
              'client_nationality': 'tr', 'currency': 'USD'}


    book_processor = BookProcessor(username, password, params=params)
    print book_processor.search()
```

**response**
```javascript
{
    "count": 13, 
    "code": "5ddc9ca0a9744a78a3dfce3a88aedd83", 
    "next_page_code": null, 
    "results": [
        {
            "hotel_code": "10370d", 
            "checkout": "2016-10-03", 
            "checkin": "2016-09-30", 
            "destination_code": "11260", 
            "products": [
                {
                    "code": "EDcNIT4ZIAAAAAAAAAAAAAAAAAAAAAAAAAHAXdycoKl0Snij3846iK7dgwABAAAAAAAAAAAAAAZfQAAAAAcIAeBOgC6nrwOkJBsJAAIAAAAAAAAAAAAABA", 
                    "list_price": "72.00", 
                    "offer": true, 
                    "pay_at_hotel": false, 
                    "price": "72.00", 
                    "currency": "USD", 
                    "cost": "72.00", 
                    "rooms": [
                        {
                            "pax": {
                                "adult_quantity": 1, 
                                "children_ages": []
                            }, 
                            "room_category": "Standard", 
                            "room_description": "Standard Room", 
                            "room_type": "SB"
                        }
                    ], 
                    "nonrefundable": null, 
                    "providers": [
                        "gta"
                    ], 
                    "supports_cancellation": true, 
                    "hotel_currency": null, 
                    "hotel_price": null, 
                    "meal_type": "RO", 
                    "minimum_selling_price": null, 
                    "view": false
                }, 
                {
                    "code": "EDcNIT4ZIAAAAAAAAAAAAAAAAAAAAAAAAAHAXdycoKl0Snij3846iK7dgwABAAAAAAAAAAAAAAZfQAAAAAcIAeBOgLvShg_ykoY5ABIAAAAAAAAAAAAABA", 
                    "list_price": "72.00", 
                    "offer": true, 
                    "pay_at_hotel": false, 
                    "price": "72.00", 
                    "currency": "USD", 
                    "cost": "72.00", 
                    "rooms": [
                        {
                            "pax": {
                                "adult_quantity": 1, 
                                "children_ages": []
                            }, 
                            "room_category": "Standard", 
                            "room_description": "Club Cottage", 
                            "room_type": "SB"
                        }
                    ], 
                    "nonrefundable": null, 
                    "providers": [
                        "gta"
                    ], 
                    "supports_cancellation": true, 
                    "hotel_currency": null, 
                    "hotel_price": null, 
                    "meal_type": "RO", 
                    "minimum_selling_price": null, 
                    "view": false
                }, 
                {
                    "code": "EDcNIT4ZIAAAAAAAAAAAAAAAAAAAAAAAAAHAXdycoKl0Snij3846iK7dgwABAAAAAAAAAAAABTBnwAAABbm5AeFOgDZubniWANS6ACIBgAAAAAAAAAAABA", 
                    "list_price": "15009.00", 
                    "offer": true, 
                    "pay_at_hotel": false, 
                    "price": "15009.00", 
                    "currency": "USD", 
                    "cost": "15009.00", 
                    "rooms": [
                        {
                            "pax": {
                                "adult_quantity": 1, 
                                "children_ages": []
                            }, 
                            "room_category": "Deluxe", 
                            "room_description": "Executive Room", 
                            "room_type": "SB"
                        }
                    ], 
                    "nonrefundable": null, 
                    "providers": [
                        "gta"
                    ], 
                    "supports_cancellation": true, 
                    "hotel_currency": null, 
                    "hotel_price": null, 
                    "meal_type": "BE", 
                    "minimum_selling_price": null, 
                    "view": false
                }, 
                {
                    "code": "EDcNIT4ZIAAAAAAAAAAAAAAAAAAAAAAAAAHAXdycoKl0Snij3846iK7dgwABAAAAAAAAAAAAAAZfQAAAAAcIAeBOgDZubniWANS6ADIBgAAAAAAAAAAABA", 
                    "list_price": "72.00", 
                    "offer": true, 
                    "pay_at_hotel": false, 
                    "price": "72.00", 
                    "currency": "USD", 
                    "cost": "72.00", 
                    "rooms": [
                        {
                            "pax": {
                                "adult_quantity": 1, 
                                "children_ages": []
                            }, 
                            "room_category": "Deluxe", 
                            "room_description": "Executive Room", 
                            "room_type": "SB"
                        }
                    ], 
                    "nonrefundable": null, 
                    "providers": [
                        "gta"
                    ], 
                    "supports_cancellation": true, 
                    "hotel_currency": null, 
                    "hotel_price": null, 
                    "meal_type": "RO", 
                    "minimum_selling_price": null, 
                    "view": false
                }, 
                {
                    "code": "EDcNIT4ZIAAAAAAAAAAAAAAAAAAAAAAAAAHAXdycoKl0Snij3846iK7dgwABAAAAAAAAAAAABTBnwAAABbm5AeFOgC6nrwOkJBsJAEIAAAAAAAAAAAAABA", 
                    "list_price": "15009.00", 
                    "offer": true, 
                    "pay_at_hotel": false, 
                    "price": "15009.00", 
                    "currency": "USD", 
                    "cost": "15009.00", 
                    "rooms": [
                        {
                            "pax": {
                                "adult_quantity": 1, 
                                "children_ages": []
                            }, 
                            "room_category": "Standard", 
                            "room_description": "Standard Room", 
                            "room_type": "SB"
                        }
                    ], 
                    "nonrefundable": null, 
                    "providers": [
                        "gta"
                    ], 
                    "supports_cancellation": true, 
                    "hotel_currency": null, 
                    "hotel_price": null, 
                    "meal_type": "BE", 
                    "minimum_selling_price": null, 
                    "view": false
                }, 
```

**notes**
- check out examples for other methods.