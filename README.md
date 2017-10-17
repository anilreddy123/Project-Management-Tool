Clone source code

git clone https://github.com/anilreddy123/Project-Management-Tool.git

cd Project-Management-Tool

Install Libraries

cd Project-Management-Tool

pip install -r requirements.txt

python manage.py runserver

open the localhost url in browser


##### NO need
Deploying to apcera

Deploying first time (configuration from continuum.conf)

$ apc target https://runq-sd-d.qualcomm.com $ apc app create

Update app for subsequent deployments

$ apc target https://runq-sd-d.qualcomm.com $ apc app deploy
