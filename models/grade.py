from odoo import models, fields

class SchoolGrade(models.Model):
    _name = 'school.grade'
    _description = 'Grade'

    student_id = fields.Many2one('school.student', string='Student', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    grade = fields.Float(string='Grade', required=True)