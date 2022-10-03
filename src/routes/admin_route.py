from flask import Blueprint 

from src.utils.constants.app import BASEDIR
from src.controllers.admin_controller import dashboard, users, error_404, academics, settings, subscribers, support, error_403 
 
admin =Blueprint('admin', __name__, template_folder= BASEDIR /'templates/admin') 

admin.route('/')(dashboard)
admin.route('/manage/<string:position>')(users)
admin.route('/academics')(academics)
admin.route('/academics/<string:section>')(academics)
admin.route('/academics/<string:section>/<string:action>', methods =['GET', 'POST'])(academics)
admin.route('/academics/<string:section>/<string:action>/<string:id>', methods =['GET', 'POST'])(academics)
admin.route('/manage/<string:position>/<string:action>', methods =['GET', 'POST'])(users)
admin.route('/manage/<string:position>/<string:action>/<string:section>')(users)
# admin.route('/manage/<string:position>/<string:action>/<string:id>', methods =['GET', 'POST', 'PUT'])(users)
# admin.route('/manage/<string:position>/<string:action>/<string:id>/<string:section>')(users)
admin.route('/mailing-list')(subscribers)
admin.route('/support')(support)
admin.route('/settings')(settings)
admin.route('/404')(error_404)
admin.route('/403')(error_403)