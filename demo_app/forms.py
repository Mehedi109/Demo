from django import forms
from .models import Usermessage
from .models import teacher_bottom

class UsermessageForm(forms.ModelForm):
	class Meta:
		model=Usermessage
		fields="__all__"

class teacher_bottomForm(forms.ModelForm):
	class Meta:
		model=teacher_bottom
		fields="__all__"
			