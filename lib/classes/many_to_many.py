class Author:
    all = []

    def __init__(self, name):
        self.name = name
        type(self).all.append(self)


    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else: 
            raise Exception("Name must be a string with at least one character")


    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list({article.magazine for article in Article.all if article.author == self})

    def add_article(self, new_magazine, new_title):
        return Article(self, new_magazine, new_title)

    def topic_areas(self):
        return list({article.magazine.category for article in Article.all if article.author == self})


author = Author("Carry Bradshaw")


class Magazine:
    
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and 2 <= len(name) <= 16:
            self._name = name

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if isinstance(category, str) and len(category) > 0:
            self._category = category

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in Article.all if article.magazine == self})

    def article_titles(self):
        return list({article.title for article in Article.all if article.magazine == self})

    def contributing_authors(self):
        return list({article.author for article in Article.all if article.magazine == self})

magazine = Magazine("Vogue", "Fashion")

class Article(Author, Magazine):
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        type(self).all.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and 5 <= len(title) <= 50:
            self._title = title

    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, author):
        if isinstance(author, Author):
            self._author = author
    
    @property 
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, magazine):
        if isinstance(magazine, Magazine):
            self._magazine = magazine


article = Article(author, magazine, "How to wear a tutu with style")



print(article.article_titles())