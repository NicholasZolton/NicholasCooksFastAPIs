# Using Alembic

To create a migration script, run:

`alembic revision --autogenerate -m "MESSAGE HERE"` (make sure to double check the generated script)

then

`alembic upgrade head`

to upgrade the database to the latest revision.
