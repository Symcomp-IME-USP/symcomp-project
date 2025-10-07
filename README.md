# Symcomp-project

## Local development
For a local deployment of the three services, use:
```
docker compose up --build
```

If you want to develop only the api, run:
```
docker compose up --build backend postgres
```

Or if you want to run the `frontend`, specify it at the end of the command

## Testing
Run the custom, optimized script:
```
./run-tests.sh
```

## Production
Wether you're actually deploying on the machine or just testing the deployment:
```
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d
```
You can remove the `-d` flag to not run on the background only.

Don't forget to fill the `.env` file with appropriate values!