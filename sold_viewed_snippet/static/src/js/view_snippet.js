/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

publicWidget.registry.viewed = publicWidget.Widget.extend({
       selector: '.viewed_products_snippet',
       start: function() {
       var self = this
        console.log('Start')

        jsonrpc('/most_viewed_products').then( function (data){
            console.log(data)
                data[0].is_active=true
//                data[0].n = Math.floor(Math.random() * 90000) + 10000;
                self.$el.find('#view_products').html(renderToElement("sold_viewed_snippet.view_snippet_carousel",{data:data}))

        })

    },
});
