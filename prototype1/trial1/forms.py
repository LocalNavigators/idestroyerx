
from django import forms


from .models import FilesInventory

         
class FilesInventoryForm(forms.ModelForm):
    class Meta:
        model = FilesInventory
        fields = ['File1',]         
         
class fileForm(forms.ModelForm):
    class Meta:
        model = FilesInventory
        fields = ['File1',] 
         
#class multipleaudiofileForm(forms.Form):
        #file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))   
        
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

