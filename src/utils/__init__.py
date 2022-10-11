from .filters import  slugify,properties, since, type_of,strip_special, alias


def load_filters(app)->None:
    """
        Loads custom filters into the app

        :param app
        :return None 
    """
    app.jinja_env.filters['properties'] =properties
    app.jinja_env.filters['slugify'] =slugify
    app.jinja_env.filters['since'] =since
    app.jinja_env.filters['type_of'] =type_of
    app.jinja_env.filters['strip_special'] =strip_special
    app.jinja_env.filters['alias'] =alias
      