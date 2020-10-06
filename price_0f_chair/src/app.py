__author__ = 'Narcisse'

from models.post import Post
from models.blog import Blog
from database import Database

Database.initialize()

post = Post(blog_id='456',
title='Web python',
content='too tired',
author ='Jose')

#post.save_to_mongo()

#post = Post.from_mongo("63944b9abb29488e95bfd037b3178320")
print(post)



blog = Blog(author='Jose',
    title='Sample title',
    description='Sample description')
blog.new_post()
#blog.save_to_mongo()

blog_db = Blog.get_from_mongo("893c508587a147f8a3fb5cdacd4baf27")

print(blog.get_posts())



