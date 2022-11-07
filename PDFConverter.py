#!/bin/python3

from fpdf import FPDF
pdf = FPDF()
list_of_images = ["MyQrCode(mywebsite).png"]


for i in list_of_images:
	pdf.add_page()
	pdf.image(i)


pdf.output("yourfile.pdf","F")
