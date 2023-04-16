import argparse
import sys
import random
from datetime import date, datetime, timedelta


from faker import Faker
# from random_word import RandomWords
# import names # the '.get_name...()' functions have an optional parameter of 'gender' which either takes  'male' or 'female'


def createSql(schema, tableName, total, uniquePairs=[]):
    fake = Faker("en_GB")

    sql = "INSERT INTO " + tableName + " ("

    for i in range(len(schema)):
        sql += schema[i]['name']
        sql += ", " if len(schema)-1 != i else ")\n\tVALUES\n\t\t"

    for i in range(total):
        singleVal = "("
        for j in range(len(schema)):
            insertVal =  genVal(schema[j], fake=fake) if "forceVal" not in schema[j] else schema[j]["forceVal"]
        
            insertVal = insertVal.replace("'", "//'") if type(insertVal) == str else insertVal
            
            singleVal += "'" + insertVal + "'" if type(insertVal) == str else str(insertVal)
            singleVal += "," if len(schema)-1 != j else ")"
        sql += singleVal 
        sql += ",\n\t\t" if total-1 != i else ""

    return sql + ";"

def genVal(row, fake=Faker("en_GB")):
    if "unique" in row:
        if row['unique']:
            if row["name"] == "forename":
                return fake.unique.first_name()
            elif row["name"] == "surname":
                return fake.unique.first_name()
            elif row["name"] == "email":
                return fake.unique.email()
            elif row["dataType"] == "string":
                return fake.unique.word()
    
    if row["name"] == "forename":
        return fake.first_name()
    elif row["name"] == "surname":
        return fake.last_name()
    elif row["name"] == "profession":
        return fake.job()
    elif row["name"] == "email":
        return fake.email()
    elif row["name"] == "country":
        return fake.country()

    
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
        return fake.word()
    
    if "valRange" in row:
        if row["dataType"] == "datetime":
            return str(fake.date_this_century())
        elif row["dataType"] == "integer":
            return random.randrange(row["valRange"][0], row["valRange"][1])
        elif "decimalPlace" in row:
            return round(random.uniform(row["valRange"][0], row["valRange"][1]), row["decimalPlace"])
        else: 
            return random.uniform(row["valRange"][0], row["valRange"][1])



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
        "unique": True # only applies to strings
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

    users = [
        {
            "name": "email",
            "dataType": "string",
            "unique": True
        },
        {
            "name": "password",
            "dataType": "string",
            "forceVal": "$2a$10$QKROIDI35N4hIOQ1qwVwU.25ciIBjum/8mgQNEfzK.fMbMgJhUUUi"
        },
        {
            "name": "forename",
            "dataType": "string"
        },
        {
            "name": "surname",
            "dataType": "string"
        },
        {
            "name": "profession",
            "dataType": "string"
        },
        {
            "name": "country",
            "dataType": "string"
        },
        {
            "name": "user_role",
            "dataType": "string",
            "possibleVals": ["learner", "admin", "field_engineer"]
        }
    ]

    courses = [{
        "name": "course_name",
        "dataType" : "string",
        "unique": True
    }]

    chapters = [
        {
            "name": "chapter_name",
            "dataType" : "string"
        },
        {
            "name":"pass_score",
            "dataType" : "decimal",
            "decimalPlace": 2
        },
        {
            "name":"num_pages",
            "dataType" : "integer"
        },
        {
            "name":"course_id",
            "dataType" : "integer",
            "forceVal": 1
        }
    ]
    
    testStr = [{
            "name" : "testStr",
            "dataType": "string",
            "unique":True                
    }]
    
    # print(createSql(testStr, "compliance_data", 10))

    # print(genVal(testStr))

    print(createSql(users, "users", 20) + "\n")
    print(createSql(courses, "courses", 1) + "\n")
    print(createSql(chapters, "chapters", 6) + "\n")

    # print(readWordlist("wordlist"))

    # date_time_str = '2018-09-19'

    # print(getRandDate("2020-12-23", "2022-04-12"))

    # fake= Faker("en_GB")

    # print(fake.words(nb=10, unique=True))