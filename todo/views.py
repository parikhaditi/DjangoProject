from django.shortcuts import render, redirect
from django.contrib import messages
 
## import todo form and models
 
from .forms import TodoForm
from .models import Todo
import os
 
###############################################
def newindex(request):
    return render(request, 'todo/newindex.html')

def embedding(request): 
    #the task which you want to perform from   python program 
    print("Hii..!")
    os.system('python extract_embeddings.py --dataset dataset --embeddings output/embeddings.pickle --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7')
    return render (request, 'todo/newindex.html') 

def train(request): 
    #the task which you want to perform from   python program 
    print("Hii..!")
    os.system('python train_model.py --embeddings output/embeddings.pickle --recognizer output/recognizer.pickle --le output/le.pickle')
    return render (request, 'todo/newindex.html') 

def recognize_video(request): 
    #the task which you want to perform from   python program 
    print("Hii..!")
    os.system('python recognize_video.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle')
    return render (request, 'todo/newindex.html')

def recognize(request): 
    #the task which you want to perform from   python program 
    print("Hii..!")
    os.system('python recognize.py --detector face_detection_model --embedding-model openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le output/le.pickle --image images/aditi.jpg')
    return render (request, 'todo/newindex.html') 

def index(request):
 
    item_list = Todo.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    form = TodoForm()
 
    page = {
             "forms" : form,
             "list" : item_list,
             "title" : "TODO LIST",
           }
    return render(request, 'todo/index.html', page)
 
 
 
### function to remove item, it receive todo item_id as primary key from url ##
def remove(request, item_id):
    item = Todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "item removed !!!")
    return redirect('todo')