Overview:

  The Job Scheduler Microservice is a Django-based application designed to schedule and manage jobs. It provides API endpoints to list, retrieve, and create jobs. Jobs are        scheduled using Celery. This microservice is scalable to handle high traffic and is integrated with Redis for task queuing.

Features:

Job Scheduling: Schedule and manage jobs with flexibility in configuration.

API Endpoints:

  GET /jobs: List all scheduled jobs.

  GET /jobs/{id}: Retrieve details of a specific job.

  POST /jobs: Create new jobs with customizable attributes.
  
Database Integration: Store job details including name, type, schedule, and timestamps.
Scalability: Designed to handle ~10,000 users and ~6,000 API requests per minute.


Getting Started:

  Prerequisites

    Python 3.8+
    Django 4.0+
    Django REST framework 3.14+
    Celery 5.0+
    Celery Beat 5.0+
    Redis



 Installation
 Clone the Repository

    git clone https://github.com/amankumar0199/job-scheduler.git
    cd job-scheduler

 Create a Virtual Environment

    python -m venv env
    source env/bin/activate

  Install Dependencies

    pip install -r requirements.txt
    Set Up Environment Variables

  Run Migrations
  
    python manage.py migrate
    
  Start the Redis Server

  Ensure Redis is running. I've used Docker to start Redis:

    docker run -d --name redis-server -p 6379:6379 redis
    
  Start Celery Worker

  Open a new terminal and start the Celery worker:

      celery -A job_scheduler worker --loglevel=info
      
  Start Celery Beat
  
  Open another terminal and start Celery Beat:

      celery -A job_scheduler beat --loglevel=info

      
  Run the Django Development Server

    python manage.py runserver



Scaling and Performance

  To scale the application:

  Database: Use a scalable database system.

  Celery Workers: Deploy multiple Celery workers.

  Celery Beat: Ensure Celery Beat is appropriately scaled for high traffic.

  Redis: Ensure Redis is scaled appropriately for high traffic.

  Load Balancing: Use load balancers to distribute traffic across multiple instances of the application.
