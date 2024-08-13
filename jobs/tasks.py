from celery import shared_task
from .models import Job

@shared_task
def run_scheduled_jobs():
    jobs = Job.objects.all()
    for job in jobs:
        if(job.should_run()):
            if(job.job_type == 'email'):
                print("send emails")
            elif(job.job_type=='number'):
                print('number')

            job.update_next_run()



