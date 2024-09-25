# skyauth 
[![Pylint](https://github.com/HaiNguyenHuynh/demo/actions/workflows/pylint.yml/badge.svg)](https://github.com/HaiNguyenHuynh/demo/actions/workflows/pylint.yml)

Write code to build a simple Python-based web application which can perform the following User Management functionalities:

- User registration, authentication (SSO based)
- Profile management
- Role-based access control
- Administrative interface

## Technical Skills to be Used

- **Language**: Python, HTML/Angular/React/CSS
- **Framework**: Django (Program should follow the Model-View-Template approach) or Flask or any other framework
- **Database**: MySQL or SQLite or MongoDB
- **Authentication**: SAML authentication
- **Logging**
- **Exception handling**

## User Management Access Details

### Roles
- **Admin**
  - Admin can Create, Update, Read, and Delete users.
  - Only Admin can access Create, Update, List, and Delete pages.

- **User**
  - User can register himself.
  - View and update his profile.
  - Cannot access the Create, Update, List, Delete pages for other users.

## Features

- Define your own access features such as:
  - A landing page
  - A sample feature page to explain the access implementation

## Deliverables

- Demonstrate a Python-based web application for User Management, showcasing:
  - Admin capabilities
  - User registration
  - Login and access control between Admin and User
- Walkthrough of the codebase, showing:
  - Code design
  - Coding best practices
  - Code commenting
  - Unit testing
  - Logging
  - Exception handling
- Code should be statically validated, and the deployment process (CI/CD) must be demonstrated using tools like Jenkins.
