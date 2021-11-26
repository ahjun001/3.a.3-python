#!/usr/bin/env python3
import xlsxwriter

workbook = xlsxwriter.Workbook('img_scaling.xlsx')
worksheet = workbook.add_worksheet()
wrap_format = workbook.add_format({'text_wrap': True})

worksheet.write('A9', 'Some text that wraps', wrap_format)

worksheet.insert_image('B2', 'python.png', {'object_position': 1})
worksheet.insert_image('B8', 'python.png', {'object_position': 1})

workbook.close()
