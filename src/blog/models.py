# -*- coding: utf-8 -*-
from django.db.models import permalink, signals
from google.appengine.ext import db
from ragendja.dbutils import cleanup_relations

class Blog(db.Model):
    user = db.ReferenceProperty(User)
    url_prefix = db.StringProperty(requited=True)

class Post(db.Model):
    author = db.ReferenceProperty(User)
    
    title = db.StringProperty(required=True)
    intro = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    
    ip = db.StringProperty()

    published = db.BooleanProperty(default=False)
    shared = db.BooleanProperty(default=False)
    
    comment_num = db.IntegerProperty(default=0)
    view_num = db.IntegerProperty(default=0)
    
    tags = db.ListProperty(db.Key)
    category = db.ReferenceProperty(Category)
    
    created_date = db.DateTimeProperty(auto_now_add=True)
    modified_date = db.DateTimeProperty(auto_now=True)

class Comment(db.Model):
    post = db.ReferenceProperty(Post)
    parent = db.SelfReferenceProperty(verbose_name='Parent', collection_name='children')
    
    user = db.ReferenceProperty(User)
    user_name = db.StringProperty(required=True)
    user_email = db.EmailProperty()
    user_homepage = db.LinkProperty()
    user_ip = db.StringProperty()
    
    # 屏蔽
    shield = db.BooleanProperty()
    
    content = db.TextProperty()
    modified_date = db.DateTimeProperty(auto_now=True)
    
class Tag(db.Model):
    name = db.StringProperty(required=True)
    parent = db.SelfReferenceProperty(verbose_name='Parent', collection_name='children')
    count = db.IntegerProperty(default=0)
    
    @property
    def posts(self):
        return Post.gql("Where tags = :1", self.key())
    
class Category(db.Model):
    name = db.StringProperty(requited=True)
    intro = db.StringProperty()
    order = db.IntegerProperty()
    count = db.IntegerProperty(default=0)

class User(db.Model):
    user = db.UserProperty(requited=True)
    nick_name = db.StringProperty()


