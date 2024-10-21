from flask import Flask, jsonify, request

app = Flask(__name__)

class StudentOrganization:
    def __init__(self, name):
        self.name = name
        self.members = {}
        self.events = []
        self.tasks = []

    def add_member(self, name, contact_info):
        self.members[name] = contact_info

    def create_event(self, title, date):
        event = {'title': title, 'date': date, 'attendees': []}
        self.events.append(event)

    def get_events(self):
        return self.events

org = StudentOrganization("Tech Club")

@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    org.add_member(data['name'], data['contact_info'])
    return jsonify({"message": "Member added!"}), 201

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    org.create_event(data['title'], data['date'])
    return jsonify({"message": "Event created!"}), 201

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify(org.get_events()), 200

@app.route('/')
def index():
    return '''
    <h1>Welcome to CampusNest</h1>
    <p>Use the endpoints to interact with the application.</p>
    <ul>
        <li>POST /members - Add a member</li>
        <li>POST /events - Create an event</li>
        <li>GET /events - List all events</li>
    </ul>
    '''

if __name__ == '__main__':
    app.run(debug=True)
