# Courses API - Backend Application

This repository contains the backend application for managing courses and course instances. It is built using Django and Django REST Framework. For frontEnd [Please visit here](https://github.com/mahesh-morde/Angular-Courses-Frontend).

## Experience the Live Application

To experience the live application, please visit [this link](https://whimsical-muffin-b51377.netlify.app). (Kindly wait for a minute to load the initial components, It'll may take 2-3 minutes as i'm using free hosting plateforms).


## Features

- **Create a New Course**
- **List All Courses**
- **View Details of a Specific Course**
- **Delete a Course**
- **Create a New Course Instance**
- **List Course Instances for a Specific Year and Semester**
- **View Details of a Specific Course Instance**
- **Delete a Course Instance**

## API Endpoints

- **Courses**
  - `POST /api/courses/` - Create a new course
  - `GET /api/courses/` - List all courses
  - `GET /api/courses/{id}/` - View details of a course
  - `DELETE /api/courses/{id}/` - Delete a course

- **Course Instances**
  - `POST /api/instances/create/` - Create a new instance of a course delivery
  - `GET /api/instances/` - List all course instances
  - `GET /api/instances/{year}/{semester}/` - List courses delivered in a specific year and semester
  - `GET /api/instances/{year}/{semester}/{id}/` - View details of a specific course instance
  - `DELETE /api/instances/{year}/{semester}/{id}/` - Delete a specific course instance

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/mahesh-morde/Django_Course_API
   cd Django_Course_API
   docker compose up

2. **Kindly visit below url to review working application in your local**
  
  http://localhost:4200/
