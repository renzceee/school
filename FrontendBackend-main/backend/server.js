const express = require('express');
const cors = require('cors');
const app = express();
const PORT = 5000;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    res.json({
        message: 'Welcome to the Task Manager API',
        endpoints: {
            'GET /': 'Shows this message',
            'GET /api/tasks': 'Get all tasks',
            'POST /api/tasks': 'Create a new task',
            'DELETE /api/tasks/:id': 'Delete a task by ID'
        }
    });
});

let tasks = [
    { id: 1, title: 'Learn React', completed: false },
    { id: 2, title: 'Learn Node.js', completed: false }
];

app.get('/api/tasks', (req, res) => {
    res.json(tasks);
});

app.post('/api/tasks', (req, res) => {
    const newTask = {
        id: tasks.length + 1,
        title: req.body.title,
        completed: false
    };
    tasks.push(newTask);
    res.status(201).json(newTask);
});

app.delete('/api/tasks/:id', (req, res) => {
    const id = parseInt(req.params.id);
    tasks = tasks.filter(task => task.id !== id);
    res.status(200).json({ message: 'Task deleted successfully' });
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
