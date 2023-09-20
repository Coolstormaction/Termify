run: 
	py main.py

build: 
	@read -p 'Enter your commit message: ' commit_message; \
	git add .; \
	git commit -m "$$commit_message"; \
	git push origin master