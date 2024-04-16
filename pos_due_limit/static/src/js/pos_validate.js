/** @odoo-module */

import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { ErrorPopup } from "@point_of_sale/app/errors/popups/error_popup";
import { _t } from "@web/core/l10n/translation";
import { PartnerDetailsEdit } from "@point_of_sale/app/screens/partner_list/partner_editor/partner_editor";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { Order } from "@point_of_sale/app/store/models";

patch(PaymentScreen.prototype, {
    async validateOrder(isForceValidate) {

        var due_amount = this.currentOrder.get_partner().due_amount
        var due_limit = this.currentOrder.get_partner().due_limit
        var i;.
        var pay =this.paymentLines
        var is_customer_account = false
        for(i in pay){
        if(pay[i].payment_method.name === "Customer Account"){
            is_customer_account=true
        }
        }
        if(due_amount > due_limit && is_customer_account){
            console.log(due_limit)
            console.log('pp',due_amount)
            this.popup.add(ErrorPopup, {
                title: _t("Limit exceeded"),
                body: _t("Your due amount limit exceeded...You cannot validate the order"),
                });
            }
        else{
            await super.validateOrder(...arguments);
        }

},
});

patch(PartnerDetailsEdit.prototype, {
    setup() {
        super.setup(...arguments);
        this.intFields.push("due_limit");
        this.intFields.push("due_amount");
        this.changes.due_limit =
                this.props.partner.due_limit;
        this.changes.due_amount =
                this.props.partner.due_amount;
    }
});

patch(PosStore.prototype,{
    // @Override
    async _processData(loadedData) {
        await super._processData(...arguments);
            this.due_limit = loadedData["due_limit"];
            this.due_amount = loadedData["due_amount"];

            },
});

