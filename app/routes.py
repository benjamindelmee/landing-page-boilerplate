from flask import render_template
from app import app

@app.route('/')
def index():
    kwargs = {
        # mandatory
        'page_title': 'ACME Company | World leader of ABCD',
        'company_name': 'ACME Company',
        'headline': 'The Leading Company',
        # optional
        'lang': 'fr',
        'page_description': 'ACME Company is the world leader in...',
        'call_to_action': 'Try it for free',
        'call_to_action_link': 'https://typeform.com',
        'learn_more': 'Learn more',
        'headline_sub': 'Why choosing someone else?'
    }
    return render_template('index.html', **kwargs)