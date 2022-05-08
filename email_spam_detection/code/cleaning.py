# cfaee4743c333c949bdb1f0120168caa9b51d76a
import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
class Cleaning:

    def __init__(self,data:list):
        self.data=data
        self.ps = PorterStemmer()
        self.lemmatizer = WordNetLemmatizer()

    def supprimer_nombre(self,text)->str:
        """
        Function to remove any number within  text
        """
        text_nombre=re.sub('[0-9]','',text)
        return text_nombre
    def supprimer_email(self,text_url)->str:

        text_email=re.sub('\S*@\S*\s?','',text_url)
        return text_email    
    def supprimer_caract_speciaux(self,text_nombre)->str:

        text_speciaux=re.sub('[^a-zA-Z]+',' ',text_nombre)
        return text_speciaux
    def normalisation(self,text_space)->str:

        text_lower=text_space.lower()
        return text_lower
    def supprimer_espace(self,text_speciaux)->str:
        text_space=text_speciaux.strip()
        return text_space
    def supprimer_path(self,text)->str:
        text_url=re.sub(r'http\S+', ' ', text)
        return text_url
    def lematization(self,email:str)->str:
        words =[]
        for w in word_tokenize(email):
            words.append(self.lemmatizer.lemmatize(w))
        email=' '.join(words)
        return email
    def stemming(self,email:str)->str:
        words =[]
        for w in word_tokenize(email):
            words.append(self.ps.stem(w))
        email=' '.join(words)
        return email

    def processing(self):
        clean_data=[]
        for comment in self.data :
          a= self.supprimer_nombre(comment[0])
          a= self.supprimer_email(a)
          a= self.supprimer_path(a)
          a= self.supprimer_caract_speciaux(a)
          a=self.supprimer_espace(a)
          a=self.normalisation(a)
          a=self.remove_stopwords(a)
          a=self.stemming(a)
          #a=lematization(a)
          a=self.remove_stopwords(a)
          clean_data.append([a,comment[1]])
        return clean_data

    def remove_stopwords(self,email:str)->str:
        words =[]
        for w in word_tokenize(email):
            if w not in stopwords.words('english'):
                words.append(w)
        email=' '.join(words)
        return email