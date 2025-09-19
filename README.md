# Project name
MoMo ETL & Dashboard

# Project Description
A comprehensive ETL (Extract, Transform, Load) pipeline and dashboard system for processing mobile money (MoMo) transaction data from XML files. The system cleanses and normalizes transaction data, stores it in a SQLite database, and provides an interactive web-based analytics dashboard for transaction insights and reporting.

# Team Members
**Timothee Uwayesu** - Repository Manager & Documentation Lead

**Naomi Bamgbose**  - System Architecture Designer (Miro)

**Oladimeji Ayanleke** - Scrum Master & Project Coordinator (Trello)

**Sandrine Dushimimana** - Software developer

# Architecture Diagram
System Architecture: https://miro.com/app/board/uXjVJK7oTwk=/

# Scrum Board
Project Management: https://trello.com/b/h6OMYoBj/momo-s-process-t5

# Project Structure

<img width="834" height="325" alt="image" src="https://github.com/user-attachments/assets/b660d857-3619-47ed-9b56-a0cec57ea5bd" />
<img width="824" height="326" alt="image" src="https://github.com/user-attachments/assets/c1d14836-4771-45f6-8993-d651937a3100" />


# Setup Instructions
## Prerequisites
Python
Git

## Installation
Step 1: Clone the repository
`git clone https://github.com/Timothee-U/momo-trananalytics.git`
`cd momo-trananalytics`

Step 2: Create virtual environment
`python -m venv venv`
`source venv/bin/activate`  # On Windows use: `venv\Scripts\activate`

Step 3: Install dependencies
`pip install -r requirements.txt`

Step 4: Set up environment variables
`cp .env.example .env`

Step 5:  Edit `.env` file with your configurations

# Running the System
## Run ETL Pipeline
`./automation/run_pipeline.sh`

## Or manually: 
`python pipeline/main_runner.py --xml storage/input/momo_transactions.xml`

## Working with dashboard

Step 1: Export Dashboard Data
`./automation/generate_dashboard_data.sh`

Step 2: Start Dashboard
`./automation/start_server.sh`

Step 3: Navigate to http://localhost:8000

**Optional: Start API Server**
`cd services`
`uvicorn web_api:app --reload`
API available at http://localhost:8000

# Database Design
- ERD: commit team-created diagram export under `docs/erd_diagram.png` or `.pdf`
- SQL setup: see `database/database_setup.sql`
- JSON models: schemas in `schemas/`, examples in `examples/` (see `examples/json_schemas.json`)
- JSON mapping notes: `docs/json_modeling.md`

# AI Usage & Attribution
- See `docs/ai_usage_log.md` for permitted AI usage, attributions, and reviewer sign-offs.

# Features
## Core Features  

- **XML Data Processing** – Parses and extracts transaction data directly from XML files for structured handling.  

- **Data Cleaning** – Normalizes amounts, dates, and phone numbers to ensure consistency and accuracy.  

- **Transaction Categorization** – Automatically classifies transaction types (e.g., deposits, withdrawals, transfers).  

- **SQLite Storage** – Stores processed transactions efficiently in a lightweight, local database.  

- **Web Dashboard** – Provides an interactive web interface for analytics, visualization, and reporting.  

- **Logging** – Captures detailed ETL logs and errors to support monitoring and troubleshooting.  


## Optional Features (Bonus)  

- **REST API** – Exposes FastAPI endpoints for seamless programmatic data access.  

- **Real-time Updates** – Enables live refresh of dashboard data without manual reloads.  

- **Advanced Analytics** – Delivers statistical insights, trends, and deeper transaction analysis.  

# Development Workflow

- Task Management: Track progress using Trello board
- Version Control: Use feature branches and pull requests
- Code Review: All changes reviewed before merging to main
- Testing: Run unit tests before committing changes
- Documentation: Update README and code comments

# Technology Stack
Backend: Python 3.8+
Database: SQLite3
Frontend: HTML5, CSS3, JavaScript (ES6+)
XML Processing: lxml/ElementTree
Project Management: Trello
Architecture Design: Miro
Version Control: Git/GitHub

# Team Responsibilities
## Current Sprint Deliverables

GitHub repository setup (Timothee)

System architecture diagram (Naomie)

Scrum board setup (Olademeji)

README.md documentation (Sandrine)

# Next Sprint Planning
- Database schema design
- ETL pipeline development
- Frontend dashboard creation
- Integration testing
