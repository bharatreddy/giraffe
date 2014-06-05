# Can do the search from command line:
# Example
# python srchMongoTilt.py <word>
if __name__ == "__main__":
    import querySrch
    import sys
    SrchObj = querySrch.SrchAnswer( sys.argv[1] )
    SrchObj.googSrch()

class SrchAnswer(object):
    """
    A class for to search for answers to a question.

    Author - Bharat Kunduri
    """

    def __init__( self, srchText):
        # check if the input text is of the right format
        if type(srchText) is not str:
            print "need to input a string"
            return False
        else :
            # convert to lower case
            self.srchText = srchText.lower()

    def googSrch(self):
        """
        make a search in google to check
        if there's an answer
        """
        import urllib2
        import bs4
        # form the url
        gglBaseUrl = "https://www.google.com/#q="
        finGglUrl = gglBaseUrl + self.srchText
        # get the url response
        rspnsGgl = urllib2.urlopen( finGglUrl )
        gglPage = rspnsGgl.read()
        # soupify
        gglSoup = bs4.BeautifulSoup( gglPage )
        gglAns = gglSoup.findAll('div', attrs={'class':'srg'})
        print gglAns