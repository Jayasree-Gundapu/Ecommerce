from django import forms

class CartForm(forms.form):
	quantity = forms.IntegerField(initial = '1')
	product_id = forms.IntegerField()

	def __init__(self,request,*args,**kvargs):
		self.request = request
		super(CartForm,self).__init__(*args,**kvargs)