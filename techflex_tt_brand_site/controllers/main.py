# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class TechFlexWebsite(http.Controller):
    """Public website routes for the fresh TechFlex TT brand site."""

    @http.route(['/', '/techflex'], type='http', auth='public', website=True, sitemap=True)
    def techflex_home(self, **kw):
        return request.render('techflex_tt_brand_site.page_home')

    @http.route(['/tech-rentals'], type='http', auth='public', website=True, sitemap=True)
    def techflex_rentals(self, **kw):
        return request.render('techflex_tt_brand_site.page_rentals')

    @http.route(['/about-us'], type='http', auth='public', website=True, sitemap=True)
    def techflex_about(self, **kw):
        return request.render('techflex_tt_brand_site.page_about')

    @http.route(['/team'], type='http', auth='public', website=True, sitemap=True)
    def techflex_team(self, **kw):
        return request.render('techflex_tt_brand_site.page_team')

    @http.route(['/contact-us'], type='http', auth='public', website=True, sitemap=True)
    def techflex_contact(self, **kw):
        return request.render('techflex_tt_brand_site.page_contact')

    @http.route(['/tech-rentals/submit'], type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def submit_rental_request(self, **post):
        name = f"{post.get('first_name', '').strip()} {post.get('last_name', '').strip()}".strip() or post.get('company_name') or 'Rental Request'
        equipment = ', '.join(request.httprequest.form.getlist('equipment'))
        description = "\n".join([
            'TechFlex TT rental request from website.',
            '',
            f"Contact: {name}",
            f"Company: {post.get('company_name', '')}",
            f"Email: {post.get('email', '')}",
            f"Phone: {post.get('phone', '')}",
            f"Business Address: {post.get('business_address', '')}",
            f"Equipment Required: {equipment}",
            f"Specification Level: {post.get('spec_level', '')}",
            f"Units: {post.get('units', '')}",
            f"Rental Start: {post.get('start_date', '')}",
            f"Rental End / Duration: {post.get('end_date', '')}",
            f"Pickup or Delivery: {post.get('fulfillment', '')}",
            '',
            f"Additional Requirements:\n{post.get('message', '')}",
        ])
        request.env['crm.lead'].sudo().create({
            'name': f"Rental Request - {name}",
            'contact_name': name,
            'partner_name': post.get('company_name') or False,
            'email_from': post.get('email') or False,
            'phone': post.get('phone') or False,
            'description': description,
            'type': 'lead',
        })
        return request.render('techflex_tt_brand_site.page_thank_you', {
            'heading': 'Rental request received',
            'message': 'Thank you. The TechFlex TT team will review your request and contact you with rental availability and next steps.',
        })

    @http.route(['/contact-us/submit'], type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def submit_contact_request(self, **post):
        full_name = post.get('name') or 'Website Contact'
        subject = post.get('subject') or 'Website Enquiry'
        request.env['crm.lead'].sudo().create({
            'name': f"Contact Enquiry - {subject}",
            'contact_name': full_name,
            'email_from': post.get('email') or False,
            'phone': post.get('phone') or False,
            'description': post.get('message') or '',
            'type': 'lead',
        })
        return request.render('techflex_tt_brand_site.page_thank_you', {
            'heading': 'Message received',
            'message': 'Thank you. The TechFlex TT team will get back to you as soon as possible.',
        })
