frappe.ui.form.on("Course", {
    refresh(frm) {
        frappe.show_alert("Welcome to Course!");
        console.log("Course Custom JS Loaded...");
    }
});