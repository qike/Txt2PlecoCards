#!/usr/bin/python
# -*- coding: utf-8 -*-

# This tool takes a file of plain chinese characters and creates an XML
# file following PLECO (https://www.pleco.com/) schema.
# The generated xml file can then be imported into PLECO as flashcards.
#
# Usage: ===>
#  Txt2PlecoCards.py  input_text_file  category  output_PLECO_xml_file
#
# To use the tool, make sure a template.xml file with the following
# content exists in the same folder as this python file.
#
# <?xml version="1.0" encoding="UTF-8"?>
# <plecoflash formatversion="2" creator="Qi Ke" generator="Pleco 2.0 Flashcard Exporter" platform="Android" created="1456630081">
# 	<cards>
# 		<card language="chinese">
# 			<entry>
# 				<headword charset="sc">八</headword>
# 			</entry>
# 			<catassign category="Grade K"/>
# 		</card>
# 	</cards>
# </plecoflash>

import codecs
import copy
import os
import sys
import time
import xml.etree.ElementTree as ET

def clonecard(card, text, category):
  newcard = copy.deepcopy(card)
  word = newcard.find('./entry/headword')
  word.text = text 
  cat = newcard.find('./catassign')
  cat.set('category', category)
  return newcard

def txt2pleco(txtfile, category, outfile):
  tree = ET.parse(os.path.dirname(os.path.abspath(__file__)) + '/template.xml')
  root = tree.getroot()
  ts = str(int(time.time()))
  root.set("created", ts)
  cards = root.find('./cards')
  card = cards.find('./card')

  f = codecs.open(txtfile, 'r', 'utf-8')
  data = f.read()
  f.close()

  for c in data:
    if c.isspace() == False:
      newcard = clonecard(card, c, category)
      cards.append(newcard)

  cards.remove(card)
  #ET.dump(root)
  tree.write(outfile, 'utf-8')

def printusage():
  print 
  print 'Usage: ===>\n  ' + \
    os.path.basename(__file__) + \
    '  input_text_file  ' + \
    'category  ' + \
    'output_PLECO_xml_file'
  print 

# Gather our code in a main() function
def main():
  if len(sys.argv) < 4:
    printusage()
    sys.exit(1)

  # input file name
  infile = sys.argv[1]
  # category name
  cat = sys.argv[2]
  # output file name
  outfile = sys.argv[3]

  txt2pleco(infile, cat, outfile)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
  main()


