from rest_framework import serializers
from .models import User,UserPost,UserComment

class UserSerializer(serializers.ModelSerializer) :
    email =  serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=32)
    username = serializers.CharField(max_length=32)
    first_name = serializers.CharField(max_length=64)
    last_name = serializers.CharField(max_length=64)
    status = serializers.IntegerField()

    class Meta() :
        model = User
        fields = ('email', 'password', 'username','first_name','last_name','status')

    def create(self, validated_data):
        return User(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.password = validated_data.get('password', instance.password)
        instance.username = validated_data.get('username', instance.username)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.status = validated_data.get('status', instance.status)
        
        instance.save()
        return instance
    
class PostSerializer(serializers.ModelSerializer) :
    user_id = serializers.IntegerField()
    title = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=1024)
    time_stamp = serializers.IntegerField()
    

    class Meta() :
        model = UserPost
        fields = ('post_id','user_id', 'title', 'content','time_stamp')

    def create(self, validated_data):
        return UserPost(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.time_stamp = validated_data.get('time_stamp', instance.time_stamp)
        instance.save()
        return instance
    

class CommentSerializer(serializers.ModelSerializer) : 
    user_id = serializers.IntegerField()
    post_id = serializers.IntegerField()
    content = serializers.CharField(max_length=512)
    time_stamp = serializers.IntegerField()

    class Meta() :
        model = UserComment
        fields = ('comment_id','user_id', 'post_id', 'content','time_stamp')

    def create(self, validated_data):
        return UserComment(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.post_id = validated_data.get('post_id', instance.post_id)
        instance.content = validated_data.get('content', instance.content)
        instance.time_stamp = validated_data.get('time_stamp', instance.time_stamp)
        instance.save()
        return instance
