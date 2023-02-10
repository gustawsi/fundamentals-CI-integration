# Continuous Integration 
Git repository for Lab 2 Continuous Integration (Fundamentals of Software Engineering DD2480, Royal Institute of Technology 2023) 
 
## Summary 
This repository contains a continuous integration project that can be connected to different github webhooks to perform automatic tests on newly pushed changes. The result is then e-mailed to the person pushing the changes.

## Licence
Permissions: private and commercial use, modification, distribution.
Conditions: license and copyright notice.
Limitations: liability and warranty. 
 
## Operate the program
#### Run server.py with: 
```
python3 src/server.py http
```
#### Start ngrok on the same port (8011) connection:
```
ngrok http 8011
```
(Make sure the webhook in the github repository has the ngrok url)

## Statement of contributions 

### Adam Melander (adrelix / adammel)
Post request handling 

Pulling git repositories

Flake8 linting of repositories

### Anna Kristiansson (anna-sara-maria / annakris) 

Notification

### Adrian Valdani (adde300 / adriankv)
save_results function

### Gustaw Siedlarski (gustawsi)

### Levi Leyh (levi-tating)
test function
