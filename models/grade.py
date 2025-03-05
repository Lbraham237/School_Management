from odoo import models, fields, api
from odoo.exceptions import ValidationError

class SchoolGrade(models.Model):
    _name = 'school.grade'
    _description = 'Grade'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    grade = fields.Float(string='Grade', required=True)

    @api.constrains('grade')
    def _check_grade(self):
        for record in self:
            if record.grade < 0 or record.grade > 20:
                raise ValidationError("La note doit être comprise entre 0 et 20.")
