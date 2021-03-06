##############################################################################
#
# Copyright (c) 2004-2006 TINY SPRL. (http://tiny.be) and Eddy Boer
#                          All Rights Reserved.
#                    Fabien Pinckaers <fp@tiny.Be>
#                    Eddy Boer <tinyerp@EdbO.xs4all.nl>
#                    Jan Verlaan <informatie@veritos.nl>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################
# I used the code of account_coda as base for this module. The module does
# exactly the same thing as account_coda. The difference is the file-layout. 
#
# This module can import .asc-files (BRI-layout).
# 06-10-2009 jverlaan added MT940 filter for Postbank and ING
#

{
	"name":"Account Bankimport",
	"version":"0.0.2",
	"author":"Tiny / Eddy Boer",
	"category":"Account Bankimport",
	"depends":["base", "account","account_report","base_iban"],
	"init_xml":[],
	"update_xml" : [
		"security/ir.model.access.csv",
		"bankimport_wizard.xml",
		"bankimport_view.xml",
	],
	"active":False,
	"installable":True,
}
