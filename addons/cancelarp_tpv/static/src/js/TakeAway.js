/** @odoo-module **/
import { ProductScreen } from "@point_of_sale/app/screens/product_screen/product_screen";
import { usePos } from "@point_of_sale/app/store/pos_hook";
import { useService } from "@web/core/utils/hooks";
import { useRef } from "@odoo/owl";

export class TakeAwayButton extends ProductScreen {
  static template = "TakeAwayButton";
  setup() {
    super.setup();
    console.log("CustomTicketScreen setup initialized!"); // Log para verificar que el setup se ejecuta correctamente
    this.pos = usePos();
    this.orm = useService("orm");
    this.notification = useService("notification"); // Servicio de notificación
    this.TakeAway = useRef("TakeAway");
  }
  async onClick() {
    const SelectedOrder = this.pos.get_order();
    if (SelectedOrder.is_empty()) {
      // Mostrar notificación si no hay productos en el pedido
      this.notification.add("Please add a product!", {
        type: "danger", // Tipo de notificación: danger, success, info, warning
      });
    } else {
      // Cambiar el estilo del botón al ser presionado
      this.TakeAway.el.className =
        "control-button customer-button btn rounded-0 fw-bolder text-truncate btn-primary";
      SelectedOrder.is_take_away = true;

      try {
        // Llamada al servidor para generar un token (simulación)
        SelectedOrder.token_number = await this.orm.call(
          "pos.order",
          "token_generate",
          [SelectedOrder.uid]
        );

        // Mostrar mensaje de éxito
        this.notification.add(
          `Order placed successfully! Token: ${SelectedOrder.token_number}`,
          {
            type: "success",
          }
        );
      } catch (error) {
        // Mostrar mensaje de error si ocurre un problema
        this.notification.add("Failed to generate token. Please try again.", {
          type: "danger",
        });
      }
    }
  }
}

// Registrar el botón en la pantalla del POS
ProductScreen.addControlButton({
  component: TakeAwayButton,
  condition: function () {
    return true; // Mostrar siempre el botón
  },
});
