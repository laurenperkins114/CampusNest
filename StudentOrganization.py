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
        print(f"Event '{title}' created for {date}.")

    def rsvp_event(self, event_title, member_name):
        for event in self.events:
            if event['title'] == event_title:
                event['attendees'].append(member_name)
                print(f"{member_name} has RSVP'd for '{event_title}'.")
                return
        print(f"Event '{event_title}' not found.")

    def assign_task(self, task_description, due_date):
        task = {'description': task_description, 'due_date': due_date}
        self.tasks.append(task)
        print(f"Task '{task_description}' assigned with due date {due_date}.")

    def show_events(self):
        print("Upcoming Events:")
        for event in self.events:
            print(f"{event['title']} on {event['date']} (Attendees: {len(event['attendees'])})")

    def show_members(self):
        print("Member Directory:")
        for name, contact in self.members.items():
            print(f"Name: {name}, Contact: {contact}")

# Example Usage
org = StudentOrganization("Tech Club")
org.add_member("Alice", "alice@example.com")
org.add_member("Bob", "bob@example.com")
org.create_event("Hackathon", "2024-11-01")
org.rsvp_event("Hackathon", "Alice")
org.assign_task("Prepare presentation", "2024-10-30")
org.show_events()
org.show_members()

