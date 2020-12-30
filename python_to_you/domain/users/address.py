from python_to_you.extensions.marshmallow import ma
from flask_marshmallow.fields import fields
from python_to_you.models import Address, address
from marshmallow.exceptions import ValidationError
from python_to_you.domain.core.error import Error


class Address():
    def __init__(self):
        self.address = Address


    def get(self, id):
        return self.address.query.filter_by(id=id).first()
        

    def create(self, country, zip_code, state, city, neighborhood, number):
        try:
            AddressSchema().load(country, zip_code, state, city, neighborhood, number)
            addres = self.address(
                country,
                zip_code,
                state,
                city,
                neighborhood,
                number            
            )
            self.address.session.add(address)
            self.address.session.commit()
        except ValidationError as error:
            Error(error.normalized_messages(), 400)


    def update(self, id, country, zip_code, state, city, neighborhood, number):
        try:
            AddressSchema().load(country, zip_code, state, city, neighborhood, number)
            addres = self.address.query.filter_by(id=id).first()
            address.country = country 
            address.zip_code = zip_code
            address.state = state
            address.city = city
            address.neighborhood = neighborhood
            address.number = number
            address.session.commit()
        except ValidationError as error:
            Error(error.normalized_messages(), 400)   


class AddressSchema(ma.Schema):
    country = fields.Str(required=True, 
        error_messages={"message": "country field is required"})
    zip_code = fields.Str(required=True, 
        error_messages={"message": "zip_code field is required"})
    state = fields.Str(required=True, 
        error_messages={"message": "state field is required"})
    city = fields.Str(required=True, 
        error_messages={"message": "city field is required"})
    neighborhood = fields.Str(required=True, 
        error_messages={"message": "neighborhood field is required"})
    number = fields.Str(required=True, 
        error_messages={"message": "number field is required"})
    
    class Meta:
        fields = (
            "country",
            "zip_code",
            "state",
            "city",
            "neighborhood",
            "number"
        )