/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

publicWidget.registry.sold = publicWidget.Widget.extend({
       selector: '.sold_products_snippet',
       start: function() {
       var self = this
        console.log('Start')

        jsonrpc('/most_sold_products').then( function (data){
//            console.log(data)
                data[0].is_active=true
//                data.num = Math.floor(Math.random() * 90000) + 10000;
                console.log('aa',data)
                self.$el.find('#sold_products').html(renderToElement("sold_viewed_snippet.sold_snippet_carousel",{data:data}))

        })

    },
});
