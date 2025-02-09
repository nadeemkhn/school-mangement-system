from odoo import fields,models,api,_


class Course(models.Model):
    _name = 'course.course'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Course')
    student_id = fields.Many2many('student.school')
    sequence_course = fields.Char(string='Course Sequence', copy=True, required=True, default=lambda self: _('New'))
    state = fields.Selection([
        ('confirm', 'confirmed'),
        ('done', 'Done'),
        ('draft', 'Draft'),
        ('cancel', 'cancelled')

    ],
        default='draft', string='status', tracking=True)



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

                val['sequence_course'] = self.env['ir.sequence'].next_by_code('course.course') or _("New")


        return super(Course, self).create(vals)

