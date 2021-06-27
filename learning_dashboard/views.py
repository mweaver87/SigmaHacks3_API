from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 

from django.views.decorators import gzip

from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse

from .models import Notes, Messages

from django.http.response import StreamingHttpResponse

import cv2
import threading

from io import StringIO
import datetime


# Create your views here.

def default(request):
    print("In Default")
    return render(request, 'learning_dashboard/dashboard.html')


def chat_function(request):
    print("chat")



def dashboard(request):
    print("In dashboard")
    return render(request, 'learning_dashboard/dashboard.html')

"""
def chat_messages(request):
    if request.method == 'POST':
        text = request.POST.get('chat_window')
        user = 'Martin'

        temp_datetime = datetime.datetime.now()
        date_temp = temp_datetime.date()
        time_temp = temp_datetime.time()

        message = Messages()
        message.date = date_temp
        message.time = time_temp
        message.test_message = text
        message.user = user
        message.save()

    #return JsonResponse({'time': time_temp, 'user':user, 'text_message': text})
    return render(request, 'learning_dashboard/classroom.html', {'time': time_temp, 'user':user, 'text_message': text})
"""

def chat_messages(request):
    if request.method == 'POST':
        text = request.POST.get('chat_window')
        user = 'Martin'

        temp_datetime = datetime.datetime.now()
        date_temp = temp_datetime.date()
        time_temp = temp_datetime.time()

        message = Messages()
        message.date = date_temp
        message.time = time_temp
        message.test_message = text
        message.user = user
        message.save()

    #return JsonResponse({'time': time_temp, 'user':user, 'text_message': text})

    return render(request, 'learning_dashboard/classroom.html', {'time': time_temp, 'user':user, 'text_message': text})

# Reference Below:
# https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage
@gzip.gzip_page
def video_feed(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass



def classroom(request):
    try:
        cam = cv2.VideoCapture(0)
        while True:
            ret_val, img = cam.read()
            if mirror: 
                img = cv2.flip(img, 1)
            cv2.imshow('my webcam', img)
            if cv2.waitKey(1) == 27: 
                break  # esc to quit
        cv2.destroyAllWindows()
    except:
        return render(request, 'learning_dashboard/classroom.html')

def save_notes(request):
    try:
        if request.method == 'POST':
            notes = request.POST.get('note_block')
            subject = request.POST.get('subject')

            temp_datetime = datetime.datetime.now()
            date_temp = temp_datetime.date()


            new_notes = Notes()
            new_notes.created = temp_datetime
            new_notes.notes = notes
            new_notes.subject = subject

            string_name = "./"(str)(date_temp) + "_" + (str)(new_notes.subject)

            new_notes.file_name = (str)(string_name) + ".txt"
            try:
                new_notes.save()
            except:
                print("Could not save model.")
                print("Created: " + (str)(new_notes.created))
                print("Subject: " + (str)(new_notes.subject))
                print("Notes: " + (str)(new_notes.notes))

            notes_string = "Creation Date: " + (str)(datetime.datetime.date()) + "\nSubject: " + (str)(new_notes.subject) + "\n\n" + (str)(new_notes.notes)

            try:

                save_notes = open(string_name + ".txt", "wt")
                file_save = save_notes.write(notes_string)
                text_file.flush()
                text_file.close()

            except:
                print("Could not save")
           
    except:
        print("could not save")

    return render(request, 'learning_dashboard/classroom.html')


def announcements(request):
    print("In announcements")
    return render(request, 'learning_dashboard/announcements.html')


def resources(request):
    print("In resources")
    return render(request, 'learning_dashboard/resources.html')



# Reference Below:
# https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage
class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        _, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()

# Reference Below:
# https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
