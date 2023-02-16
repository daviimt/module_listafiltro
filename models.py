from odoo import models, fields

class FiltroProductos(models.Model):
    _name="filtro.productos"
    nombre = fields.Char("Nombre del productos")
    descripcion = fields.Char("Descripción del producto")
    categoria = fields.Selection(selection=[("decoracion","Decoración"),("oficina","Oficina"),("coleccionables","Coleccionables"),("revistas","Revistas"),("libros","Librerias")])
    precioventa = fields.Char("Precio")