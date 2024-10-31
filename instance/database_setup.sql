DROP TABLE IF EXISTS Events;
DROP TABLE IF EXISTS Tasks;
DROP TABLE IF EXISTS Members;
DROP TABLE IF EXISTS EventMembers;
DROP TABLE IF EXISTS TaskMembers;

CREATE TABLE Events (
    event_id INTEGER PRIMARY KEY AUTOINCREMENT,
    month VARCHAR(255),
    day INT,
    year INT,
    time VARCHAR(255),
    location VARCHAR(255),  -- Added location column
    details TEXT            -- Added details column
);

CREATE TABLE Tasks (
    task_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(255),
    description TEXT,
    dueDate DATE,
    completed BOOLEAN DEFAULT 0,
    rsvp INTEGER DEFAULT 0  -- Keep rsvp as integer
);

CREATE TABLE Members (
    member_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(20)  -- Ensure this column matches your data
);

-- Optional: Create EventMembers junction table
CREATE TABLE EventMembers (
    event_id INT,
    member_id INT,
    PRIMARY KEY (event_id, member_id),
    FOREIGN KEY (event_id) REFERENCES Events(event_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Optional: Create TaskMembers junction table
CREATE TABLE TaskMembers (
    task_id INT,
    member_id INT,
    PRIMARY KEY (task_id, member_id),
    FOREIGN KEY (task_id) REFERENCES Tasks(task_id),
    FOREIGN KEY (member_id) REFERENCES Members(member_id)
);

-- Insert events into Events table
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('August', 5, 2024, '12:00:00', 'Central Park', 'Welcome Back Picnic - Join us for food and fun!');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('August', 12, 2024, '18:00:00', 'Student Lounge', 'Game Night - Bring your favorite board games!');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('August', 18, 2024, '10:00:00', 'Main Hall', 'Career Fair - Network with potential employers.');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('August', 24, 2024, '08:00:00', 'City Park', 'Yoga in the Park - Start your day with some yoga.');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('August', 28, 2024, '19:00:00', 'Quad', 'Movie Under the Stars - Enjoy a classic movie outdoors.');

-- Insert events for September
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('September', 3, 2024, '16:00:00', 'Campus Center', 'Campus Welcome BBQ - Meet fellow students over BBQ!');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('September', 7, 2024, '11:00:00', 'Campus Center', 'Club Recruitment Fair - Sign up for clubs and organizations.');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('September', 14, 2024, '13:00:00', 'Room 201', 'Exam Prep Workshop - Tips for effective studying.');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('September', 21, 2024, '20:00:00', 'Auditorium', 'Outdoor Movie Night - Join us for a fun movie screening!');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('September', 28, 2024, '15:00:00', 'Room 204', 'Resume Building Workshop - Enhance your resume with expert tips.');

-- Insert events for October
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('October', 6, 2024, '17:00:00', 'Library', 'Midterm Study Session - Study together for midterms!');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('October', 15, 2024, '19:00:00', 'Main Hall', 'Halloween Haunted House - Experience our spooky haunted house!');

-- Insert events for November
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('November', 10, 2024, '11:00:00', 'Memorial Plaza', 'Veterans Appreciation Day - Honoring those who served.');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('November', 22, 2024, '17:00:00', 'Dining Hall', 'Thanksgiving Potluck - Bring a dish and share with everyone!');

-- Insert events for December
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('December', 2, 2024, '10:00:00', 'Campus Center', 'Holiday Market - Shop local vendors for gifts.');
INSERT INTO Events (month, day, year, time, location, details) 
VALUES ('December', 16, 2024, '15:00:00', 'Quad', 'Finals Relaxation Day - Free snacks and relaxation activities!');

-- Insert tasks into Tasks table
INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Freshman Orientation', '2024-08-03', 'Welcome to all new students!', FALSE, 1);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Ice Cream Social', '2024-08-10', 'Enjoy ice cream and meet new friends!', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Campus Job Fair', '2024-08-15', 'Meet potential employers.', FALSE, 1);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Welcome Back Picnic', '2024-08-05', 'Join us for food and fun! (Location: Central Park, Time: 12 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Game Night', '2024-08-12', 'Bring your favorite board games! (Location: Student Lounge, Time: 6 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Career Fair', '2024-08-18', 'Network with potential employers. (Location: Main Hall, Time: 10 AM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Yoga in the Park', '2024-08-24', 'Start your day with some yoga. (Location: City Park, Time: 8 AM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Movie Under the Stars', '2024-08-28', 'Enjoy a classic movie outdoors. (Location: Quad, Time: 7 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Campus Welcome BBQ', '2024-09-03', 'Meet fellow students over BBQ! (Location: Campus Center, Time: 4 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Club Recruitment Fair', '2024-09-07', 'Sign up for clubs and organizations. (Location: Campus Center, Time: 11 AM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Exam Prep Workshop', '2024-09-14', 'Tips for effective studying. (Location: Room 201, Time: 1 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Outdoor Movie Night', '2024-09-21', 'Join us for a fun movie screening! (Location: Auditorium, Time: 8 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Resume Building Workshop', '2024-09-28', 'Enhance your resume with expert tips. (Location: Room 204, Time: 3 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Midterm Study Session', '2024-10-06', 'Study together for midterms! (Location: Library, Time: 5 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Halloween Haunted House', '2024-10-15', 'Experience our spooky haunted house! (Location: Main Hall, Time: 7 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Veterans Appreciation Day', '2024-11-10', 'Honoring those who served. (Location: Memorial Plaza, Time: 11 AM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Thanksgiving Potluck', '2024-11-22', 'Bring a dish and share with everyone! (Location: Dining Hall, Time: 5 PM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Holiday Market', '2024-12-02', 'Shop local vendors for gifts. (Location: Campus Center, Time: 10 AM)', FALSE, 0);

INSERT INTO Tasks (title, dueDate, description, completed, rsvp) 
VALUES ('Finals Relaxation Day', '2024-12-16', 'Free snacks and relaxation activities! (Location: Quad, Time: 3 PM)', FALSE, 0);
