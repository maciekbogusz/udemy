from unittest import TestCase
from unittest.mock import patch
from blog import Blog
from post import Post
import app

class AppTest(TestCase):
    def setUp(self):
        blog = Blog('Test', 'Test Author')
        app.blogs = {'Test': blog}
           
    def test_menu_prints_prompt(self):
        with patch('builtins.input', return_value = 'q') as mocked_print:
            app.menu()
            mocked_print.assert_called_with(app.MENU_PROMPT)

    def test_menu_calls_prints_blogs(self):
        with patch('app.print_blogs') as mocked_print_blogs:
            with patch('builtins.input', return_value = 'q'):
                app.menu()
                
                mocked_print_blogs.assert_called()
              
    def test_print_blogs(self):
        with patch('builtins.print') as mocked_print:
            app.print_blogs()
              
            mocked_print.assert_called_with('- Test by Test Author (0 posts)')
      
    def test_ask_create_blog(self):
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Test Author')
            app.ask_create_blog()
            
            self.assertIsNotNone(app.blogs.get('Test'))
              
    def test_ask_read_blog(self):
        blog = app.blogs['Test']
       
        with patch('builtins.input', return_value = 'Test'):
            with patch('app.print_posts') as mocked_print_posts:
                app.ask_read_blog() 
               
                mocked_print_posts.assert_called_with(blog)
 
    def test_print_posts(self):
        blog = app.blogs['Test']
        blog.create_post('Post title', 'Post content')
        
        with patch('app.print_posts') as mocked_print_post:
            app.print_posts(blog)
             
            mocked_print_post.assert_called_with(blog.posts[0])
             
    def test_print_post(self):
        post = Post('Post Title', 'Post Content')
        expected_print = """
--- Post Title ---

Post Content

"""
        with patch('builtins.print') as mocked_print:
            app.print_post(post)
            
            mocked_print.assert_called_with(expected_print)
            
    def test_ask_create_post(self):
        blog = app.blogs['Test']
        app.print_posts(blog)
        with patch('builtins.input') as mocked_input:
            mocked_input.side_effect = ('Test', 'Post Title', 'Post Content')
            app.ask_create_post()
            
            self.assertEqual(blog.posts[0].title, 'Post Title')
            self.assertEqual(blog.posts[0].content, 'Post Content')
           
            