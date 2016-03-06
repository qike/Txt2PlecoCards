# Txt2PlecoCards
A python tool to convert a plain text file of Chinese characters into Pleco cards, 
an XML file following [PLECO] (https://www.pleco.com/) schema.
The generated xml file can then be imported into PLECO as flashcards.

## Usage
 <code>Txt2PlecoCards.py  input_text_file  category  output_PLECO_xml_file</code>

For example: Txt2PlecoCards.py './book1.txt' 'Book 1' './1.xml'

To use the tool, make sure the template.xml file exists in the same folder of *Txt2PlecoCards.py*.

Update teamplate.xml file to change deault creator etc.


