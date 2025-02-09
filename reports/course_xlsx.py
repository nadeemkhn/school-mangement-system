from odoo import models

class TeacherXlsx(models.AbstractModel):
    _name = 'report.cheeter.course_report_template_id_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, teacher):
        sheet = workbook.add_worksheet('Teacher Data')
        bold = workbook.add_format({'bold': True})
        row = 2
        col = 2
        for obj in teacher:
            row += 1
            sheet.write(row,col,'Teacher',bold)
            sheet.write(row,col+1,obj.name,bold)
