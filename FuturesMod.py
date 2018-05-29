'''
Created on Jun 21, 2016

@author: shai
'''
import sys

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class writeArray():
    s = str()
    
    def write(self, line):
        self.s = ''.join([self.s, line])
        

def stockFileReader(filename):
    rsrcmgr = PDFResourceManager(caching=True)
    outfp = writeArray()
    device = TextConverter(rsrcmgr, outfp, codec='latin',
                           laparams=LAParams(), imagewriter=None)
    fp = file(filename, 'r')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    page = list(PDFPage.get_pages(fp, set(), caching=True))[0]
    interpreter.process_page(page)
    fp.close()
    device.close()
    
    s = outfp.s
    print s
    """"s = s.split('\n')
    s = [s1 for s1 in s if s1]
    l = [s1 for s1 in s if 'Russell' in s1]
    j = s.index(l[-1]) + 1
    
    print 'Value   Key'
    for k in range(22):
        print s[j + k]
    """

stockFileReader('../../../Data/PDFs/tech 060216.pdf')