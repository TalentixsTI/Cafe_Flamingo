from odoo import models
from odoo.exceptions import UserError

class PosOrder(models.Model):
    _inherit = 'pos.order'

    def unlink(self):
        # Verificar si el usuario pertenece al grupo 'Administrador Punto de Venta'
        if not self.env.user.has_group('point_of_sale.group_pos_manager'):
            # Lanzar un error de usuario con un mensaje claro
            raise UserError("No tienes permisos para eliminar pedidos. Por favor, contacta al administrador.")
        # Si tiene permisos, continuar con la eliminación
        return super(PosOrder, self).unlink()
