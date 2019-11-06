from django.test import TestCase
from . models import Editor,Article,tags
import datetime as dt

class EditorTestClass(TestCase):
    def setUp(self):
        self.dickson = Editor(first_name = 'dickson',last_name = 'kariuki',email = 'dicksonkariuki4@gmail.com')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.dickson,Editor))

    def test_save_method(self):
        self.dickson.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors)>0)
class ArticleTestClass(TestCase):
    def setUp(self):
        self.dickson = Editor(first_name ='dickson',last_name = 'kariuki',email = 'dicksonkariuki4@gmail.com')
        self.dickson.save_editor()
        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.dickson)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()
    
    def test_get_news_today(self):
        today_news = Article.todays_news()
        self.assertTrue(len(today_news)>0)
    
    def test_get_news_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        news_by_date = Article.days_news(date)
        self.assertTrue(len(news_by_date) == 0)
