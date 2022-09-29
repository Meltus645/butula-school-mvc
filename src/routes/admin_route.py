from flask import Blueprint 

from src.utils.constants import BASEDIR
from src.controllers.admin_controller import dashboard, users, error_404 
 
admin =Blueprint('admin', __name__, template_folder= BASEDIR /'templates/admin') 

admin.route('/')(dashboard)
admin.route('/<string:type>')(users)
admin.route('/<string:type>/<string:action>')(users)
admin.route('/<string:type>/<string:action>/<string:section>')(users)
# admin.route('/<string:type>/<string:action>/<string:id>')(users)
# admin.route('/<string:type>/<string:action>/<string:id>/<string:section>')(users)
admin.route('/404')(error_404)