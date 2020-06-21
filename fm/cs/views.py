from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import UpdateView
from django.views.generic.edit import FormView
from django.views.generic.list import MultipleObjectMixin
from .models import Request
from .models import vendor
from .forms import RequestForm
import simplejson as json



# Create your views here.

class vendorview(TemplateView):
    template_name = "cs/vendor_list.html"

class Requestview(MultipleObjectMixin, CreateView):
    model = Request
    fields = "__all__"
    template_name = "cs/request.html"
    success_rul = "cs/request/"

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset() # DB에서 레코드들을 꺼내오는 메소드get_queryset()
        # get_queryset() 메소드는 어느쪽에 있는 것을 호출할까? (MultipleObjectMixin, CreateView)
        # 이럴 때 순서가 중요하다, 앞에 있는 클래스를 먼저 봐서 이 클래스에 get_queryset 메소드가
        # 있다면 그걸 호출하고, 거기에 없으면 CreateView에서 찾아서 get_queryset() 메소드를 호출
        # 둘 다 get_queryset() 메소드가 있기 때문에 MultipleObjectMixin 에 있는 것이 호출된다.
        return super().get(request, *args, **kwargs)
        # 상위 클래스(Requestview)의 get 메소드를 그대로 호출하게 되면, CreateView클래스의
        # get_context_data 메소드가 호출되고, 이 메소드에서 object_list라는 context변수가
        # 템플릿에 넘어가게 되는 것이다.
        # 그리고 상위 클래스의 메소드를 오버라이딩 할 때는 인자는 동일하게 써줘야 한다.

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs) # 인자는 동일하게


class RequestUpdateView(UpdateView):
        model = Request
        field = ['text']
        template_name_suffix = ""


# class RequestFormview(FormView):
#     form_class = RequestForm
#     template_name = "cs/request.html"
#     success_url = "/cs/request/"

#     def form_valid(self, form):
#         form.save()
#         return super(RequestFormview, self).form_valid(form)


class RequestDelete(DeleteView):
    model = Request
    success_url = "/cs/request/"
    context_object_name = "request_list"

def text(request):
    send_text = request.POST['send_text']
    context = {'send_text' : send_text }
    return render(request, 'only_table.html', context)