# Multi-Database Library Management API

A robust backend API built with **FastAPI** that demonstrates how to integrate and manage **four different database engines** simultaneously within a single application architecture using **Docker**.

## Tech Stack & Architecture

* **Framework:** FastAPI (Python 3.12)
* **Containerization:** Docker & Docker Compose
* **Relational Databases:**
  * **PostgreSQL:** Handles Member management and user accounts.
  * **MySQL:** Manages Book inventory and catalog details.
  * **Oracle Database (Free):** Handles enterprise-level borrowing records and transactions.
* **NoSQL Database:**
  * **MongoDB:** Stores system logs, audit trails, and reviews.

## Getting Started & Prerequisites

Make sure you have **Docker Desktop** (or Docker Engine) and **Git** installed on your system.

### 1. Clone the Repository
```bash
git clone [https://github.com/ankrah3/library-api.git](https://github.com/ankrah3/library-api.git)
cd library-api
