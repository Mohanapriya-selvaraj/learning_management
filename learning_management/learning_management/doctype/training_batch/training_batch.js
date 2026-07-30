// Copyright (c) 2026, mona and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Training Batch", {
// 	refresh(frm) {

// 	},
// });



frappe.ui.form.on("Training Batch", {
    setup(frm) {
        frm.fields_dict.students.get_query = function() {
            return {
                filters: {
                    department: frm.doc.department,
                    status: frm.doc.status
                }
            };
        };
    },

    department(frm) {
        frm.set_value("students", []);
    },

    status(frm) {
        frm.set_value("students", []);
    }
});