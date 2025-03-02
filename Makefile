db_update:
	@echo "Enter your alembic upgrade message: "; \
	read ALEMBIC_MESSAGE; \
	alembic revision --autogenerate -m "$$ALEMBIC_MESSAGE"

db_upgrade:
	alembic upgrade head

# packaging ONLY works on linux, requires `zip` as well
lambda_package:
	ifdef os
		echo "Packaging only works on Linux."
	else
		-rm ./dep -r
		-rm lambda_artifact.zip
		pip freeze > requirements.txt
		pip install -t dep -r requirements.txt --platform manylinux2014_x86_64 --only-binary=:all:
		cd dep; zip ../lambda_artifact.zip -r .
		cd ..
		zip ./lambda_artifact.zip -u nicholascooks -r
		zip ./lambda_artifact.zip -u lambda.py
		-rm ./dep -r
		-rm requirements.txt
	endif

# check for windows, if so use .venv/Scripts/activate
ifdef os
dev:
	echo "Windows detected, using .venv/Scripts/activate"
	.venv/Scripts/activate && python dev.py
else
# if linux, use .venv/bin/activate
dev:
	echo "Linux detected, using .venv/bin/activate"
	( \
		. .venv/bin/activate; \
		python3 ./dev.py; \
	)
endif

test:
	.venv/bin/pytest
