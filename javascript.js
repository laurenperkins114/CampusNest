import React, { useState } from 'react';

const CampusNest = () => {
    const [members, setMembers] = useState([]);
    const [events, setEvents] = useState([]);
    const [tasks, setTasks] = useState([]);

    const addMember = (name, contact) => {
        setMembers([...members, { name, contact }]);
    };

    const createEvent = (title, date) => {
        setEvents([...events, { title, date, attendees: [] }]);
    };

    const rsvpEvent = (eventTitle, memberName) => {
        setEvents(events.map(event => 
            event.title === eventTitle 
            ? { ...event, attendees: [...event.attendees, memberName] } 
            : event
        ));
    };

    const assignTask = (description, dueDate) => {
        setTasks([...tasks, { description, dueDate }]);
    };

    return (
        <div>
            {/* Components for managing members, events, and tasks would go here */}
        </div>
    );
};

export default CampusNest;

