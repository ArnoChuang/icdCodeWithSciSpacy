import spacy

class CustomSpacyF:
    def __init__(self,model_name = "en_core_sci_lg"):
        '''
        model_name - spacy model name
        '''
        self.__nlp = spacy.load(model_name)
    
    def __del__(self):
        self.__nlp
        del self.__nlp



    #  get single word's vector from scispacy model
    def getVector(self,strList):
        aryRtn=[]
        
        tokens = self.__nlp(strList)
        
        for token in tokens:
            if token.has_vector == True:
                aryRtn = [token.text, token.vector_norm]
            else:
                aryRtn = [token.text, None]

        return aryRtn

    def getSentenceVector(self,strList,blnStayComma = False,blnStayBrackets = False):
        '''
        blnStayComma - sentence's vector consider comma.\n
        blnStayBrackets - sentence's vector consider brackets.
        '''
        
        #sentence's vector reference the location of the each word
        
        aryRtn = []

        intWordCount = 0
        intAdd = 0 # spacy thinks to symbol is independent word,so we need to count additionally
        strTitle = strList
        
        if blnStayComma == False:
            while( ((",") in strTitle) == True):
                strTitle = strTitle.replace(",","")
        else:
            intAdd = intAdd+strTitle.count(",")
        
        if (blnStayBrackets == False):
            while( (("(") in strTitle) == True ):
                idx1 = strTitle.find('(')
                idx2 = strTitle.find(')')
                strTitle = strTitle.replace(strTitle[idx1:idx2+1],"")

            while( (("[") in strTitle) == True ):
                idx1 = strTitle.find('[')
                idx2 = strTitle.find(']')
                strTitle = strTitle.replace(strTitle[idx1:idx2+1],"")

        else:
                intAdd = intAdd+strTitle.count("(")
                intAdd = intAdd+strTitle.count(")")
                intAdd = intAdd+strTitle.count("[")
                intAdd = intAdd+strTitle.count("]")

        # generally,spacy use blank to split each word
        # word count = blank split sentence's len + symbol's count
        intWordCount = len(strTitle.split(" ")) + intAdd

        #print(intWordCount)
        
        doc = self.__nlp(strTitle)

        #let token reference the location of the each word
        with doc.retokenize() as retokenizer:
            retokenizer.merge(doc[0:intWordCount], attrs={"LEMMA": strTitle}) #attrs={"DEP": strTitle} get same result
        
        #print(strTitle)
        for token in doc:
            if token.has_vector == True:
                aryRtn = [token.text, token.vector_norm]
            else:
                aryRtn = [token.text,None]

        return aryRtn