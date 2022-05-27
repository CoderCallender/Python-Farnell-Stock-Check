#!/usr/bin/python

import xml.sax
import requests
import xml.etree.ElementTree

sku = ""

class FarnellHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.sku = ""
      self.instock = []
      self.region = []
      self.MPN = []
 

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
   #   if tag == "ns1:products":
   #      print ("*****product*****")
   #   if tag == "ns1:stock":
   #      print ("*****stock*****")
   #   if tag == "ns1:translatedManufacturerPartNumber":
   #      print ("*****MPN*****")
   

   # Call when an elements ends
#    def endElement(self, tag):
#       if self.CurrentData == "ns1:sku":
#          print ("sku:", self.sku)
#       #   sku = self.sku
#       elif self.CurrentData == "ns1:inv":
#          print ("Qty in stock:", self.instock)
#       elif self.CurrentData == "ns1:region":
#          print ("Region:", self.region)
#       elif self.CurrentData == "ns1:translatedManufacturerPartNumber":
#          print ("MPN:", self.MPN)
 

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "ns1:sku":
         self.sku = content
      elif self.CurrentData == "ns1:inv":
         self.instock.append(content)
      elif self.CurrentData == "ns1:region":
         self.region.append(content)
      elif self.CurrentData == "ns1:translatedManufacturerPartNumber":
         self.MPN.append(content)

  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = FarnellHandler()
   parser.setContentHandler( Handler )
   
   
   #response = requests.get('https://api.element14.com/catalog/products?versionNumber=1.2&term=id%3A1652963&storeInfo.id=uk.farnell.com&resultsSettings.offset=0&resultsSettings.numberOfResults=1&resultsSettings.refinements.filters=rohsCompliant%2CinStock&resultsSettings.responseGroup=large&callInfo.omitXmlSchema=false&callInfo.responseDataFormat=xml&callinfo.apiKey=rhcf7dupd8arzxtvqubksbbw')

  


   
   #with open(r"C:\Users\callende\Desktop\Python stock check\Python-Farnell-Stock-Check\response.xml", "w") as f:
   # f.write(response.text)
   # f.close
   parser.parse(r'C:\Users\callende\Desktop\Python stock check\Python-Farnell-Stock-Check\farnell.xml')
 #  parser.parse(r'C:\Users\callende\Desktop\Python stock check\Python-Farnell-Stock-Check\response.xml')
 #  parser.parse(xml.etree.ElementTree.dump(tree))
 
   print("MPN",Handler.sku)
   print("stock",Handler.instock[0])
   print("location",Handler.region[0])