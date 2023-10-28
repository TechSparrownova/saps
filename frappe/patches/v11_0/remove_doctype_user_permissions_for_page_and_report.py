# Copyright (c) 2015, Sparrownova Technologies
# License: MIT. See LICENSE

import frappe


def execute():
	frappe.delete_doc_if_exists("DocType", "User Permission for Page and Report")
