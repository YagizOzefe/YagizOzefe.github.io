from django.shortcuts import render,redirect,get_object_or_404
from .models import * #Model 1
from .forms import * #Form 1
# Create your views here.

def index(request):
    if request.user.is_authenticated: # Kullanıcı girişlisyse

        # todo = Todo.objects.all() #Model 2 Modelden almak istediğin yapıları çek - object.all hepsini alır
        todo = Todo.objects.filter(user = request.user)
        if request.method == 'POST': # Htmlden admin tarafına veri göndericeğimiz zaman bu methodu kullanırız.
            #! Html tarafında ilgili yapı Formun içinde ve type submit olmalıdır !
            form = TodoForm(request.POST)
            if form.is_valid():
                userTodo = form.save(commit=False) # Onayla ama veri tabanına kaydetme
                userTodo.user = request.user
                userTodo.save()
                return redirect('index')
        else:
            
            form = TodoForm() #Form 2 görüntülencek olan formu tanımladık.

        context = {
            'todo':todo, #Model3
            'form':form # Form 3
        }
        return render(request,'index.html',context)
    else:
        return render(request,'index.html')


def todoDetay(request,d_slug):
    todo = get_object_or_404(Todo, slug = d_slug)
    context = {
        'todo':todo,
    }
    return render(request,'todoDetay.html',context)

def sil(request):
    if request.method == 'POST':
        todoId = request.POST['sil']
        sil = Todo.objects.get(id = todoId) # İlk değeri veri tabanından alır ve kendi belirlediğimiz id ile eşleşirse silme işlemine devam eder
        sil.delete()
        return redirect('index')


