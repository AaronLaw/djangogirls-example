# djangogirls-example
sample code from Django girls taiwan, http://djangogirls.org/
http://djangogirls.org/taipei/

This example's coding is from http://djangogirlstaipe.gitbooks.io/django-girls-taipei-tutorial/content/

I use virtualenv and virtualenv wrapper to isolate the dev environment.

## Usage
After install virtualenv, activate it by:

`mkdir ~/Envs`
`cd ~/Envs`
`virtualenv env1` # setup virtualenv at /home
`source env1/bin/activate'

or deactivate it by
`deactivate`

To run the test server:
`cd djangogirls`
`python manage.py runserver`

## Deployment
在眾多服務提供者中，我們選擇 [Heroku] (https://www.heroku.com/) 作為這次的範例， 它的免費額度足夠經營一個小型網站，並擁有完善的開發者教學資源。

這一章，我們會根據 官方教學 - ["Getting Started with Django on Heroku"] (https://devcenter.heroku.com/articles/getting-started-with-django) 稍作調整，教你如何準備部署，並在 Heroku 上發佈你的網站。