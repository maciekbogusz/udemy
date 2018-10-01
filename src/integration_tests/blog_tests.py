from unittest import TestCase
from blog import Blog
from post import Post

class BlogTest(TestCase):
    def test_repr_multiple_posts(self):
        b = Blog('Test', 'Test Author')
        b.posts = ['test']
        b2 = Blog('My day', 'Rolf')
        b2.posts  = ['test', 'another']
        
        
        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'My day by Rolf (2 posts)')
           
    def test_create_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
        
        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')
        
    def test_json_no_posts(self):
        b = Blog('Test', 'Test Author')
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [],
            }
        
        self.assertDictEqual(expected, b.json()) 
      
    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.create_post('Test Post', 'Test Content')
       
        expected = {
            'title': 'Test',
            'author': 'Test Author',
            'posts': [
                {
                    'title': 'Test Post', 
                    'content': 'Test Content'
                }
            ]
        }
        
        self.assertDictEqual(expected, b.json())