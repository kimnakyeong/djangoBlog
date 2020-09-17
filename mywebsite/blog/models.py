from django.db import models
from django.urls import reverse
from django.shortcuts import resolve_url, redirect
# Create your models here.


# 블로그 카테고리
class Category(models.Model):
    name = models.CharField(max_length=50, help_text="블로그 글의 분류를 입력하세요.")

    def __str__(self):
        return self.name

#블로그 글 : 제목, 작성일, 대표이미지, 내용, 분류 등 
class Post(models.Model):
    title = models.CharField(max_length=200)
    title_image = models.ImageField(blank=True)
    context = models.TextField()
    createDate = models.DateTimeField(auto_now_add=True)
    updateDate = models.DateTimeField(auto_now_add=True)
    # 하나의 글을 여러 분류로 해당할 수 있다. 글=카테고리 다대다 관계 ManyToMany
    category = models.ManyToManyField(Category, help_text="글의 분류를 설정하세요.")
    
    def __str__(self):
        return self.title

    # 1번 글의 경우 -> post/1
    def get_absolute_url(self):
        return reverse("post", args=[str(self.id)])

    # 300자 넘는지 확인하는 코드.
    def is_context_more300(self):
        return len(self.context) > 300

    def get_context_under300(self):
        return self.context[:300]

    #update에서 쓰는 함수
    def form_valid(self, form):
        form.save()
        return render(self.requst, 'blog/post_update_form.html', {'message': '일정을 업데이트 했습니다.'})

    def get_self_context(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)
        

