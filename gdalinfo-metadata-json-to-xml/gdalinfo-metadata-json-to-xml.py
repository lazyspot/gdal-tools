'''
Reads data from json file and converts to xml file
json file is created by command: gdalinfo -json 'picture.tif' > picture_info.json
where picture.tif - path to tif picture, picture_info.json - name/path of the file where tif info will be saved

'''


#### FUNCTIONS ######

def print_xml(xml):
    '''prints nice formated xml, copy from https://pypi.org/project/dicttoxml/ ---> Pretty-Printing'''
    from xml.dom.minidom import parseString
    dom = parseString(xml)
    print(dom.toprettyxml())
    return

def save_xml(my_file, xml):
    '''taking xml object (xml) saves in file with name given as (my_file)'''
    my_file=open(my_file,"wb")
    my_file.write(xml)
    my_file.close()
    return




######      MAIN        ###########

import dicttoxml

#    parameters  #

picture_info_json = r'/media/sf_windows/25TFE_info.json'
picture_info_xml = '/media/sf_windows/25TFE_info.xml'

#    parameters end #

    # read json file
with open(picture_info_json, "r") as tekst:
    input_csv = tekst.readlines()
    # create xml object
xml = dicttoxml.dicttoxml(input_csv)

    # save xml file
save_xml(picture_info_xml, xml)

print('File xml saved as:', picture_info_xml)





