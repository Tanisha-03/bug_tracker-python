# Ultimate Bug Tracker Project

# Import necessary libraries
import datetime

# Creating a class for our Bug Tracker
class BugTracker:
    def __init__(self):
        self.bugs = []

    def add_bug(self, title, description):
        bug = {
            'id': len(self.bugs) + 1,
            'title': title,
            'description': description,
            'status': 'Open',
            'created_at': datetime.datetime.now()
        }
        self.bugs.append(bug)
        print(f"Bug added with ID: {bug['id']}")

    def list_bugs(self):
        if not self.bugs:
            print('No bugs have been reported.')
            return
        for bug in self.bugs:
            print(f"ID: {bug['id']}, Title: {bug['title']}, Status: {bug['status']}, Created At: {bug['created_at']}")

    def update_bug_status(self, bug_id, status):
        for bug in self.bugs:
            if bug['id'] == bug_id:
                bug['status'] = status
                print(f"Bug with ID: {bug_id} now has Status: {bug['status']}")

# Initializing the Bug Tracker
tracker = BugTracker()

# Adding some bugs
tracker.add_bug('Login Error', 'User unable to login.')
tracker.add_bug('Page Crash', 'Page crashes after clicking the submit button.')

# Listing all bugs
tracker.list_bugs()

# Updating a bug
tracker.update_bug_status(1, 'Closed')

# Listing all bugs after update
tracker.list_bugs()