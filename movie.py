#!/usr/bin/python

import xml.sax

class MovieHandler( xml.sax.ContentHandler ):
   def __init__(self):
      self.CurrentData = ""
      self.sku = ""
      self.instock = ""
      self.region = ""
      self.rating = ""
      self.stars = ""
      self.description = ""

   # Call when an element starts
   def startElement(self, tag, attributes):
      self.CurrentData = tag
      if tag == "ns1:products":
         print ("*****product*****")
      if tag == "ns1:stock":
         print ("*****stock*****")
       #  title = attributes["title"]
       #  print ("Title:", title)

   # Call when an elements ends
   def endElement(self, tag):
      if self.CurrentData == "ns1:sku":
         print ("sku:", self.sku)
      elif self.CurrentData == "ns1:inv":
         print ("Qty in stock:", self.instock)
      elif self.CurrentData == "ns1:region":
         print ("Region:", self.region)
      elif self.CurrentData == "rating":
         print ("Rating:", self.rating)
      elif self.CurrentData == "stars":
         print ("Stars:", self.stars)
      elif self.CurrentData == "description":
         print ("Description:", self.description)
      self.CurrentData = ""

   # Call when a character is read
   def characters(self, content):
      if self.CurrentData == "ns1:sku":
         self.sku = content
      elif self.CurrentData == "ns1:inv":
         self.instock = content
      elif self.CurrentData == "ns1:region":
         self.region = content
      elif self.CurrentData == "rating":
         self.rating = content
      elif self.CurrentData == "stars":
         self.stars = content
      elif self.CurrentData == "description":
         self.description = content
  
if ( __name__ == "__main__"):
   
   # create an XMLReader
   parser = xml.sax.make_parser()
   # turn off namepsaces
   parser.setFeature(xml.sax.handler.feature_namespaces, 0)

   # override the default ContextHandler
   Handler = MovieHandler()
   parser.setContentHandler( Handler )
   
   parser.parse(r'C:\Users\Chase\Desktop\Python Farnell Stock Check\farnell.xml')