# Overview

This is a cookbook for a python FastAPI with Auth0, Supabase (really Postgresql in general), and Alembic integrated.

It also provides easy integration with Stripe, email claims in Auth0, and much more.

To run it, simply clone the project after creating your environment with devenv (or with poetry).

## Modifying for your Usage

Find and replace `nicholascooks` in the entire project repo folder with the name of your project/package.

Setup your `.env` file as shown in the `example.env` file.

Run the database update command in the `Makefile`.

Run the `dev` command in the `Makefile` to start the local server.

## Lambda Usage

If you want to run the API through lambda, follow these instructions:

First, make sure you enable Mangum in the pyproject file, install it with `poetry install`, and uncomment the Mangum lines in the `nicholascooks/app.py`.

Second, create the Lambda in AWS and set the handler to be `nicholascooks.app.handler`. Feel free to modify the other settings however you want, and do not forget to add your environment variables.
