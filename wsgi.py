"""
Message in a Bottle
Web Server Gateway Interface

This file is the entry point for
mib-users-ms microservice.
"""
# from src import create_app
from src import create_app

# application instance
app = create_app()

if __name__ == '__main__':
    app.run()