all:
	pyinstaller --onefile --clean --add-data templates:templates  app.py