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