import frappe

def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")


@frappe.whitelist()
def student_summary():

    student = frappe.qb.DocType("Studenttest")
    enrollment = frappe.qb.DocType("TestEnrollment")

    query = (
        frappe.qb
        .from_(student)
        .inner_join(enrollment)
        .on(student.name == enrollment.student)
        .select(
            student.name,
            student.student_name,
            student.department,
            student.status,
            enrollment.course
        )
    )

    results = query.run(as_dict=True)

    doc = frappe.get_doc("Studenttest", results[0]["name"])
    doc.status = "Inactive"
    doc.save()

    for row in results:
        frappe.db.set_value(
            "Studenttest",
            row["name"],
            "status",
            "Active"
        )
    results = query.run(as_dict=True)

  
    return results


def send_sms(receiver_list, msg, success_msg=None, success_url=None):
    print("Receiver:", receiver_list)
    print("Message:", msg)


@frappe.whitelist()
def get_recent_todos():
    timestamp = frappe.utils.now()
    todos=frappe.get_list(
        "ToDo",
        fields=["name","description","owner"],
        order_by="creation desc",
        limit_page_length=5
    )
    for todo in todos:
        email = frappe.db.get_value(
            "User",
            todo.owner,
            "email"
        )
        todo["owner_email"]=email
    return {
    "timestamp": timestamp,
    "records": todos
}