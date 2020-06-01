from django.db import models
import json

class User(models.Model) :
    user_id = models.AutoField(primary_key=True)
    email =  models.CharField(max_length=64,unique=True)
    password = models.CharField(max_length=32)
    username = models.CharField(max_length=32,unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    status = models.IntegerField(default=1)
    
    def __repr__(self) :
        return json.dumps({"user_id" : self.user_id,
                "email": self.email,
                "username":self.username,
                "first_name":self.first_name,
                "last_name":self.last_name,
                "status":self.status})


class UserPost(models.Model) :
    post_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    title = models.CharField(max_length=128)
    content = models.CharField(max_length=1024)
    time_stamp = models.IntegerField()

    def __repr__(self) :
        return json.dumps({"post_id" : self.post_id,
                "user_id": self.user_id,
                "title":self.title,
                "content":self.content,
                "time_stamp":self.time_stamp})    

class UserComment(models.Model) :
    comment_id =  models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    post_id = models.IntegerField()
    content = models.CharField(max_length=512)
    time_stamp = models.IntegerField()

    def __repr__(self) :
        return json.dumps({"comment_id" : self.comment_id,
                "user_id": self.user_id,
                "post_id":self.post_id,
                "content":self.content,
                "time_stamp":self.time_stamp})



