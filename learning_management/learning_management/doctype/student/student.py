# Copyright (c) 2026, mona and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Student(Document):

    def validate(self):
        if self.age and self.age < 5:
            frappe.throw("Student age must be at least 5.")
    def before_insert(self):
        self.status = "Active"
    def before_save(self):
       if self.student_name:
        self.student_name = self.student_name.upper()
    def after_insert(self):
        frappe.msgprint("Student created successfully.")
    def on_update(self):
        frappe.msgprint(f"Updated Student: {self.student_name}")
    def on_change(self):
        frappe.msgprint("Student document has changed.")
    def before_rename(self, old, new, merge=False):
       if not new.startswith("STU-"):
        frappe.throw("Student ID must start with STU-")
    def after_rename(self, old, new, merge=False):
        frappe.msgprint(f"Rename completed successfully.\nOld Name: {old}\nNew Name: {new}")
    def on_trash(self):
       if frappe.db.exists("Enrollment", {"student": self.name}):
        frappe.throw("Cannot delete. Student has enrollments.")
    def after_delete(self):
         frappe.logger("student").error(f"Deleted Student: {self.name}")
  