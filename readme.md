# Movies

A small project that serves up movie data. A very small amount of movie data. Very small. The goal of the project is to be able to connect a FastAPI app with a database, then a React frontend with the backend.

## Steps taken to build

I was successfully able to connect a FastAPI with a database and a React frontend with the backend. I was able to complete the backend with little to no ChatGPT help (only used to help form custom responses). When it came to the front end, I was lost. I followed some tutorials to get me up and running, then gave chat gpt my backend and had it create the front end for me. It wasn't easy, chat GPT had it broken and using js instead of tsx and spend a good hour massaging it to get it work. I have no idea how the front end works, but I'm starting to see patterns of what is needed to get the front end to work.

## Installation and Running

Clone the repository and run `pip install -r requirements.txt` in the backend folder.

### Docker Postgres Database Create

Within the backend folder, run `docker-compose up -d`.

### Backend Start

You can access the FastAPI Docs at <http://localhost:8000/docs>.
In terminal run `uvicorn main:app --reload` from the backend folder. Backend should be running on <http://localhost:8000>.
You can access the FastAPI Docs at <http://localhost:8000/docs>.

### Frontend Start

In another terminal run `npm run dev` from the frontend/movie-app folder. Frontend should be runnon on <http://localhost:3000>.

Upon launch of afresh install, or if all movies are deleted and servers are restarted, the database will populate with 3 movies to start from from the given list in the assignment.
