from pyramid.view import view_config
from apscheduler.schedulers.background import BackgroundScheduler

count = 0

def count_up():
    global count
    if(count >= 10):
        print("Reset.")
        print("")
        count = 0
    else:
        print("")
        print(str(count))
        print("")
        count += 1

@view_config(route_name='home', renderer='aptest:templates/mytemplate.jinja2')
def my_view(request):
    global count
    return {'project': str(count)}

scheduler = BackgroundScheduler()
scheduler.add_job(count_up, 'interval', seconds=5)
scheduler.start()