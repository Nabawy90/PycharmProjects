from behave import given
from behave import when
from behave import then

@given("I go to Expedia website")
def go_to_expedia_website(context):
    pass

@when("{adult_count} adult wants to fly on {date} from {origin} to {dest}")
def submit_flight_data(context, adult_count, date, origin, dest):
    one = 1
    assert one == 2
    pass

@then("I shall see an error telling me that origin and destination are the same")
def validate_error_message(context):
    pass