import frappe

def send_email_every_minute():
    logger = frappe.logger("learning_management")
    logger.error("Testing error log")