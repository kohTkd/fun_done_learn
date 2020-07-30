# Fun Done Learn

This is a web application for `Fun Done Learn`.
`Fun Done Learn` is a retrospective activity designed by Team Almost Done in Scrum Coaches Retreat in Okinawa.

## Requirement

- Docker

## Install

```
git clone https://github.com/kohTkd/fun_done_learn.git
```

## Set up

```
docker-compose up -d
docker-compose exec back pipenv run python bin/migrate.py
```

Then, visit http://localhost:8080/ .

## Unimplemented features

- Enable to deploy AWS
- Sync by websocket
- User authentication and manage sessions
- Edit / Delete session notes
- Edit session title
- Add comments to each activities
