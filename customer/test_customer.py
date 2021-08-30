from __future__ import unicode_literals

import frappe
from frappe.model.document import Document



class Customer(Document):
    # check before submitting this document
    def validate(self):
        if frappe.db.exists("Booking",{'Customer': self.Customer}):
            frappe.throw("Already booked")
        # exists = frappe.db.exists(
            # "Customer",
            # {
            #     "Customer": self.customer_name,
            #     # check for submitted documents
            #     "docstatus": 1,
            #     # check if the membership's end date is later than this membership's start date
            #     "to_date": (">", self.from_date),
            # },
        # )
        # if exists:
        #     frappe.throw("Already booked")
        # time_list = []
        # if starttime , endtime not in time_list:
        #     print('booked')
        #     time_list.append(starttime, endtime)
        # else:
        #     print('Time slot not available')