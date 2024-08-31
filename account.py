from flask import Blueprint

bp_account = Blueprint('account', __name__)

@bp_account.route('/account/login')
def login():
    return "BP login"
@bp_account.route('/account/register')
def login():
    return "BP register"