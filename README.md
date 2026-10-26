# ClearPath AI — Your Personal Problem-Solving Assistant

ClearPath AI is a local AI-powered planning assistant designed to help students organize tasks, break down complex problems, and create practical action plans.

It uses Python and Ollama to run the Llama 3.1 language model locally, helping users turn overwhelming tasks into manageable steps.

## Problem Statement

Students often struggle to prioritize assignments, prepare for examinations, and complete projects within limited time. Large tasks can feel overwhelming when there is no clear starting point or structured plan.

## Proposed Solution

ClearPath AI provides a simple, interactive assistant that generates structured plans based on a user's tasks, problems, and available time.

The application focuses on practical next steps, clear explanations, and realistic time management.

## Features

- **Priority Planner:** Organizes multiple tasks and identifies important deadlines.
- **Problem Breaker:** Divides a complex problem into smaller, actionable steps.
- **Time Rescue:** Creates a plan based on the user's available time.
- **Local AI processing:** Uses Ollama with Llama 3.1 to generate responses locally.
- **Interactive menu:** Allows users to select different planning modes in one session.

## Technology Stack

- Python
- Ollama
- Llama 3.1 (8B model)
- Ollama Python library
- Git and GitHub
- Visual Studio Code

## Prerequisites

- Python installed on your computer
- Ollama installed and running
- Git installed
- The Llama 3.1 model downloaded through Ollama

## Installation and Setup

1. Clone this repository or download the project files.
2. Open a terminal in the project directory.
3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the environment.

   On Windows PowerShell:

   ```powershell
   .\venv\Scripts\Activate.ps1
   ```

   If script execution is blocked, use Command Prompt:

   ```bat
   venv\Scripts\activate.bat
   ```

5. Install the Python dependency:

   ```bash
   python -m pip install ollama
   ```

6. Install Ollama from its official website if it is not already installed.
7. Download the model:

   ```bash
   ollama pull llama3.1:8b
   ```

8. Ensure Ollama is running, then start the application:

   ```bash
   python app.py
   ```

## How to Use

1. Start the program using `python app.py`.
2. Select one of the three planning modes from the menu.
3. Enter your tasks, problem, or available time.
4. Read the generated action plan.
5. Select another mode or exit the application.

## Privacy

When using the local Ollama model, prompts are processed by the locally running model rather than being sent to a hosted AI chatbot by this application. Ollama itself must be installed and running on the computer.

## Current Limitations

- AI-generated plans may contain incorrect estimates or recommendations.
- Users should review generated plans and verify important deadlines.
- The current interface runs in the terminal; it does not yet include a graphical interface.
- The application requires sufficient computer resources to run the selected model.

## Future Improvements

- Add a graphical user interface.
- Allow users to save and revisit plans.
- Add task completion tracking.
- Improve time-budget validation.
- Add automated tests for planning features.

## Project Status

Initial working prototype. Features and planning accuracy can be improved through testing and future contributions.

## License

No license has been added yet. A license should be selected before others are granted explicit permission to reuse, modify, or redistribute this project.
