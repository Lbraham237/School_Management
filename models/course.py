from odoo import models, fields

class SchoolCourse(models.Model):
    _name = 'school.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    teacher_id = fields.Many2one('res.users', string='Teacher')
    student_ids = fields.Many2many('school.student', string='Students')
    schedule_ids = fields.One2many('school.schedule', 'course_id', string='Schedules')