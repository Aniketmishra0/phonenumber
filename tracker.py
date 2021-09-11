import phonenumbers
from pnumber import number

# Geocoder is a build in function from phone number
from phonenumbers import geocoder

c_number = phonenumbers.parse(number, "CH")
print(geocoder.description_for_number(c_number, "en"))

from phonenumbers import carrier
service_provider = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_provider,"en"))

