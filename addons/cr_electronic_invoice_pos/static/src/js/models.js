/** @odoo-module */
import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {
  get_sequence: function () {
    return this.sequence;
  },
  get_tipo_documento: function () {
    return this.tipo_documento;
  },
  get_number_electronic: function () {
    return this.number_electronic;
  },

  export_for_printing() {
    const result = super.export_for_printing(...arguments);
    if (this.get_partner()) {
      result.headerData.partner = this.get_partner();
    }

    // Agregar sequence y number_electronic
    var sequence = this.get_sequence();
    var number_electronic = this.get_number_electronic();
    var tipo_documento = this.get_tipo_documento();

    if (sequence) {
      result.headerData.sequence = sequence;
    }
    if (number_electronic) {
      result.headerData.number_electronic = number_electronic;
    }

    if (tipo_documento) {
      result.headerData.tipo_documento = tipo_documento;
    }

    return result;
  },
});
