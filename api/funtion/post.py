from ..models import UserPost,UserComment
from rest_framework import status
from django.http import HttpResponse,JsonResponse
from ..serializers import PostSerializer,CommentSerializer
from .map import checkKey
import json

def saveData(data) :
    if data.is_valid() :
        data.save()
        return HttpResponse(status=status.HTTP_201_CREATED)
    else :
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

def getlistPostWithPostId(post_id):
    serializer = PostSerializer(UserPost.objects.filter(post_id=post_id), many=True)
    print(serializer)
    json_data = json.dumps(serializer.data)
    if json_data != "[]" :
            return JsonResponse(data=json_data,status=status.HTTP_200_OK,safe=False)
    else :
        return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False) 


def getALLlistPostWithUserId(data):
    if checkKey(data,'id') and not(checkKey(data,'limit')) and not(checkKey(data,'start') and checkKey(data,'end')):
        serializer = PostSerializer(UserPost.objects.filter(user_id=int(data['id'])).order_by('-time_stamp'), many=True)
        json_data = json.dumps(serializer.data)
        if json_data != "[]" :
            return JsonResponse(data=json_data,status=status.HTTP_200_OK,safe=False)
        else :
            return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False) 
    elif checkKey(data,'id') and checkKey(data,'limit') and not(checkKey(data,'start') and checkKey(data,'end')):
        if int(data['limit']) <=100 :
            serializer = PostSerializer(UserPost.objects.filter(user_id=int(data['id'])).order_by('-time_stamp')[:int(data['limit'])], many=True)
            json_data = json.dumps(serializer.data)
            if json_data != "[]" :
                return JsonResponse(data=json_data,status=status.HTTP_200_OK,safe=False)
            else :
                return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False)
        else : 
            return JsonResponse(data = json.dumps({"status" : status.HTTP_400_BAD_REQUEST ,"detail" : "Max limit is 100"}),
                                status=status.HTTP_400_BAD_REQUEST,safe=False)
    elif checkKey(data,'id') and checkKey(data,'start') and checkKey(data,'end') :
        if int(data['end']) - int(data['start']) <= 100 :
            serializer = PostSerializer(UserPost.objects.all().order_by('-time_stamp')[int(data['start']):int(data['end'])], many=True)
            json_data = json.dumps(serializer.data)
            if json_data != "[]" :
                return JsonResponse(data=json_data,status=status.HTTP_200_OK,safe=False)
            else :
                return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False)
        else : 
            return JsonResponse(data = json.dumps({"status" : status.HTTP_400_BAD_REQUEST ,"detail" : "Max limit is 100"}),
                                status=status.HTTP_400_BAD_REQUEST,safe=False)
    else :
        HttpResponse(status=status.HTTP_400_BAD_REQUEST)
     
def getPostAll() :
    serializer = PostSerializer(UserPost.objects.all().order_by('-time_stamp')[:10], many=True)
    return json.dumps(serializer.data)

def getPostAllWithParameter(data) :
    if checkKey(data,'limit') :
        if int(data['limit']) <= 100 :
            serializer = PostSerializer(UserPost.objects.all().order_by('-time_stamp')[:int(data['limit'])], many=True)
            return JsonResponse(status = status.HTTP_200_OK ,data=json.dumps(serializer.data) ,safe=False)   
        else :
            return JsonResponse(data = json.dumps({"status" : status.HTTP_400_BAD_REQUEST ,"detail" : "Max limit is 100"}),
                                                    status=status.HTTP_400_BAD_REQUEST,safe=False)

    elif checkKey(data,'start') and checkKey(data,'end') :
        if int(data['end']) - int(data['start']) <= 100 :
            serializer = PostSerializer(UserPost.objects.all().order_by('-time_stamp')[int(data['start']):int(data['end'])], many=True)
            json_data = json.dumps(serializer.data)
            if json_data != "[]" :
                return JsonResponse(status = status.HTTP_200_OK ,data=json_data,safe=False) 
            else :
                return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False) 

        else :
            return JsonResponse(data = json.dumps({"status" : status.HTTP_400_BAD_REQUEST ,"detail" : "Max limit is 100"}),
                                                    status=status.HTTP_400_BAD_REQUEST,safe=False)
    else :
        HttpResponse(status=status.HTTP_400_BAD_REQUEST)


def getComment(data):
    if checkKey(data,'id') and not(checkKey(data,'limit')) and not(checkKey(data,'start') and checkKey(data,'end')):
        serializer = CommentSerializer(UserComment.objects.filter(post_id=int(data['id'])).order_by('-time_stamp'), many=True)
        json_data = json.dumps(serializer.data)
        if json_data != "[]" :
            return JsonResponse(data=json_data,status=status.HTTP_200_OK,safe=False)
        else :
            return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False) 
    elif checkKey(data,'id') and checkKey(data,'limit') and not(checkKey(data,'start') and checkKey(data,'end')):
        if int(data['limit']) <=100 :
            serializer = CommentSerializer(UserComment.objects.filter(post_id=int(data['id'])).order_by('-time_stamp')[:int(data['limit'])], many=True)
            json_data = json.dumps(serializer.data)
            if json_data != "[]" :
                return JsonResponse(data=json_data,status=status.HTTP_200_OK,safe=False)
            else :
                return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False)
        else : 
            return JsonResponse(data = json.dumps({"status" : status.HTTP_400_BAD_REQUEST ,"detail" : "Max limit is 100"}),
                                status=status.HTTP_400_BAD_REQUEST,safe=False)
    elif checkKey(data,'id') and checkKey(data,'start') and checkKey(data,'end') :
        if int(data['end']) - int(data['start']) <= 100 :
            serializer = CommentSerializer(UserComment.objects.filter(post_id=int(data['id'])).order_by('-time_stamp')[int(data['start']):int(data['end'])], many=True)
            json_data = json.dumps(serializer.data)
            if json_data != "[]" :
                return JsonResponse(data=json_data,status=status.HTTP_200_OK,safe=False)
            else :
                return JsonResponse(status = status.HTTP_204_NO_CONTENT ,data=json.dumps({"detail" : "NO CONTENT"}),safe=False)
        else : 
            return JsonResponse(data = json.dumps({"status" : status.HTTP_400_BAD_REQUEST ,"detail" : "Max limit is 100"}),
                                status=status.HTTP_400_BAD_REQUEST,safe=False)
    else :
        HttpResponse(status=status.HTTP_400_BAD_REQUEST)


def UpdatePost(data,user_id) :
    serializer = PostSerializer(UserPost.objects.filter(post_id=data['post_id']), many=True).data
    if user_id == serializer[0]['user_id'] :
        obj, created  =  UserPost.objects.update_or_create(post_id=data['post_id'],defaults={"content":data['content']})
        if created :
            obj.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        else :
            return HttpResponse(status=status.HTTP_200_OK)

    else :
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)

    
def UpdateComment(data,user_id) :
    serializer = CommentSerializer(UserComment.objects.filter(comment_id=data['comment_id']), many=True).data
    if user_id == serializer[0]['user_id'] :
        obj, created  =  UserComment.objects.update_or_create(comment_id=data['comment_id'],defaults={"content":data['content']})
        if created :
            obj.save()
            return HttpResponse(status=status.HTTP_201_CREATED)
        else :
            return HttpResponse(status=status.HTTP_200_OK)

    else :
        return HttpResponse(status=status.HTTP_403_FORBIDDEN)

