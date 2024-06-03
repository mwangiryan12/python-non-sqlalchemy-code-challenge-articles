class Article:
    all = []
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)

    @property
    def title(self):
        return self._title
        
    @title.setter
    def title(self,value):  
        if isinstance(value,str) and (hasattr(self,'title')==False):
            self._title = value
            
                

class Author:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value,str) and (hasattr(self,'name')==False):
            self._name = value

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        magz = set([article.magazine for article in self.articles()])
        return list(magz)

    def add_article(self, magazine, title):
        return Article(self,magazine,title)

    def topic_areas(self):
        topics = set([article.magazine.category for article in self.articles()]) 
        if len(topics) == 0:
            return None
        else:
            return list(topics)

class Magazine:

    def __init__(self, name, category):
        self.name = name
        self.category = category
     
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,value):
        if isinstance(value,str) and 2<=len(value)<=16:
            self._name = value

    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self,value):
        if isinstance(value,str) and len(value)>0:
            self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]
        

    def contributors(self):
        return list(set([article.author for article in self.articles()]))
    

    def article_titles(self):
        titles = [article.title for article in self.articles()]
        if len(titles)>0:
            return titles
        else:
            return None
        

    def contributing_authors(self):
        contrAuth = {article.author for article in self.articles()}
        moreThanTwo = [author for author in contrAuth if sum(1 for art in self.articles() if art.author == author) > 2]
        if (len(moreThanTwo)>0):
            return moreThanTwo
        else:
            return None