#-*- coding: utf-8 -*-
from django import forms
from uploads.core.models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('author','description', 'document','uploaded_at' )
    
