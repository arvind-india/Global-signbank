from django import forms
from signbank.video.models import Video, GlossVideo

class VideoUploadForm(forms.ModelForm):
    """Form for video upload"""
    
    class Meta:
        model = GlossVideo
        fields = '__all__'

class VideoUploadForGlossForm(forms.Form):
    """Form for video upload for a particular gloss"""
    
    videofile = forms.FileField(label="Upload Video")
    gloss_id = forms.CharField(widget=forms.HiddenInput)
    redirect = forms.CharField(widget=forms.HiddenInput, required=False)
    