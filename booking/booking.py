# -*- coding: utf-8 -*-
# Copyright (c) 2021, Jagadesh  and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from datetime import datetime
from frappe.model.document import Document

class Booking(Document):
	def before_save(self):
		start_time = datetime.strptime(self.start_time,"%H:%M:%S")
		end_time = datetime.strptime(self.end_time,"%H:%M:%S")
		# a= frappe.db.get_value("Booking",{'booking': self.booking,'start_time':   ["between",self.start_time,self.end_time],'end_time':   ["between",self.start_time,self.end_time]})
		a=frappe.db.sql("""select name from `tabBooking` where date=\'{4}\' and booking=\'{0}\' and ((start_time>=\'{1}\' and start_time<=\'{2}\') or (end_time>=\'{1}\' and end_time<=\'{2}\')) and name!=\'{3}\'""".format(self.booking,self.start_time,self.end_time,self.name,self.date))
		if len(a):
			frappe.throw("Time slot already booked")
		# elif frappe.db.exists("Booking",{'end_time': self.end_time}):
		# 	frappe.msgprint("Time slot already booked")