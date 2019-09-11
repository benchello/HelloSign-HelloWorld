from flask import Flask, request, render_template
from hellosign_sdk import HSClient
import hashlib, hmac
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['FLASK_SECRET_KEY']

HS_APP_KEY = os.environ['HS_APP_Key'] or '<HS app key>'
HS_CLIENT_ID = os.environ['HS_CLIENT_ID'] or '<HS client id>'
TEMPLATE_ID = os.environ['TEMPLATE_ID'] or '<HS template id>'

@app.route("/", methods=['GET'])
def index():
	client = HSClient(api_key=HS_APP_KEY)
	embedded_sign = client.send_signature_request_embedded_with_template(
		test_mode=True,
		client_id=HS_CLIENT_ID
		template_id=TEMPLATE_ID,
		subject='<subject>',
		message='<message>',
		signers=[{ 'role_name': '<role>', 
					'email_address': '<email>', 
					'name': '<name>' }],
		)
	embed_id = client.get_embedded_object(embedded_sign.signatures[0].signature_id)
	sign_url = str(embed_id.sign_url)
	return render_template('index.html', client_id=HS_CLIENT_ID, sign_url=sign_url)

@app.route("/callback", methods=['POST']) 
def callback():
	try:
		data = request.form.to_dict()
		results = data['json']
		details = json.loads(results)
		event_time= details['event']['event_time']
		event_type = details['event']['event_type']
		event_hash = details['event']['event_hash']
		h = hmac.new(HS_APP_KEY.encode(), (str(event_time+event_type)).encode(), hashlib.sha256).hexdigest()
		valid = (h == event_hash)
		if valid:
			return "Hello API Event Received"
		else:
			return "Invalid Data received"
	except BaseException as e:
		return "Error"

if __name__ == "__main__":
    app.run()