from .filters import properties, slugify

def load_filters(app)->None:
    """
        Loads custom filters into the app

        :param app
        :return None 
    """
    app.jinja_env.filters['properties'] =properties
    app.jinja_env.filters['slugify'] =slugify
      