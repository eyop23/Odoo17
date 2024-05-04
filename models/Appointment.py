from odoo import api, fields, models
class HospitalPatient(models.Model):
    _name = "hospital.appointment" # db table name (hospital_patient)
    _inherit=['mail.thread','mail.activity.mixin']
    _description = "Hospital Appointment"

    patient_id=fields.Many2one('hospital.patient',string="Patient") # for accessing h.p model fileds
    gender=fields.Selection(related="patient_id.gender") #default this field is readonly, but by setting readonly=False you can edit
    appointment_time=fields.Datetime(string="Appointment Time",default=fields.Datetime.now)
    booking_time=fields.Date(string='Booking Date')
    # patient_id=fields.Many2one(string="Patient",comodal='hospital.patient')

