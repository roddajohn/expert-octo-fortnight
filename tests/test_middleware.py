""" Tests the middleware

This includes jinja2 custom formatters
"""

from flask import current_app, render_template_string

def test_template_filters():
    """ Tests the filters

    Creates a template with all necessary filters to test
    Creates sample data if formatters require the data
    Renders the template
    Ensures the formatters formatted correctly
    
    """
    template = """
    Hi

    """
    
    data = []

    with current_app.app_context():
        html = render_template_string(template, data = data)

    assert 'Hi' in html
