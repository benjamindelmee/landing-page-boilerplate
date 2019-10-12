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
        'headline_sub': 'Why choosing someone else?',
        'intro_title': 'Our outstanding value proposition',
        'intro_text': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.'
    }
    return render_template('index.html', **kwargs)