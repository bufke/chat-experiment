# chat-experiment
Chat and Django

Just an experiment for now. To run:

1. Use docker compose to start.
2. `docker-compose run --rm web migrate`
3. `docker-compose run --rm web createsuperuser`
4. Log in to /admin to create a profile, organization, and room. 
5. Go to / and start chatting in a room. Everything is api based except new messages are received via websockets.
