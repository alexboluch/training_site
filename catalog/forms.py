# from django import forms
# from django.core.exceptions import ValidationError
# from django.utils.translation import ugettext_lazy as _
# import datetime
# from .models import Post, PostImage
# import ipywidgets as widgets
#
# class AddPostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = '__all__'
#
# class PostImagesForm(forms.Form):
#
#     widget=widgets.FileInput(attrs={'multiple': True}))
#     def __init__(self, *args, **kwargs):
#         if 'request' in kwargs:
#             self.request = kwargs.pop('request')
#         super(PostImagesForm, self).__init__(*args, **kwargs)
#
#     def clean_photos(self):
#         # Остаются только картинки
#         photos = [photo for photo in self.request.FILES.getlist('photos') if 'image' in photo.content_type]
#         # Если среди загруженных файлов картинок нет, то исключение
#         if len(photos) == 0:
#             raise forms.ValidationError(u'Not found uploaded photos.')
#         return photos
#
#     def save_for(self, advert):
#         for photo in self.cleaned_data['photos']:
#             PostImage(photo=photo, advert=advert).save()