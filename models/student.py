from odoo import models, fields

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'Student'

    name = fields.Char(string='Name', required=True)
    birthdate = fields.Date(string='Birthdate')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')
    course_ids = fields.Many2many('school.course', string='Courses')
    grade_ids = fields.One2many('school.grade', 'student_id', string='Grades')