# phone_api
API that processes 46elk callbacks and retrieves user requests from there

## Usage

The main app should be run in the server that will receive the calls from 46elks service:

```bash
  python3 app.py https://phone.thedigitalvolunteer.se API_USERNAME API_PASSWORD
```

The API_USERNAME and API_PASSWORD are secret values that are provided by the 46elk account. They are needed to be able to retrieve the user's recording.

The URL provided parameter should reference this same server, as it will be used to create the callback links that will be used to provide the recording.

The 46elks account configuration should point to this service, using the `/incomingCalls` path, for example:

```bash
  https://phone.thedigitalvolunteer.se/incomingCalls
```

## Local development

Run using ngrok as described in the official 46elks tutorials below.

For more information:
- https://46elks.com/docs/receive-call
- https://46elks.com/docs/voice-record
- https://46elks.com/tutorials/ivr-flask
- https://46elks.com/tutorials/record-call
