# Courses API - Backend Application

This repository contains the backend application for managing courses and course instances. It is built using Django and Django REST Framework.

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
  - `POST /api/courses` - Create a new course
  - `GET /api/courses` - List all courses
  - `GET /api/courses/{id}` - View details of a course
  - `DELETE /api/courses/{id}` - Delete a course

- **Course Instances**
  - `POST /api/instances` - Create a new instance of a course delivery
  - `GET /api/instances/{year}/{semester}` - List courses delivered in a specific year and semester
  - `GET /api/instances/{year}/{semester}/{id}` - View details of a specific course instance
  - `DELETE /api/instances/{year}/{semester}/{id}` - Delete a specific course instance

## Setup and Installation

1. **Clone the Repository**

  Crrent repo contains only backEnd application for frontEnd [Please visit here](https://github.com/mahesh-morde/Angular-Courses-Frontend).

   ```bash
   git clone https://github.com/mahesh-morde/Django_Course_API
   cd Django_Course_API
   docker compose up

2. **Kindly visit below url to review working application**
  
  http://localhost:4200/
