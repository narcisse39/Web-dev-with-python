__author__ = 'Narcisse'

import datetime
import uuid
from models.post import Post
from database import Database



class Blog(object):

    def __init__(self,author,title,description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        title = input('Enter the post title: ')
        content = input('Enter the post content: ')
        date = input('Enter the date or leave blanck for today date(format DDMMYYYY): ')
        post = Post(blog_id=self.id,
            title=title,
            content=content,
            author =self.author, 
            date = datetime.datetime.utcnow()
            )
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_mongo(self.id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json_file())

    def json_file(self):
        return{
            'title': self.title,  
            'author': self.author  ,
            'description': self.description  ,
            'id': self.id 
        }

    @staticmethod
    def get_from_mongo(id):
        blog_data = Database.find_one(collection='blogs',query={'id':id})
        return blog_data
