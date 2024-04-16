/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { jsonrpc } from "@web/core/network/rpc_service";
import { renderToElement } from "@web/core/utils/render";

publicWidget.registry.demo = publicWidget.Widget.extend({
       selector: '.dynamic_custom_snippet',
       start: function() {
       var self = this
        console.log('Start')

        jsonrpc('/products').then( function (data){
//            console.log(data)
//                data[0].is_active=true
//                data.num = Math.floor(Math.random() * 90000) + 10000;
                console.log('aa',data)
                self.$el.find('#snippet_dynamic').html(renderToElement("custom_snippet.dynamic_snippet_carousel",{data:data}))

        })

    },
});
