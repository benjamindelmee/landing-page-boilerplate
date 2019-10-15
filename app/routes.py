from flask import render_template
from app import app

@app.route('/')
def index():
    kwargs = {
        'meta_lang': 'en',
        'meta_title': 'Product ABCD by ACME',
        'meta_description': '',

        'company_name': 'ACME',
        'btn_calltoaction_text': 'try it for free',
        'btn_calltoaction_link': 'https://typeform.com',
        'btn_learnmore_text': 'Learn more',
        'btn_learnmore_link': '#content',

        'headline': 'Our product name',
        'headline_sub': 'The most advanced product in the world',
        'background_url': 'https://source.unsplash.com/BtbjCFUvBXs/1920x1080',

        'sections': [
            {
                'order': '1',
                'type': 'text',
                'title': 'Our outstanding value proposition',
                'paragraph': 'Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt.'
            },
            {
                'order': '2',
                'type': 'double_cards',
                'left_card_image': 'http://placehold.it/700x400',
                'left_card_image_alt': '',
                'left_card_title': 'advantage one',
                'left_card_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit aliquam aperiam nulla perferendis dolor nobis numquam, rem expedita, aliquid optio, alias illum eaque. Non magni, voluptates quae, necessitatibus unde temporibus.',
                'right_card_image': 'http://placehold.it/700x400',
                'right_card_image_alt': '',
                'right_card_title': 'advantage two',
                'right_card_text': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. Fugit aliquam aperiam nulla perferendis dolor nobis numquam, rem expedita, aliquid optio, alias illum eaque. Non magni, voluptates quae, necessitatibus unde temporibus.'
            },
            # {
            #     'order': '42',
            #     'type': 'text',
            #     ...
            # }
        ]
    }

    return render_template('index.html', **kwargs)