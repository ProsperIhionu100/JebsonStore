from django import forms

from  . models  import ShippingAddress

class ShippingForm(forms.ModelForm):
    
    class Meta:
        
        model = ShippingAddress
        
        fields = ['full_name', 'email', 'address1', 'address2', 'city', 'state', 'zipcode', 'phone_no']
        exclude = ['user',]
        
        widgets = {
            
            'full_name': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),
            
            'email': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),
            
            'address1': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),
            
            'address2': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),
            
            'city': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),
            
            'state': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),
            
            'zipcode': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),
            
            'phone_no': forms.TextInput(attrs={'class':'w-full rounded-md border bg-white py-2 px-2 outline-none ring-blue-600 focus:ring-1'}),

        }