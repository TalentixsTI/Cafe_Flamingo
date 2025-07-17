# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class ProjectInherit(models.Model):
    _inherit = "project.project"
    _description = "Projects"

    sub_project_ids = fields.One2many('sub.project', 'project_id', string="Sub Projects")
    sub_task_count = fields.Integer(compute="compute_sub_task_count")
    privacy_visibility = fields.Selection([
        ('followers', 'Invited employees'),
        ('employees', 'All employees'),
        ('portal', 'Portal users and all employees'),
    ],
        string='Visibility', required=True,
        default='followers',
        help="Defines the visibility of the tasks of the project:\n"
             "- Invited employees: employees may only see the followed project and tasks.\n"
             "- All employees: employees may see all project and tasks.\n"
             "- Portal users and all employees: employees may see everything."
             "   Portal users may see project and tasks followed by.\n"
             "   them or by someone of their company.")

    def compute_sub_task_count(self):
        for rec in self:
            rec.sub_task_count = len(rec.sub_project_ids)

    def unlink(self):
        for remove in self:
            if len(remove.sub_project_ids) > 0:
                raise UserError(_("Sorry !!! You cannot delete this project, because it has sub project(s)"))
        return super(ProjectInherit, self).unlink()


class SubProject(models.Model):
    _name = 'sub.project'
    _description = "Sub Projects"

    user_id = fields.Many2one('res.users', "Project Manager")
    partner_id = fields.Many2one('res.partner', string='Customer')
    project_id = fields.Many2one('project.project', string='Project', store=True)
    p_project_id = fields.Many2one('project.project', string='Project', store=True)

    @api.onchange('p_project_id')
    def set_sub_project_vals(self):
        if self.p_project_id:
            self.user_id = self.p_project_id.user_id
            self.partner_id = self.p_project_id.partner_id

    def unlink(self):
        for remove in self:
            if len(remove.p_project_id.task_ids) > 0:
                raise UserError(_("Sorry !!! You cannot delete this project, because it has Task(s)"))
        return super(SubProject, self).unlink()
