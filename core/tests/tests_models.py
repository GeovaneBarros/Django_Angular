from django.test import TestCase
from core.models import *
# Create your tests here.
class ProdutoTestCase(TestCase):
    
    def setUp(self):
        Produto.objects.create(
            nome = 'Mouse',
            marca = 'Razer',
            preco = 105.00
        )
    
    def test_str(self):
        produto1 = Produto.objects.get(marca='Razer')
        self.assertEquals(produto1.__str__(), 'Mouse Razer 105.00')