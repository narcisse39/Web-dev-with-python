__author__ = 'Narcisse'

import datetime
import uuid

from database import Database


class Post(object):

    def __init__(self,title,content,author,blog_id,date = datetime.datetime.utcnow(), id = None):
        self.title = title
        self.content = content
        self.author = author
        self.blog_id = blog_id
        self.id = uuid.uuid4().hex if id is None else id
        self.created_date = date
    
    def json_file(self):
        return{
            'title': self.title,  
            'content': self.content ,
            'author': self.author  ,
            'blog_id': self.blog_id ,
            'id': self.id ,
            'created_date': self.created_date
        }
    
    def save_to_mongo(self):
        Database.insert(collection='posts', data=self.json_file())
    
    
    @staticmethod
    def from_mongo(id):
        post_data = Database.find_one(collection='posts',query={'id':id})
        return post_data
       

    @staticmethod
    def from_blog(id):
        return [post for post in Database.find(collection='posts',query={'id':id})]
        
        