##Webpage

Repo for my personal webpage at benedikt-haeuser.com

<b>Framework:</b> Django
<b>Deployment:</b> Heroku
<b>Static files:</b> Azure BLOB store, served with Gunicorn and whitenoise
<b>Tracking:</b> Django send information to an Azure Function API which writes tracking information (device, browser, city) to a Azure BLOB table.