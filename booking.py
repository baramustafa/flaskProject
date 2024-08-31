from flask import Blueprint

bp_booking = Blueprint('booking', __name__)

@bp_booking.route('/booking')
def login():
    return "BP booking"