from rest_framework.viewsets import ModelViewSet
import json
from time import time
from rest_framework import status
from .models import User,UserComment,UserPost
from .serializers import UserSerializer,CommentSerializer,PostSerializer
from django.http import HttpResponse ,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .funtion.User import authentication
from .funtion.post import saveData,getPostAll,getPostAllWithParameter,getlistPostWithPostId,getALLlistPostWithUserId,getComment,UpdateComment,UpdatePost
from .funtion.map import getQueryTodict,checkKey
from django.http import JsonResponse


@csrf_exempt
def CreatePost(request) :
    if request.method == 'POST' :
        print(request.META.get('HTTP_AUTHORIZATION'))
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user:
            if user.status == 2 :
                data = json.loads(request.body)
                data["user_id"] = user.user_id
                data["time_stamp"] = int(time())
                post =  PostSerializer(UserPost(),data=data)
                return saveData(post)
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def CreateComment(request) :
    if request.method == 'POST' :
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user :
            if user.status == 2 :
                data = json.loads(request.body)
                if getlistPostWithPostId(data['post_id']) :
                    data["user_id"] = user.user_id
                    data["time_stamp"] = int(time())
                    comment =  CommentSerializer(UserComment(),data=data)
                    return saveData(comment)
                else : 
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def EditPost(request) :
    if request.method == 'POST' :
        print(request.META.get('HTTP_AUTHORIZATION'))
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user:
            if user.status == 2 :
                return UpdatePost(json.loads(request.body),user.user_id)
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)    


@csrf_exempt
def EditComment(request) :
    if request.method == 'POST' :
        print(request.META.get('HTTP_AUTHORIZATION'))
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user:
            if user.status == 2 :
                return UpdateComment(json.loads(request.body),user.user_id)
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)   

@csrf_exempt
def ListPostWithPostId(request) :
    if request.method == 'GET' :
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user :
            if user.status == 2 :
                query = getQueryTodict(request.META.get("QUERY_STRING"))
                if checkKey(query,"id") :
                    return getlistPostWithPostId(int(query["id"]))
                else :
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def ListALLPostWithUserId(request) :
    if request.method == 'GET' :
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user :
            if user.status == 2 :
                query = getQueryTodict(request.META.get("QUERY_STRING"))
                if len(query)>0 :
                    return getALLlistPostWithUserId(query)
                else :
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
                  
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def ListALLPost(request) :
    if request.method == 'GET' :
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user :
            if user.status == 2 :
                query = getQueryTodict(request.META.get("QUERY_STRING"))
                if len(query) > 0 :
                    return getPostAllWithParameter(query)
                else :
                    return JsonResponse(data=getPostAll() ,safe=False,status=status.HTTP_200_OK )
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)


@csrf_exempt
def ListComment(request) :
    if request.method == 'POST' :
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user :
            if user.status == 2 :
                data = json.loads(request.body)
                if checkPost(data['post_id']) :
                    data["user_id"] = user.user_id
                    data["time_stamp"] = int(time())
                    comment =  CommentSerializer(data=data)
                    return saveData(comment)
                else : 
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)

    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

@csrf_exempt
def ListComment(request) :
    if request.method == 'GET' :
        user = authentication(request.META.get('HTTP_AUTHORIZATION'))
        if user :
            if user.status == 2 :
                query = getQueryTodict(request.META.get("QUERY_STRING"))
                if len(query)>0 :
                    return getComment(query)
                else :
                    return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
                  
            else :
                return HttpResponse(status=status.HTTP_403_FORBIDDEN)
        else :
            return HttpResponse(status=status.HTTP_401_UNAUTHORIZED)
    else :
        return HttpResponse(status=status.HTTP_405_METHOD_NOT_ALLOWED)

