from odoo import models, fields

class SchoolSchedule(models.Model):
    _name = 'school.schedule'
    _description = 'Schedule'

    name = fields.Char(string='Name', required=True)
    start_time = fields.Datetime(string='Start Time', required=True)
    end_time = fields.Datetime(string='End Time', required=True)
    course_id = fields.Many2one('school.course', string='Course', required=True)
    classroom = fields.Char(string='Classroom')