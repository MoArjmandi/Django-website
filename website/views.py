from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from .forms import ContactForm
# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'


class AboutView(TemplateView):
    template_name ='about.html'


class ContactView(TemplateView):
    template_name = 'contacts.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'پیام شما با موفقیت ارسال شد! در کمتر از ۲۴ ساعت پاسخ می‌دهیم.')
            return redirect('website:contact')
        else:
            context = self.get_context_data()
            context['form'] = form
            return render(request, self.template_name, context)