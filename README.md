# My Robot Framework Project

This is a demo automated testing project using Robot Framework.

## **Project Structure**

- **tests/**: Contains test suites.
- **resources/**: Contains reusable keywords and libraries.

## **Setup Instructions**

1. Install dependencies:

   ```bash
   pip install -r requirements.txt

2. Run convert google sheet to csv
   python -m resources.utils.process_data_file.ggsheet_convert

3. Run tests:
   robot --outputdir results tests

4. Run reports:
   robotmetrics --inputpath ./results/ --output output.xml