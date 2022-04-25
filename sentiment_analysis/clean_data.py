import re
import string

class clean_data():
    # remove URLs   
    def remove_URL(self,text):
        url = re.compile(r'https?://\S+|www\.\S+')
        return url.sub(r'',text)

    # remove htmls
    def remove_html(self,text):
        html=re.compile(r'<.*?>')
        return html.sub(r'',text)
    
    # remove punct
    def remove_punct(self,text):
        table=str.maketrans('','',string.punctuation)
        return text.translate(table)

    # remove other ...
    def remove_other (self,text) : 
        text = text.lower()
        text = re.sub('\[.*?\]', '', text)
        text = re.sub('<.*?>+', '', text)
        text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
        text = re.sub('\n', '', text)
        text = re.sub('\w*\d\w*', '', text)
        return(text)

    # clean text
    def clean (self,text) : 
        text = self.remove_URL(text)
        text = self.remove_html(text)
        text = self.remove_punct(text)
        text = self.remove_other (text)
        return text
