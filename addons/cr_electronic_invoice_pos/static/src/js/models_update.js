import { PosOrder } from "@point_of_sale/app/models/pos_order";
import { patch } from "@web/core/utils/patch";

patch(PosOrder.prototype, {
    setup() {
        super.setup(...arguments);
    },

    export_for_printing(baseUrl, headerData) {
        const result = super.export_for_printing(...arguments);

        result.headerData.number_electronic = this.number_electronic || '';
        result.headerData.account_move_name = this.account_move_name || '';
        result.qr_image = this.qr_image || '';

        console.log('number_electronic', result.headerData);
        console.log('result', result);

        return result;
    },
});