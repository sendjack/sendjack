""" Module: user

Store a User from the Sign Up page.

"""
import stripe

import settings

FIRST_NAME = "first-name"
LAST_NAME = "last-name"
EMAIL = "email"
TOKEN = "token"


class User(object):

    """ Store a new user. """


    def __init__(self, parameters):
        """ Construct a User. """
        self.first_name = parameters[FIRST_NAME]
        self.last_name = parameters[LAST_NAME]
        self.email = parameters[EMAIL]
        self.token = parameters[TOKEN]

        # make sure Stripe has an api secret
        stripe.api_key = settings.STRIPE_SECRET_KEY


    def store(self):
        """ Store a User's data. """
        description = "{} {}".format(self.first_name, self.last_name)

        # create a Customer
        customer = stripe.Customer.create(
                card=self.token,
                email=self.email,
                description=description)

        # TODO: actually have a database

        # save the customer ID in your database so you can use it later
        # save_stripe_customer_id(user, customer.id)

        # later
        # customer_id = get_stripe_customer_id(user)

        # stripe.Charge.create(
        #     amount=1500, # $15.00 this time
        #     currency="usd",
        #     customer=customer_id
        # )
