from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render,HttpResponse
import json
from UserActivity.models import User,UserActivity

# Create your views here.
def user(request):
    if request.method =="POST":
        file=request.FILES.get("file")
        json_file=json.load(file)

        try:
            for i in json_file['members']:
                user_object=User(user_id=i['id'],name=i['real_name'],tz=i['tz'])
                user_object.save()
                for j in i['activity_periods']:
                    user_object1 = User.objects.get(user_id=i['id'])
                    user_activity_object = UserActivity(user_id=user_object1, start_time=j['start_time'],
                                                        end_time=j['end_time'])
                    user_activity_object.save()
            user_activity_object = UserActivity.objects.all()
            return render(request, 'userActivity.html', {"data": user_activity_object})
        except:
            return HttpResponse("Error ")

    return render(request, 'UserActivityForm.html')


@api_view(['GET'])
def user_activity(request):
    if request.method == 'GET':
        data2=[]
        member=[]
        user_id = []
        user_activity_object = UserActivity.objects.all()
        user_object = User.objects.all()
        for data in user_object:
            user_id.append(data.user_id)
            user_object1 = User.objects.get(user_id=data.user_id)
        user=len(user_id)
        for user_data in range(user):

            start_time = []
            end_time = []
            activity_periods = []
            user1 = {"id":user_object1.user_id, "real_name": user_object1.name, "tz": user_object1.tz,"activity_periods":member}
            for data1 in user_activity_object:
                if data1.user_id.user_id == user_id[user_data]:
                    start_time.append(data1.start_time)
                    end_time.append(data1.end_time)
            for i, j in zip(start_time, end_time):
                dict = {"start_time": i, "end_time": j}
                activity_periods.append(dict)
            if len(activity_periods) >= 1:
                for value in activity_periods:
                    member.append(value)
                data2.append(user1)
        content = {"ok": "true","members":data2}
        return Response(content)
    else:
        return Response('incorrect data')



