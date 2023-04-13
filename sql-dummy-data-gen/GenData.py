import argparse
import sys
import random
from datetime import date, datetime, timedelta

from random_word import RandomWords
import names


def createSql(schema, tableName, total):
    sql = "INSERT INTO " + tableName + " ("

    for i in range(len(schema)):
        sql += schema[i]['name']
        sql += ", " if len(schema)-1 != i else ")\n\tVALUES\n\t\t"

    for i in range(total):
        singleVal = "("
        for j in range(len(schema)):
            insertVal = genVal(schema[j])
            singleVal += "'" + insertVal + "'" if type(insertVal) == str else str(insertVal)
            singleVal += "," if len(schema)-1 != j else ")"
        sql += singleVal 
        sql += ",\n\t\t" if total-1 != i else ""

    return sql + ";"

def genVal(row):
    if ("valRange" not in row) and (row["dataType"] == "integer" or row["dataType"] == "decimal"):
        min = random.randrange(1,10)
        row["valRange"] = [min, random.randrange(min,min*100)]

    if ("valRange" not in row) and (row["dataType"] == "datetime"):
        row["valRange"] = [getRandDate("2000-12-23", "2008-04-12"),getRandDate("2008-04-14", "2022-04-12")]

    if "possibleVals" in row:
        return random.choice(row["possibleVals"])
    elif row["dataType"] == "boolean":
        return random.choice([True, False])
    elif row["dataType"] == "string":
        return RandomWords().get_random_word()
    
    if "valRange" in row:
        if row["dataType"] == "datetime":
            return getRandDate(row["valRange"][0], row["valRange"][1])
        elif row["dataType"] == "integer":
            return random.randrange(row["valRange"][0], row["valRange"][1])
        elif "decimalPlace" in row:
            return round(random.uniform(row["valRange"][0], row["valRange"][1]), row["decimalPlace"])
        else: 
            return random.uniform(row["valRange"][0], row["valRange"][1])
    
    ## generate random names using the following

    # names.get_full_name() # 'Patricia Halford'
    # names.get_full_name(gender='male') # 'Patrick Keating'
    # names.get_first_name() # 'Bernard'
    # names.get_first_name(gender='female') # 'Christina'
    # names.get_last_name() # 'Szczepanek'



def getRandDate(startDate, endDate):
    # initializing dates ranges
    # startDate, test_date2 = date(2015, 6, 3), date(2022, 7, 1)

    #  datetime.fromisoformat supports YYYY-MM-DDTHH:MM:SS but anything after T can be removed

    startObj = datetime.fromisoformat(startDate)
    endObj = datetime.fromisoformat(endDate)
    
    # getting days between dates
    datesBet = endObj - startObj
    totalDays = datesBet.days
    
    # getting random days
    randay = random.randrange(totalDays)

    # ranSec = random.randrange(totalSecs)

    # ranHrs = random.randrange(totalHrs)

    # ranMins = random.randrange(totalMins)
    
    return str(startObj + timedelta(days=randay))
    

if __name__ == '__main__':
    row = {
        "name": "prime",
        "dataType": ["integer", "decimal", "datetime", "boolean", "string"],
        "possibleVals": [],
        "valRange": ["min", "max"],
        "decimalPlace": 3,
        "isPk": True,
        "unique": True
    }

    possibleData = [
        {
            "name": "entry_date",
            "dataType": "datetime"
        },
        {
            "name": "method",
            "dataType": "string",
            "possibleVals": ["SOSPD", "CAPD"]
        },
        {
            "name": "bed_number",
            "dataType": "integer"
        }, 
        {
            "name": "picu_id",
            "dataType": "integer",
            "valRange": [1,23]
        },
        {
            "name": "correct_details",
            "dataType": "boolean"
        },
        {
            "name": "comfort_recorded",
            "dataType": "boolean"
        },
        {
            "name": "comfort_above",
            "dataType": "boolean"
        },
        {
            "name": "all_params_scored",
            "dataType": "boolean"
        },
        {
            "name": "totalled_correctly",
            "dataType": "boolean"
        },
        {
            "name": "in_score_range",
            "dataType": "boolean"
        },
        {
            "name": "observer_name",
            "dataType": "boolean"
        }
    ]

    possibleData2 = [
        {
            "name" : "testStr",
            "dataType": "string"
        },
        {
            "name": "entry_date",
            "dataType": "datetime"
        },
        {
            "name": "method",
            "dataType": "string",
            "possibleVals": ["SOSPD", "CAPD"]
        },
        {
            "name": "bed_number",
            "dataType": "integer"
        }, 
        {
            "name": "picu_id",
            "dataType": "integer",
            "valRange": [1,23]
        },
        {
            "name": "correct_details",
            "dataType": "boolean"
        },
        {
            "name": "comfort_recorded",
            "dataType": "boolean"
        },
        {
            "name": "comfort_above",
            "dataType": "boolean"
        },
        {
            "name": "all_params_scored",
            "dataType": "boolean"
        },
        {
            "name": "totalled_correctly",
            "dataType": "boolean"
        },
        {
            "name": "in_score_range",
            "dataType": "boolean"
        },
        {
            "name": "observer_name",
            "dataType": "boolean"
        }
    ]

    testStr = {
            "name" : "testStr",
            "dataType": "string"
        }
    # print(genVal(testStr))

    print(createSql(possibleData2, "compliance_data", 10))

    # print(readWordlist("wordlist"))

    # date_time_str = '2018-09-19'

    # print(getRandDate("2020-12-23", "2022-04-12"))