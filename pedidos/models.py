from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Sum, F, FloatField
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
# Create your models here.
from tienda.models import Producto

User=get_user_model()

class Pedido(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    created=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.id

    @property

    def total(self):
        return self.lineapedido_agregate(
            total=Sum(F("precio")*F("cantidad"), outputfield=FloatField())
        )["total"]

    class Meta:
        db_table='pedidos'
        verbose_name='pedido'
        verbose_name_plural='pedidos'
        ordering=['id']


class LineaPedido(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    producto_id=models.ForeignKey(Producto,on_delete=models.CASCADE)
    pedido_id=models.ForeignKey(Pedido,on_delete=models.CASCADE)
    cantidad=models.IntegerField(default=1)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.cantidad} unidades de {self.producto_id.nombre}'


    class Meta:
        db_table='lineapedidos'
        verbose_name='Línea Pedido'
        verbose_name_plural='Línea Pedidos'
        ordering=['id']
