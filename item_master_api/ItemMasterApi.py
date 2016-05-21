import pandas
import os
import subprocess


class ItemMasterApi:

    def __init__(self,username, password):
        self.user=username
        self.passw=password
        self.xml_file_name=None

    # It fetch items from idx to limit and save it on a a xml file
    def get_items(self, idx=None, limit=None, xml_file_name=None):
        if (xml_file_name!=None):
            self.xml_file_name = xml_file_name
        else:
            self.xml_file_name='output.xml'


        os.system("curl --header username:"+self.user+" --header password:" + self.passw + " 'https://api.itemmaster.com/v2/item?idx=0&limit=50' > " + self.xml_file_name)




    def xml2json(self, output_file=None):

        if (output_file==None):
            output_file='output.json'

        args = "xml2json --input " + self.xml_file_name +" --output " + output_file

        process = subprocess.Popen(args.split(), stdout=subprocess.PIPE)
        output =  process.communicate()[0]


        '''
        if json_file==None and excel_file==None:
            pandas.read_json("input.json").to_excel("output.xlsx")
        else:
            try:
                pandas.read_json(json_file,excel_file)
            except:
                print "Need the name of input json and output xlsx "
                return
        '''

        return output_file

    def json2excel(self, input_file,output_file=None):

        if excel_file==None:
            pandas.read_json(input_file).to_excel("output.xlsx")
        else:
            try:
                pandas.read_json(input_file,output_file)
            except:
                print "Need the name of input json and output xlsx "
                return
        return

    def xml2excel(self, output_file=None):
        json_file = self.xml2json(output_file)

        if output_file==None:
            pandas.read_json(json_file).to_excel("output.xlsx")
        else:
            try:
                pandas.read_json(json_file,output_file)
            except:
                print "Need the name of input json and output xlsx "
                return
        return

