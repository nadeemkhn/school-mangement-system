from odoo import fields, models,api,_


class Student(models.Model):
    _name = 'student.school'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', tracking=True)
    sequence_student = fields.Char(string='Student Sequence', required=True, copy=False, default=lambda self: _('New'))
    class_name = fields.Char(string='Class', tracking=True)
    group = fields.Char(string='Group' , tracking=True)
    age = fields.Integer(string='Age', default=18)
    roll_no = fields.Integer(string='Roll No' , tracking=True)
    course_ids = fields.Many2many('course.course',string='Course')
    state = fields.Selection([
        ('confirm', 'confirmed'),
        ('done', 'Done'),
        ('draft', 'Draft'),
        ('cancel', 'cancelled')


    ],
        default='draft', string='status', tracking=True)

    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ],string='Gender', tracking=True)


    def action_confirm(self):
        self.state = 'confirm'

    def action_done(self):
            self.state = 'done'

    def action_draft(self):
        self.state = 'draft'

    def action_cancel(self):
        self.state = 'cancel'


    @api.model
    def create(self, vals):
        vals['sequence_student'] = self.env['ir.sequence'].next_by_code('student.student') or _("New")
        if 'name' in vals:
            vals['name'] = vals['name'].title()

        return super(Student, self).create(vals)



    def write(self,vals):
        if vals.get('age') and vals['age'] < 18:
            raise ValidationError("Age must be 18 or above.")
        return super(Student,self).write(vals)






