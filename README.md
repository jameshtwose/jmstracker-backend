# jmstracker-backend
The backend of a personal tracker (predominantly food intake), using a _fastapi_ API hosted using deta, storing data in the cloud via cockroachdb.

The hosted API can be found here:
https://4qcow4.deta.dev/docs

You can also run the API locally by first installing the python requirements:
`pip install -r requirements.txt`

Then running the API using:
`uvicorn main:app --reload`
