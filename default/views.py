from django.shortcuts import render
from django.views.generic import ListView, DetailView, RedirectView,CreateView,UpdateView,DeleteView #新增修改刪掉
from .models import Poll, Option

# Create your views here.
def poll_list(req):
    data = Poll.objects.all()
    return render(req, 'poll_list.html', {'polls':data})

class PollList(ListView):
    model = Poll

class PollDetail(DetailView):
    model = Poll

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['option_list'] = Option.objects.filter(poll_id=self.kwargs['pk'])
        return ctx

class PollVote(RedirectView):

    def get_redirect_url(self, *args, **kwargs):
        op = Option.objects.get(id=self.kwargs['oid'])
        op.count += 1
        op.save()
        return "/poll/{}/".format(op.poll_id)
class PollCreate(CreateView): #CreatView找應用程式底下的temp>defalut
    model = Poll #必要 
    fields = ['subject','desc'] #顯示subject,desc #顯示全部'__all__' #必要
    #success_url = "/poll/" #/poll/主機後開始 #poll/原網址多加poll/
    # template_name = 'general_form.html' 自己指定頁面範本
    #固定不動的success_url 
    #不固定的
    def get_success_url(self):
       return "/poll/{}/".format(self.object.id)
    #sellf(PollCreate) 
class PollEdit(UpdateView): #撈與pk相同的id
    model = Poll
    fields = ['subject','desc']
    def get_success_url(self):
        return "/poll/{}/".format(self.object.id)
#CreateView與UpdateView很相同 只是一個是新增一個是修改