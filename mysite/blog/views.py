from django.views import generic
from .models import Post
from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category
from django.shortcuts import render
from .models import Post



# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

def about(request):
    return render(request, "about.html")   

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def home(request):
    return render(request, 'base.html')    

class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='1')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context
    
def about(request):
    return render(request, 'about.html')    

def feature(request):
    return render(request, 'feature.html')     

# def searchBar(request):
#     if request.method == 'GET':
#         query = request.GET.get('query')
#         if query:
#             Post = Post.objects.filter(title_icontains=query)
#             return render(request, 'searchbar.html',{'Post':Post})
#         else:
#             print("No information to show")
#             return request(request, 'searchbar.html',{})    

def searchBar(request):
    query = request.GET.get('q')
    results = Post.objects.filter(title__icontains=query)
    return render(request, 'searchbar.html', {'results': results})