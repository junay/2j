# -*- coding: utf-8 -*-
from django.db.models import permalink, signals
from google.appengine.ext import db
from ragendja.dbutils import cleanup_relations
# TODO     #share = db. #共享分类【 0：私有，1：家人，2：朋友， 3：所有 】

class Blog(db.Model):
    pass

class Post(db.Model):
    author = db.UserProperty()
    
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
    
    user = db.UserProperty()
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

class ShareLevel(db.Model):
    pass

class User(db.Model):
    pass
