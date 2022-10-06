from django import forms


class BarangWishlistForm(forms.Form):
    nama_barang = forms.CharField(max_length=50)
    harga_barang = forms.IntegerField()
    deskripsi = forms.CharField(widget=forms.Textarea)
