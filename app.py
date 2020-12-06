from app import app
from app.startTracking import startTracking
from app import sheduler


if __name__== '__main__':
    sheduler.add_job(id="BackgroundProcess",func=startTracking,trigger='interval',seconds=30)
    sheduler.start()
    app.run(debug=True)

