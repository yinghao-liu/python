#!/usr/bin/env python3
import xml.dom.minidom
xml_file = "config.xml"
def xml_config_init():
	with xml.dom.minidom.parse(xml_file) as dom:
		sub_list = dom.getElementsByTagName("sub")
		for sub_index in range(sub_list.length):
			sub = sub_list.item(sub_index)

			item_list = sub.childNodes
			print(item_list)
			print(item_list.length)
			for item_index in range(item_list.length):
				item = item_list.item(item_index)	

				print(item.nodeType, ":", item)


if "__main__" == __name__:
	xml_config_init()
