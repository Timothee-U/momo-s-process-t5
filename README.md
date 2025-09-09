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

.                                                                                                                                                 
├── README.md  
├── .env.example  
├── requirements.txt  
├── dashboard.html  
├── frontend/  
│   ├── styles/  
│   │   ├── main.css  
│   │   └── components.css  
│   ├── scripts/  
│   │   ├── analytics.js  
│   │   └── api_handler.js  
│   └── assets/  
├── storage/  
│   ├── input/  
│   │   └── momo_transactions.xml  
│   ├── output/ 
│   │    └── analytics_data.json  
│   ├── momo_database.sqlite3  
│   └── monitoring/  
│       ├── pipeline.log  
│       └── errors/  
├── pipeline/  
│   ├── __init__.py  
│   ├── settings.py  
│   ├── xml_processor.py  
│   ├── data_cleaner.py  
│   ├── transaction_classifier.py  
│   ├── database_manager.py  
│   └── main_runner.py  
├── services/  
│   ├── __init__.py  
│   ├── web_api.py  
│   ├── database_service.py  
│   └── response_models.py  
├── automation/                                                                                                                                         
│   ├── run_pipeline.sh                                                                                                                                              
│   ├── generate_dashboard_data.sh                                                                                                                               
│   └── start_server.sh                                                                                                                                     
└── tests/                                                                                                                                  
    ├── test_xml_processing.py                                                                                                
    ├── test_data_cleaning.py                                                                                                                       
    └── test_classification.py                                                                                                           


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

# Features
## Core Features
- XML Data Processing: Parse and extract transaction data from XML files
- Data Cleaning: Normalize amounts, dates, and phone numbers
- Transaction Categorization: Automatic categorization of transaction types
- SQLite Storage: Efficient local database storage
- Web Dashboard: Interactive analytics and reporting interface
- Logging: Comprehensive ETL process logging and error handling
## Optional Features (Bonus)
- REST API: FastAPI endpoints for programmatic data access
- Real-time Updates: Live dashboard data refresh
- Advanced Analytics: Statistical analysis and trends

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
Database schema design
ETL pipeline development
Frontend dashboard creation
Integration testing
