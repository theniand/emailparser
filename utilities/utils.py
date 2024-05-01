import pandas as pd

class Utils():
    def __init__(self):
        pass

def getDataFromDatabase():
    dataSource = 'data/metalinfo.csv'
    # df = pd.read_csv(dataSource) can't get panda to ingest quite right
    #can use panda here to clean & filter large datasets
    #can also use astra to store the data
    df = "id,product_name,cost_per_ton,production_time_in_days,,,,,1,stainless steel,40,8,,,,,2,nickel,20,6,,,,,3,iron,30,5,,,,,4,aluminum,10,4,,,,,5,zinc,7,3,,,,,6,scrap,5,2,,,,,7,misc,3,1,,,,,"
    return df

def getContent():
    jsonObject = 'Store a structured JSON object like this:{"NameFirst": "","NameLast": "","Email": "","PhoneNumber": "","Company": "","Order":"","Quantity":""} called jsondata'
    database = "csv:" + getDataFromDatabase()
    solveAndCreateEmail = "from the csv, match the order to the product_name in the table. If you cannot find a good enough match for proudct_name use the product_name of misc. then multiply the quantity to the cost_per_ton in the table and save that value as totalcost. Match the order to the product_name in the table, then multiply the quantity to the production_time_in_days in the table and save that value as productiondays. Write and compose an email given all the information in the json and tell the user the lead time of productiondays and a cost of totalcost with my name as Chris Holt"
    fineTuiningContent = "Given an email, parse the contact details from the lead." + jsonObject + database + solveAndCreateEmail
    return fineTuiningContent

def getSampleEmail():
    email = "\n\nDear Cloudforge,\n\nI hope this email finds you well. We are in need of a bulk order of stainless steel for our manufacturing process. I am looking to buy 4 tons of stainless steel. Could you please provide us with the cost and the lead time for an order? \nPlease let us know if you have any further questions or if you require additional information.\n\nThank you and best regards,\n\nJoan Smithe,\n\nPanlite Company\n\nPhone: 919-555-1234"
    return email