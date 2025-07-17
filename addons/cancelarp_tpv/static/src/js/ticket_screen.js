/** @odoo-module **/
import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { useAutofocus } from "@web/core/utils/hooks";
import { patch } from "@web/core/utils/patch";
import { Component, useState } from "@odoo/owl";

export class Test extends TicketScreen {
  static template = "Test";
  setup() {
    super.setup();
    console.log("ticket_screen setup initialized!"); // Log para verificar que el setup se ejecuta correctamente
  }
}
