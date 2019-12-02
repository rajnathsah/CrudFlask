from flask import abort, render_template
from flask_login import login_required, current_user

from . import home

@home.route('/')
def homepage():
    '''
    render the homepage on the / route
    :return:
    '''
    return render_template('home/index.html', title='Welcome')

@home.route('/dashboard')
@login_required
def dashboard():
    '''
    render dashboard
    :return:
    '''
    return render_template('home/dashboard.html', title='Dashboard')

@home.route('/admin/dashboard')
@login_required
def admin_dashboard():
    '''
    render admin dashboard
    :return:
    '''
    if not current_user.is_admin:
        abort(403)

    return render_template('home/admin_dashboard.html', title='Dashboard')