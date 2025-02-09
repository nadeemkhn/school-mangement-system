from odoo import fields, models, api, _


class Teacher(models.Model):
    _name = 'teacher.school'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    reference = fields.Char(string='Sequence No', required=True, copy=False, default=lambda self: _('New'))
    student_line_id = fields.One2many('teacher.data.line', 'teacher_id', string='Student')
    profession = fields.Char(string='Profession', tracking=True)
    subject = fields.Char(string='Course', tracking=True)
    state = fields.Selection([
        ('confirm', 'confirmed'),
        ('done', 'Done'),
        ('draft', 'Draft'),

    ], default='draft', string='status', tracking=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', tracking=True)

    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
        self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'

    @api.model_create_multi
    def create(self, vals):
        for val in vals:
            if 'name' in val:
                # val['name'] = val['name'].title()
                # val['subject'] = val['subject'].title()

                val['reference'] = self.env['ir.sequence'].next_by_code('teacher.teacher') or _("New")

        return super(Teacher, self).create(vals)


class DoctorLine(models.Model):
    _name = 'teacher.data.line'

    teacher_id = fields.Many2one('teacher.school', string='Teacher')
    student_id = fields.Many2one('student.school', string='Student')
    class_name = fields.Char(string='Class', tracking=True ,related='student_id.class_name')
    roll_no = fields.Integer(string='Roll No', tracking=True,related='student_id.roll_no' )
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], string='Gender', tracking=True,related='student_id.gender')
