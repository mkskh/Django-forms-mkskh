"""Todo views."""
from django.http import HttpResponse
from django.urls import reverse
from django.shortcuts import redirect, render

from todo.models import todos
from .forms import LoginForm
from.models import User


def detail_view(request, todo_id):
    form = LoginForm()
    access = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            login = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = User.objects.get(id=1)
            if login == user.login and password == user.password:
                access = True
                id = todo_id
                todo = todos[todo_id - 1]
                previous_note = todo_id - 1 if todo_id > 1 else None
                next_note = todo_id + 1 if todo_id < len(todos) else None
                
                return render(request, "todo/details.html", 
                            {"access": access, 
                            "todo": todo, 
                            "id": id,
                            "previous_note": previous_note,
                            "next_note": next_note})
            else:
                form = LoginForm()
                return render(request, "todo/details.html", {"form": form})

    elif request.method == "GET":
        # if not access:
        form = LoginForm()
        return render(request, "todo/details.html", {"form": form})

        # elif access:
        #     pass
        

    



def details(request, todo_id):
    """Show a single todo matching the todo_id."""
    todo = todos[todo_id - 1]
    previous = "Previous todo"
    next = "Next todo"
    if todo_id - 1 > 0:
        previous_url = reverse("todo:details", args=[todo_id - 1])
        previous = f"<a href=\"{previous_url}\">Previous todo</a>"
    if todo_id < len(todos):
        next_url = reverse("todo:details", args=[todo_id + 1])
        next = f"<a href=\"{next_url}\">Next todo</a>"
    response = [
        f"<h1>To Do number {todo_id}</h1>",
        "<h3>", todo["topic"], "</h3>",
        "<p>", todo["text"], "<p>",
        "<p>", todo["status"].capitalize(), "</p>",
        previous, " | ",
        next
    ]
    return HttpResponse("".join(response))



# class ToDoDetails(View):

#     def get(self, request):
#         pass

#     def post(self, request):
#         pass
    