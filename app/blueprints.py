""" All Flask blueprints are defined here. """

from flask import Blueprint

def _factory(partial_module_string, url_prefix):
    """ Generates blueprint objects for view modules

    partial_module_string: 'auth.login' instead of 'app.views.auth.login'
    url_prefix: url prefix for the blueprint

    Returns:
    Blueprint instance for a view module
    """
    
    import_name = 'app.views.{}'.format(partial_module_string)
    template_folder = 'templates'

    blueprint = Blueprint(partial_module_string, import_name, template_folder = template_folder, url_prefix = url_prefix)

    return blueprint

# The blueprints -- each is instantiated using the _facory() method
auth_mod = _factory('auth.controller', '/auth')
public_mod = _factory('public.controller', '/')

all_blueprints = (auth_mod, public_mod)
""" List of all blueprints (all have been instantiated through _factory()) """
    
