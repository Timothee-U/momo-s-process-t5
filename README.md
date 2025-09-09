# momo-s-process-t5

## Project Description
A comprehensive ETL (Extract, Transform, Load) pipeline and dashboard system for processing mobile money (MoMo) transaction data from XML files. The system cleanses and normalizes transaction data, stores it in a SQLite database, and provides an interactive web-based analytics dashboard for transaction insights and reporting.

## Team Members
**Timothee Uwayesu** - Repository Manager & Documentation Lead
**Naomi Bamgbose**  - System Architecture Designer (Miro)
**Oladimeji Ayanleke** - Scrum Master & Project Coordinator (Trello)
**Sandrine Dushimimana** - Software developer

## Architecture Diagram
System Architecture: https://miro.com/app/board/uXjVJKkj0Zg=/?share_link_id=844505314297

## Scrum Board
Project Management: https://trello.com/invite/b/68bf6d4ff57bdd9777616bf6/ATTI7367a1d02e2da2d9696262bdb1d51b1546D3C578/momo-trananalytics-scrum-board

## Project Structure
.
├── README.md                         # Setup, run, overview
├── .env.example                      # DATABASE_URL or path to SQLite
├── requirements.txt                  # lxml/ElementTree, dateutil, (FastAPI optional)
├── dashboard.html                    # Main dashboard entry point
├── frontend/                         # Web interface (renamed from web/)
│   ├── styles/
│   │   ├── main.css                  # Dashboard styling
│   │   └── components.css            # Component-specific styles
│   ├── scripts/
│   │   ├── analytics.js              # Data visualization and charts
│   │   └── api_handler.js            # API communication
│   └── assets/                       # Images, icons, fonts
├── storage/                          # Data management (renamed from data/)
│   ├── input/                        # Raw XML files (was raw/)
│   │   └── momo_transactions.xml
│   ├── output/                       # Processed data (was processed/)
│   │   └── analytics_data.json       # Dashboard data feed
│   ├── momo_database.sqlite3         # Main transaction database
│   └── monitoring/                   # System logs (was logs/)
│       ├── pipeline.log              # ETL process logs
│       └── errors/                   # Failed processing records
├── pipeline/                         # ETL operations (renamed from etl/)
│   ├── __init__.py
│   ├── settings.py                   # Configuration and constants
│   ├── xml_processor.py              # XML parsing and extraction
│   ├── data_cleaner.py               # Data normalization and validation
│   ├── transaction_classifier.py     # Transaction categorization
│   ├── database_manager.py           # SQLite operations and queries
│   └── main_runner.py                # Main ETL orchestration
├── services/                         # API layer (renamed from api/)
│   ├── __init__.py
│   ├── web_api.py                    # FastAPI application
│   ├── database_service.py           # Database connection utilities
│   └── response_models.py            # API response schemas
├── automation/                       # Deployment scripts (renamed from scripts/)
│   ├── run_pipeline.sh               # Execute full ETL process
│   ├── generate_dashboard_data.sh    # Export analytics data
│   └── start_server.sh               # Launch web server
└── quality_assurance/                # Testing suite (renamed from tests/)
    ├── test_xml_processing.py        # XML parsing tests
    ├── test_data_cleaning.py         # Data validation tests
    └── test_classification.py        # Categorization logic tests

## Setup Instructions
# Prerequisites
Python
Git

# Installation
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

# Edit .env file with your configuration

Running the System
Run ETL Pipeline
./automation/run_pipeline.sh
# Or manually: python pipeline/main_runner.py --xml storage/input/momo_transactions.xml
Export Dashboard Data
./automation/generate_dashboard_data.sh
Start Dashboard
./automation/start_server.sh
# Navigate to http://localhost:8000
Optional: Start API Server
cd services
uvicorn web_api:app --reload
# API available at http://localhost:8000
Features
Core Features
XML Data Processing: Parse and extract transaction data from XML files
Data Cleaning: Normalize amounts, dates, and phone numbers
Transaction Categorization: Automatic categorization of transaction types
SQLite Storage: Efficient local database storage
Web Dashboard: Interactive analytics and reporting interface
Logging: Comprehensive ETL process logging and error handling
Optional Features (Bonus)
REST API: FastAPI endpoints for programmatic data access
Real-time Updates: Live dashboard data refresh
Advanced Analytics: Statistical analysis and trends
Development Workflow
Task Management: Track progress using Trello board
Version Control: Use feature branches and pull requests
Code Review: All changes reviewed before merging to main
Testing: Run unit tests before committing changes
Documentation: Update README and code comments
Technology Stack
Backend: Python 3.8+
Database: SQLite3
Frontend: HTML5, CSS3, JavaScript (ES6+)
XML Processing: lxml/ElementTree
Project Management: Trello
Architecture Design: Miro
Version Control: Git/GitHub

## Team Responsibilities
# Current Sprint Deliverables
GitHub repository setup (Timothee)
System architecture diagram (Naomie)
Scrum board setup (Olademeji)
README.md documentation (Sandrine)

# Next Sprint Planning
Database schema design
ETL pipeline development
Frontend dashboard creation
Integration testing
