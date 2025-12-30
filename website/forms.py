from django import forms

from .models import ContactModel



class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ["subject", "full_name", "email", "phonenumber", "content"]
        labels = {
            'full_name': 'نام و نام خانوادگی',
            'email': 'ایمیل',
            'phonenumber': 'شماره تماس',
            'subject': 'موضوع',
            'content': 'پیام شما',
        }
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-accent/50 bg-white px-4 py-3 text-slate-900 placeholder-slate-400 focus:border-primary focus:ring-2 focus:ring-primary/20 transition',
                'placeholder': 'مثلاً علی رضایی'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'w-full rounded-xl border border-accent/50 bg-white px-4 py-3 text-slate-900 placeholder-slate-400 focus:border-primary focus:ring-2 focus:ring-primary/20 transition',
                'placeholder': 'ali@example.com'
            }),
            'phonenumber': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-accent/50 bg-white px-4 py-3 text-slate-900 placeholder-slate-400 focus:border-primary focus:ring-2 focus:ring-primary/20 transition',
                'placeholder': '۰۹۱۲۳۴۵۶۷۸۹'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'w-full rounded-xl border border-accent/50 bg-white px-4 py-3 text-slate-900 placeholder-slate-400 focus:border-primary focus:ring-2 focus:ring-primary/20 transition',
                'placeholder': 'موضوع پیام خود را وارد کنید'
            }),
            'content': forms.Textarea(attrs={
                'class': 'w-full rounded-xl border border-accent/50 bg-white px-4 py-3 text-slate-900 placeholder-slate-400 focus:border-primary focus:ring-2 focus:ring-primary/20 transition resize-none',
                'placeholder': 'در مورد پروژه یا درخواست خود توضیح دهید...',
                'rows': 5
            }),
        }
        error_messages = {
            'email': {
                'required': "فیلد ایمیل نمی تواند خالی باشد"
            },
            'content': {
                'required': "فیلد محتوا نمی تواند خالی باشد",
                'min_length': "طول محتوای وارد شده غیر مجاز است"
            },
            'subject': {
                'required': "فیلد عنوان نمی تواند خالی باشد"
            },
            'full_name': {
                'required': "فیلد نام و نام خانوادگی نمی تواند خالی باشد"
            }
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add error styling to fields with errors
        for field_name, field in self.fields.items():
            if field_name in self.errors:
                current_class = field.widget.attrs.get('class', '')
                field.widget.attrs['class'] = current_class.replace('border-accent/50', 'border-red-300')
 
    