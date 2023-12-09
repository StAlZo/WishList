from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import WishList, Goods


class AddWishList(forms.ModelForm):
    class Meta:
        model = WishList
        fields = ["title"]


class AddGoods(forms.ModelForm):
    class Meta:
        model = Goods
        fields = ["title", "link"]


class CreateWishList(forms.Form):
    title = forms.CharField(max_length=255)
    goods_name = forms.CharField(max_length=255)
    link = forms.CharField(max_length=255)



