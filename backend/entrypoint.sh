#!/bin/sh
# Initialize database and create superadmin
python -m app.init_db
# Start the server
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
