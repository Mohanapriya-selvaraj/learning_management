# Copyright (c) 2026, mona and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Feedback(Document):

    def before_submit(self):
        if not self.rating:
            frappe.throw("Please provide a rating before submitting.")

    def before_cancel(self):
        frappe.msgprint("Feedback is about to be cancelled.")

    def on_cancel(self):
        frappe.msgprint("Feedback cancelled successfully.")