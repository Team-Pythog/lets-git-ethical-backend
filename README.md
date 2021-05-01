# Authors
## Sean Hawkins, Amber Falbo, Alex Angelico, Sam Clark 

# Project 
## Lets Git Ethical 

---
<!-- ### We are deployed on REACT!

[project url here] -->


## **Let’s Git Ethical**

**Summary:** An application that allows you to go through various moral dilemmas. When going through moral dilemmas, you can see how your answers compare with other users. In addition, customize your own profile, and connect with users that have similar ethical standards OR not. Maybe you want a challenge on the date and to discuss your vastly different perspectives.
Pain Point: Have you ever wondered how you might respond in various moral dilemmas? Well now you can go through a set of moral dilemmas and find out what kind of person you really are. You can also see how your ethical standards align with other users, and even include your own dilemmas. If accepted, your unique dilemma can be added to the API! 

**MVP:**
Each moral dilemma will have a corresponding visual. Each moral dilemma will be multiple choice and have follow-up questions to extend the scope of the dilemma. Users will be able to see how their answers match up with others.
In addition, connect with other users to discuss moral dilemmas in a dedicated comment section. Users can submit new moral dilemmas (optional photo) to our own API. We as admins will then decide whether to approve and include it in our application.
Users will have dedicated profiles and can connect with each other and see how much their ethics align. Users can privately message each other and have their own debates. Moreover, users can link their Facebook, Instagram, and LinkedIn accounts to their profiles. Profiles can optionally have a thumbnail photo, header, and bio section.
Potential Stretch Goals:
Generate a page of users that have ethical standards most like your own.
Create the ability for users to add other users to a friends list.
Add the ability for users to use emojis in comments and private messages.
Add an ability for users to have their own walls where they can make various posts.
Add a feed where users can see their friend’s posts.

The web application consists of a frontend written in HTML, CSS,
Bootstrap/Tailwind, and jQuery. The backend was written in Python/

An interface is provided to create new blog
posts, view existing blog posts, edit existing blog posts, delete existing
blog posts, and search by both keywords and usernames.

---

## Tools Used
VS Code
PyCharm

- Python
- Django
- Docker
- MVC
- Bootstrap/Tailwind
- Pytest

---

## Trello Board
```
https://trello.com/b/qeJ8FHxG/lets-git-ethical
```

---
## Recent Updates

#### V 1.0
*TBA* - April " "

---

## Getting Started

Clone this repository to your local machine.

```
$ git clone https://github.com/Team-Pythog/lets-git-ethical.git
```
<!-- Once downloaded, activate your virtual environment and run by ____________
```
cd Team-Pythog/lets-git-ethical
python build
```
The poetry tools will automatically install any dependencies. Before running the application, setup your DB by doing ________
```
Update-Database
```
Once the database has been created, the application can be run. Options for running and debugging the application using can be found via your coding tools of ___________. From the command line, the following will start an instance of the Postgresql server to host the application:
```
cd YourRepo/YourProject
dotnet run
```
Unit testing is included in the __________________ project using the pytest test framework. Tests have been provided for models, view models, controllers, and utility classes for the application.

---

## Usage
***[Provide some images of your app with brief description as title]***

### Overview of Recent Posts
![Overview of Recent Posts](https://via.placeholder.com/500x250)

### Creating a Post
![Post Creation](https://via.placeholder.com/500x250)

### Enriching a Post
![Enriching Post](https://via.placeholder.com/500x250)

### Viewing Post Details
![Details of Post](https://via.placeholder.com/500x250)

---
## Data Flow (Frontend, Backend, REST API)
***[Add a clean and clear explanation of what the data flow is. Walk me through it.]***
![Data Flow Diagram](/assets/img/Flowchart.png)

---
## Data Model

### Overall Project Schema
***[Add a description of your DB schema. Explain the relationships to me.]***
![Database Schema](/assets/img/ERD.png)

---
## Model Properties and Requirements

### Blog

| Parameter | Type | Required |
| --- | --- | --- |
| ID  | int | YES |
| Summary | string | YES |
| Content | string | YES |
| Tags | string(s) | NO |
| Picture | img jpeg/png | NO |
| Sentiment | float | NO |
| Keywords | string(s) | NO |
| Related Posts | links | NO |
| Date | date/time object | YES |


### User

| Parameter | Type | Required |
| --- | --- | --- |
| ID  | int | YES |
| Name/Author | string | YES |
| Posts | list | YES |

---

## Change Log
***[The change log will list any changes made to the code base. This includes any changes from TA/Instructor feedback]***
1.4: *Added OAuth for MySpace* - 23 Jan 2003
1.3: *Changed email handler to Alta Vista, fixed issue with styling on Netscape Navigator browser.* - 21 Dec 1999
1.2: *Fixed bug where pages would not load due to temp data* - 16 Jun 1998
1.1: *Added ability for user to change photos on a post* - 12 May 1998

--- -->
