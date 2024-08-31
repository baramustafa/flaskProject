from flask import Flask

import account
import booking

app = Flask(__name__)
app.register_blueprint(account.bp_account)
app.register_blueprint(booking.bp_booking)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
