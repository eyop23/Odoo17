from datetime import date
from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = "hospital.patient" # db table name (hospital_patient)
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "Hospital Patient"

    #collections inside the tabel
    name=fields.Char(string='Name',tracking=True) #name= fieldname and Name=filedlabel,tracking=>by who customer add pr anyhting add
    date_of_birth = fields.Date(string='Date Of Birth')
    age=fields.Integer(string='Age',compute='_compute_age',tracking=True)
    code=fields.Char(string='Code')
    gender=fields.Selection([('male','Male'),('female','Female')],string='Gender',tracking=True)
    active=fields.Boolean(string='Action',default=True) # reserved key in odoo for archive n unarchive
    @api.depends('date_of_birth') #helps to see real time changes in age field when the dob changes
    def _compute_age(self):
      for rec in self:
        today=date.today()
        if rec.date_of_birth:
            rec.age=today.year-rec.date_of_birth.year
        else:
           rec.age=0
