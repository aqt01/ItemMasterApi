# itemMaster-API
API for retrieving data from the API ItemMaster V2
https://api.itemmaster.com/v2/


# Notes
This is not a pythonic way of retrieving and using data from item master API

We fetch from the item master API using curl from a command on the system, and we store the xml and manipulate the data on disk. 




# Install
First, install curl on your OS and then

$ pip install requirements.txt

# Usage

ItemMasterApi(username,password - Store username and password on class object
get_items(idx,limit, xml_file_name=None)) - Retrieve the items from 'idx' to 'limit'. Both are numeric values. if xml_file_name is not defined output.xml is created
xml2excel(output_file=None) - Converts the retrieved xml from the item master api to a excel file. If no name is given, the name will be output.xlsx
xml2json(output_file=None) - Converts the retrieved xml from the item master api to a json file. If no name is given, output.json will be created

# Example
from item_master_api import ItemMasterApi.ItemMasterApi

x = ItemMasterApi('username','password')
x.get_items(0,50) 
x.xml2excel('50-items.xlsx')



