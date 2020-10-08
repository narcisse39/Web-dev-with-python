__author__ = 'Narcisse'

from models.blog import Blog
from models.post import Post
from database import Database

class Menu(object):

    def __init__(self):

        self.user_blog = None
        self.blog_id = list()

        #Ask user for author name
        self.user = input('Enter your author name: ')

        #Check if they have already got an account
        if self._user_has_account():
            print('Welcome back {}'.format(self.user))
        #if not, prompt them to create one
        else:
            self._prompt_user_for_account()
            
        
    def _user_has_account(self):
        #Check the blog database
        #To see if the author exist
        blog = Database.find_one('blogs',{'author': self.user})
        if blog is not None:
            self.user_blog = Blog.get_from_mongo(blog['id'])
            return True
        else:
            return False
    

    def _prompt_user_for_account(self):
        #Start a blog
        title= input('Enter blog title: ')
        description= input('Enter description: ')
        blog = Blog(author= self.user,
                    title= title,
                    description= description)

        #Save blog to database
        blog.save_to_mongo()
        self.user_blog = blog
        print('Record Added to blog!')


    def run_menu(self):

        _menu_text = """
        Menu
        ====
        W. Write to database
        R. Read from database
        E. Exit 
        """

        print(_menu_text)
        read_or_write = input('Select action by inputting the character: ')
        while True:
            
          
            if read_or_write == 'R'or read_or_write == 'r' :
                """
                list blogs in database
                allow user to pick one
                display posts
                """
                self._list_blogs()
                self._view_blog()
                print('='*80)
                read_or_write = input('Select action by inputting the character: ')
                
            elif read_or_write == 'W' or read_or_write == 'w':
                
                #Blog.new_post(self.user_blog['id'],self.user)
                self.user_blog = Database.find_one('blogs',{'author': self.user})
                print('Id: {}, Author: {}'.format(self.user_blog['id'],self.user))
                Blog.new_post(self.user_blog['id'],self.user)
                print('Record Added to post!')
                print('='*80)
                read_or_write = input('Select action by inputting the character: ')
                
            else:
                print('Thank you for blogging!')
                print('='*80)
                exit()

    def _list_blogs(self):
        blogs = Database.find(collection='blogs',query={})
        _id = 1
        
        for blog in blogs:
            print('No:{} | ID: {}, Title: {}, Author: {}'.format(_id, blog['id'], blog['title'], blog['author']))
            self.blog_id.append(blog['id'])
            _id= _id + 1
        print('='*80)

    def _view_blog(self):
        
        blog_select = input('Please select the number of the id post you want to read: ')

        if blog_select != '':
            blog_to_see = self.blog_id[int(blog_select) - 1]
            blog = Blog.get_from_mongo(blog_to_see)
            post = Post.get_from_mongo_blog(blog_to_see)
            
            if post is not None:
                print('Date: {}, title: {} \n\n{}'.format(post['created_date'],post['title'],post['content']))

            #===================================================================================================
            print('')
            print('-'*20)
            print('All post by {} '.format(self.user))
            print('-'*20)
            load_all = Database.find('posts',{'author':self.user})
            for _post in load_all:
                print('Date: {}, title: {} \n\n{}'.format(_post['created_date'],_post['title'],_post['content']))  
                print('-'*30)
            #===================================================================================================
            else:
                print('No record found in the post database')

            
        else:
            print('No selection detected')
            
        
        
        

        

        