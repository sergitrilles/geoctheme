import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit


class Geoc_ThemePlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fantastic', 'geoc_theme')
		
	

	def before_map(self, m):
		m.connect('contact', '/contact', controller='ckanext.geoc_theme.controller:IrishThemeController', action='contact')
		m.connect('freedomofinformation', '/freedomofinformation', controller='ckanext.geoc_theme.controller:IrishThemeController', action='foi')
		m.connect('publicsectorinformation', '/publicsectorinformation', controller='ckanext.geoc_theme.controller:IrishThemeController', action='psi')
		return m

