update_database:
	@echo "Enter your alembic upgrade message: "; \
	read ALEMBIC_MESSAGE; \
	alembic revision --autogenerate -m "$$ALEMBIC_MESSAGE"
	alembic upgrade head

lambda_package:
	-rm ./dep -r
	-rm lambda_artifact.zip
	pip install -t dep -r requirements.txt --platform manylinux2014_x86_64 --only-binary=:all:
	cd dep; zip ../lambda_artifact.zip -r .
	cd ..
	zip ./lambda_artifact.zip -u nicholascooks -r
	-rm ./dep -r

dev:
	python3 main.py

