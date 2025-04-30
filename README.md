# Python Scraper
This repository contains the barebones to setup a Python scraper.

:warning: **If the resource you are scraping requires you to agree to any Terms & Conditions, please do not proceed and notify your contract manager immediately.  Under no circumstances should you create a false account or fake identity.**

## Developing
### Timeline
You may complete this job any time and submit any required files to this repository within one week of accepting the job.

### Project Structure
- `scraper/` - Place all your source code in this directory.
  - `scraper.py` - Main scraper code. You can treat the `run` function as the entrypoint and write your code here.
  - `__main__.py` - Main entrypoint to the scaper. This will be invoked with an output `$filename`. You should not modify this.
- `requirement.txt` - List of package requirements for your code to run. You can modify these to your needs.
- `data/` - Contains all data output from the scraper.
  - `sample.csv` - A sample output from your scraper.
  - `history/` - All manually generated historical files.

### Environment
Install the necessary requirements into your Python environment. The command below will install the necessary `idr-requirements.txt` as well as your custom requirements.
```bash
$ pip install -r requirements.txt
```

__Note__: Make sure you re-run this when you add a new requirement to the `requirements.txt` file.

## Running
To run your code, you must invoke the scraper module with a filename argument. This can be done using the `-m` option with Python interpreter.
```bash
$ python -m scraper data/sample.csv
```

## Testing
Any commits to the main branch will automatically trigger a GitHub Actions workflow. This will build and test your code in a containerized environment. The tests must pass for your code to be accepted.

## Runtime
During the build process, the contents of this repository will be copied to `/usr/src/scrape`. Your code must be able to run from this path.
