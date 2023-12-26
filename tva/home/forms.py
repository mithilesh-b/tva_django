from django import forms
from .models import Course, Video, StudyMaterial


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['course', 'title', 'youtube_link']

class StudyMaterialForm(forms.ModelForm):
    class Meta:
        model = StudyMaterial
        fields = ['course', 'title', 'file']



