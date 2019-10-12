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
        'call_to_action': 'try it for free',
        'call_to_action_link': 'https://typeform.com',
        'learn_more': 'Learn more',
        'headline_sub': 'Why choosing someone else?',
        'intro_title': 'Our outstanding value proposition',
        'intro_text': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.',
        'advantage_one_image': 'http://placehold.it/700x400',
        'advantage_one_image_alt': '',
        'advantage_one_title': 'advantage one',
        'advantage_one_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit aliquam aperiam nulla perferendis dolor nobis numquam, rem expedita, aliquid optio, alias illum eaque. Non magni, voluptates quae, necessitatibus unde temporibus.',
        'advantage_two_image': 'http://placehold.it/700x400',
        'advantage_two_image_alt': '',
        'advantage_two_title': 'advantage two',
        'advantage_two_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit aliquam aperiam nulla perferendis dolor nobis numquam, rem expedita, aliquid optio, alias illum eaque. Non magni, voluptates quae, necessitatibus unde temporibus.',
    }
    return render_template('index.html', **kwargs)