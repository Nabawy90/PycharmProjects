import time
import pandas as pd

'''
Other validations can take place like
    - None of the cells has null values
    - Completely duplicate rows
'''

def validate_airport_str_length(flights_df):
    '''
    Validates the lenght of the airport abbreviations to be exactly 3.
    :param flights_df: flights datafram from csv
    :return: true if all airports are exactly 3 chars

    SELECT * FROM
    FLIGHTS as f
    WHERE LENGTH(f.from) <> 3 OR LENGTH(f.to) <> 3
    '''

    '''

    '''

    len_mask = (flights_df['from'].str.len() != 3) | (flights_df['to'].str.len() != 3)
    airport_len_not_3_df = flights_df[len_mask]

    if len(airport_len_not_3_df) != 0:
        return False
    else:
        return True


def validate_airport_exist(flights_df):
    '''
    This function returns True if the airports in the data frame are existing in real world not fake airports.
    :param flights_df: flights dataframe
    :return: bool

    SELECT airport
    FROM flights
    WHERE airport NOT IN (SELECT airport_abb FROM airports)
    '''
    original_flights_df_len = len(flights_df)
    AP_list = ['HAM', 'LHR', 'CAI', 'LIS', 'OPO', 'AMS']
    existing_mask = (flights_df['from'].isin(AP_list)) & (flights_df['to'].isin(AP_list))
    exisiting_airport_df = flights_df[existing_mask]

    if len(exisiting_airport_df) < original_flights_df_len:
        return False
    else:
        return True


def validate_origin_dst_different(flights_df):
    '''
    Validate that flights are from an origin different than the destination
    :param flights_df:
    :return:

    SELECT *
    FROM flights as f
    WHERE f.origin == f.dest
    '''
    original_flights_df_len = len(flights_df)
    different_mask = (flights_df['from'] != flights_df['to'])
    different_origin_dest_df = flights_df[different_mask]

    if len(different_origin_dest_df) < original_flights_df_len:
        return False
    else:
        return True


def validate_date(flights_df):
    '''
    This function returns True if the date is bigger than yesterday and less than a year from NOW()
    :param flights_df:
    :return:

    SELECT *
    FROM flight as f
    WHERE f.date < CURDATE() OR f.date > CURDATE + 356

    '''
    today = time.strftime("%d/%m/%Y")
    numOfFlights = len(flights_df.index)
    test_status = True

    for i in range(numOfFlights):
        if (time.strptime(str(flights_df.loc[i, 'date']), "%d/%m/%Y") < time.strptime(today, "%d/%m/%Y")) \
                or (time.strptime(str(flights_df.loc[i, 'date']), "%d/%m/%Y")
                        > time.strptime("10/10/2018", "%d/%m/%Y")):
            print(flights_df['date'])
            test_status = False
            break

    return test_status


def validate_number_of_adults(flights_df):
    '''
    This function returns True if the number of adults in a row is bigger than 0 and less than 7
    :param flights_df:
    :return:

    SELECT *
    FROM flights as f
    WHERE f.adults < 0 OR f.adults >7
    '''
    original_flights_df_len = len(flights_df)
    passenger_number_mask = (flights_df['adults'] > 0) & (flights_df['adults'] < 7)
    passeneger_number_df = flights_df[passenger_number_mask]

    print(passeneger_number_df)

    if len(passeneger_number_df) < original_flights_df_len:
        return False
    else:
        return True


def validate_flights_data_test(csv_file):
    '''
    This function will test a combination of invalid flights. an invalid flight takes one or more of the following form:
    - date in the past
    - Origin = Destination
    - Unknown Origin or destination

    The invalid inputs will be stored in a CSV file. The function will try and validate the data in the file
    :return: none
    '''

    # according to IAAT, ariport abbreviation has to be 3 letters
    # will check against a list of predefined airports. [HAM, LHR, CAI, LIS, OPO, AMS]
    test_status = True

    # Read the csv file and put it in a df. Get the original size of the df to compare against conditional selection
    # later
    flightsDataFrame = pd.read_csv(csv_file)

    # Making sure that these columns are of string type.
    flightsDataFrame['from'] = flightsDataFrame['from'].astype('str')
    flightsDataFrame['to'] = flightsDataFrame['to'].astype('str')

    if not validate_airport_str_length(flightsDataFrame):
        print("some records has airport length is not exactly 3")
        test_status = False
    elif not validate_airport_exist(flightsDataFrame):
        print("some records has airports doesn't exist")
        test_status = False
    elif not validate_origin_dst_different(flightsDataFrame):
        print("some records has origin == dest")
        test_status = False
    elif not validate_date(flightsDataFrame):
        print("some records has date is either less than today or bigger than a year from now")
        test_status = False
    elif not validate_number_of_adults(flightsDataFrame):
        print("some records has adults number is less than 1 or bigger than 6")
        test_status = False

    print(test_status)
    return test_status

