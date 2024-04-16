/**@odoo-module **/

import { registry } from "@web/core/registry";
import { loadBundle } from "@web/core/assets";
import { useService } from "@web/core/utils/hooks";
import { _t } from "@web/core/l10n/translation";
import { onWillStart } from "@odoo/owl";
import { Component } from  "@odoo/owl";
import { useRef, useEffect } from "@odoo/owl";
import { loadJS } from "@web/core/assets";
const actionRegistry = registry.category("actions");
class EmployeeDashboard extends Component {
   setup() {
        super.setup()
        this.actionService = useService("action");
        this.orm = useService('orm');
        this.canvasRef = useRef('canvas');
        this._fetch_data();
        onWillStart(async () => await loadBundle("web.chartjs_lib"));

        useEffect(() => {
            this.renderChart();
            return () => {
                if (this.chart) {
                    this.chart.destroy();
                }
            };
        });
   }

   renderChart(){
   var self = this;
   this.orm.call("hr.employee", "get_tiles_data", [], {}).then(function(result){
   var config = {
                type: "line",
                data: {
                    labels: result.name,
                    datasets: [{
                        backgroundColor: "DarkBlue",
                        data: result.exp
                    }]
                },
                options: {
                    plugins: {
                       legend: {
                          display: false,

                       }
                    }
                }
                }
    self.chart = new Chart(self.canvasRef.el, config);
    });
   }

   _fetch_data(){
   var self = this;
   this.orm.call("hr.employee", "get_tiles_data", [], {}).then(function(result){
           $('#my_attendance').append('<span>' + result.total_attendance + '</span>');
           $('#my_project').append('<span>' + result.total_project + '</span>');
           $('#my_task').append('<span>' + result.total_task + '</span>');
           $('#my_leave').append('<span>' + result.total_leave + '</span>');
           $('#my_payslip').append('<span>' + result.total_payslip + '</span>');
           $('#my_hierarchy').append('<span>' + result.total_hierarchy + '</span>');

           for(let i = 0; i < result.name.length; i++){
            let name = result.name[i];
            let email = result.email[i];
            let phone = result.phone[i];
            let gender = result.gender[i];
            let cert = result.cert[i];
            let study = result.study[i];
            $('#employee').append('<tr><td>' + name + '</td><td>' + email + '</td><td>' + phone + '</td><td>' + gender +'</td><td>' + cert +'</td><td>' + study +'</td></tr>');
           }
           });
       };

   async _onClickAttendance() {
        const action = await this.actionService.doAction({
            type: "ir.actions.act_window",
                name: _t("Attendances"),
                res_model: "hr.attendance",
                views: [[false, "tree"]],
                view_mode: "tree",
                target: "current",
        });
   }
   async _onClickProject() {
        const action = await this.actionService.doAction({
            type: "ir.actions.act_window",
                name: _t("Projects"),
                res_model: "project.project",
                views: [[false, "tree"]],
                view_mode: "tree",
                target: "current",
        })
   }
   async _onClickTask() {
        const action = await this.actionService.doAction({
            type: "ir.actions.act_window",
                name: _t("Tasks"),
                res_model: "project.task",
                views: [[false, "tree"]],
                view_mode: "tree",
                target: "current",
        })
   }
   async _onClickLeave() {
        const action = await this.actionService.doAction({
            type: "ir.actions.act_window",
                name: _t("Leaves"),
                res_model: "hr.leave",
                views: [[false, "tree"]],
                view_mode: "tree",
                target: "current",
        })
   }
   async _onClickHierarchy() {
        const action = await this.actionService.doAction({
            type: "ir.actions.act_window",
                name: _t("Hierarchy"),
                res_model: "hr.employee",
                views: [[false, "hierarchy"]],
                view_mode: "hierarchy",
                target: "current",
        });
   }
   async _onClickPayslip() {
        const action = await this.actionService.doAction({
            type: "ir.actions.act_window",
                name: _t("Payslips"),
                res_model: "hr.payslip",
                views: [[false, "tree"]],
                view_mode: "tree",
                target: "current",
        })
   }
}
EmployeeDashboard.template = "employee_dashboard.EmployeeDashboard";
actionRegistry.add("employee_dashboard_tag", EmployeeDashboard);