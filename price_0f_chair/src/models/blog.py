__author__ = 'Narcisse'

from datetime import datetime
import uuid
from models.post import Post
from database import Database



class Blog(object):

    def __init__(self,author,title,description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id


    @staticmethod
    def new_post(_id,_author):
        title = input('Enter the post title: ')
        content = input('Enter the post content: ')
        date = input('Enter the date or leave blanck for today date(format DD/MM/YYYY): ')

        if date =="":
            current_date_time = datetime.utcnow()
        else: 
            date_to_string = date + ' ' + datetime.now().strftime("%H:%M:%S")
            current_date_time = datetime.strptime(date_to_string, "%d/%m/%Y %H:%M:%S")

        post = Post(blog_id=_id,
            title=title,
            content=content,
            author =_author, 
            date = current_date_time
            )
        post.save_to_mongo()

    
    def get_posts(self):
        return Post.get_from_mongo_blog(self.id)

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
