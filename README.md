# SpanDigital_osX
1. First Things First: Checking Python Version
Before you begin, it's crucial to verify which version of Python is installed on your system. The Python version impacts the compatibility with different libraries and frameworks. Here are a few ways to check your Python version:
1.1 Using the Command Line Interface (CLI):
Open your command prompt or terminal and type the following:
bash
python --version
or
bash
python -V
This will display the installed Python version. If Python is not installed, you will see an error message.
1.2 Using the Python Interactive Shell:
Alternatively, you can check the Python version directly in the interactive shell. Open the terminal, type python to enter the Python shell, and then run:
python
import sys
print(sys.version)
This will output the Python version.
1.3 Checking Python Version Programmatically:
If you're writing a Python script and want to check the Python version programmatically, use the sys module. Here's how:
python
import sys
print(sys.version)
Research:
For further details, visit this guide on checking Python versions.
________________________________________
2. Understanding the Prerequisites for Creating a SOLID PyCharm Game
2.1 Key Concepts: SOLID Principles
To build a robust, maintainable game using PyCharm, it's essential to follow the SOLID principles in object-oriented design. SOLID stands for:
•	S: Single Responsibility Principle (SRP)
•	O: Open/Closed Principle (OCP)
•	L: Liskov Substitution Principle (LSP)
•	I: Interface Segregation Principle (ISP)
•	D: Dependency Inversion Principle (DIP)
In a simplified form:
python
if (!finished):
    grabSomeCoffee()
else:
    grabSomeChampagne()
________________________________________
3. Step-by-Step Guide to Developing the Game:
Step 1: Understand the Problem
1.	Review the Rules and Requirements:
o	The objective is to calculate and rank teams based on match results, awarding points for wins, draws, and losses.
2.	Clarify Input/Output Formats:
o	Input: The match results should include teams and their scores (e.g., Team1, Score1, Team2, Score2).
o	Output: The output should be a ranking table, like:
Rank | TeamName  | Points
1     Tarantulas  6 pts
2     Lions       5 pts
3     FC Awesome  1 pt
3     Snakes      1 pt
5     Grouches    0 pts
3.	Ranking Logic:
o	Win = 3 points
o	Draw = 1 point each
o	Loss = 0 points
o	Teams should be sorted by points first (descending) and alphabetically for ties.
________________________________________
Step 2: Break Down the Solution
1.	Input Handling:
o	Task: Read match results from a file or input stream.
o	Classes/Methods:
	MatchResultsReader class for handling file input and parsing.
	parse_match_data(line) method for converting a line of input into match details.
o	SOLID Principles:
	Single Responsibility: MatchResultsReader handles input reading only.
	Open/Closed: The parse_match_data method can be extended for different input formats without modifying the class.


2.	Processing Points:
o	Task: Track and update team points.
o	Classes/Methods:
	TeamPoints class with a dictionary to store and update points.
	update_points(team_name, points) method to update the points for each team.
o	SOLID Principles:
	Single Responsibility: TeamPoints manages points alone.
	Dependency Inversion: Processing logic relies on abstractions for input handling.
3.	Ranking Logic:
o	Task: Sort and rank teams.
o	Classes/Methods:
	Rankings class for sorting and ranking teams.
	calculate_rank() method to assign ranks based on points.
o	SOLID Principles:
	Liskov Substitution: Subclasses can implement additional ranking strategies if needed.
	Interface Segregation: The Rankings class focuses only on ranking.
4.	Output Formatting:
o	Task: Format and display results.
o	Classes/Methods:
	RankingsOutputFormatter class for formatting the output.
	format_and_print() method to display the rankings.
o	SOLID Principles:
	Single Responsibility: RankingsOutputFormatter handles only formatting and printing.
5.	Testing:
o	Task: Ensure correctness via unit tests.
o	Classes/Methods:
	Unit tests should cover:
	Reading input correctly.
	Calculating points.
	Sorting and ranking correctly.
	Formatting the output correctly.
o	SOLID Principles:
	Dependency Inversion: Tests can mock dependencies, such as file reading.
	Open/Closed: Tests can be extended without modifying existing code.
________________________________________
4. OOD Design Implementation
Classes:
•	MatchResultsReader: Handles input reading.
•	TeamPoints: Manages team points.
•	Rankings: Sorts and ranks teams.
•	RankingsOutputFormatter: Formats and prints the results.
Methods:
•	parse_match_data() – Parses match data.
•	update_points() – Updates team points.
•	calculate_rank() – Calculates rankings.
•	format_and_print() – Prints the rankings.
(Note: This design was not implemented as the focus was on lightweight local command-line emulation.)
________________________________________
5. Focus Areas on Testing Output
•	Use PyCharm’s refactoring tools to ensure SOLID principles are followed.
•	Use unit tests and PyCharm’s test runner for continuous feedback.
•	Leverage PyCharm’s linting and code quality tools (e.g., Pylint) to maintain consistency and best practices.
________________________________________
6. Incorporating Visual Elements (PyGame Integration)
To enhance the game and include visual elements like team logos or icons, we need to refactor the program to use PyGame for graphical rendering. This includes displaying rankings alongside team logos.
Folder Structure:
graphql
SpanDigital_osX/
  ├── SpanDigital_osX.py      # Main application logic
  ├── tests.py                # Unit tests for the Python application
  ├── input.txt               # Sample input for testing
  └── assets/                 # Folder containing team logo images
      ├── lions.png
      ├── snakes.png
      ├── tarantulas.png
      ├── fc_awesome.png
      └── grouches.png
  
____________________________________________________________________________________
Install PyGame: 
To install PyGame, run the following command:
pip install pygame
Run the Application: Once installed, you can run the program with:
python main.py input.txt
Refactor the Program to Use PyGame for Displaying Rankings: This version of the Python program integrates PyGame to display the rankings. We use a folder named assets/ where each team has a corresponding logo image (e.g., team_name.png).
If you wish to organize the directory with a solution file like SpanDigital_osX.sln and refactor the code from a "spaghetti" mess into a more stable stack, follow the steps below.
Update pip and Install Dependencies: To ensure everything is up-to-date, first upgrade pip:
python -m pip install --upgrade pip
Research Resources:
•	PEP 8 – Style Guide for Python Code
•	PyPI – The Python Package Index
Install Homebrew (macOS Only): If you're on macOS and need to install Homebrew, use this command:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
Platform-Specific Code: Here’s an example of platform-specific handling in the code. The following script detects if the program is running on macOS and shows a system notification. If it’s running on a different platform, it will print the platform name:





python
import os
import platform
# Check for macOS (OS X)
if platform.system() == "Darwin":
    print("Running on macOS (OSX)...")
    try:
        # Show a macOS-specific notification
        os.system('osascript -e \'display notification "Starting the app on macOS" with title "App Launch"\'')
    except Exception as e:
        print(f"Error sending macOS notification: {e}")
else:
    print(f"Running on {platform.system()}...")
Example Output on Windows: When running the application on Windows, you might see output like this:
bash
PS C:\Users\ADMIN\source\repos\SpanDigital_osX\SpanDigital_osX> python main.py
Running on Windows...
Grabbing some champagne...
Rankings:
1. Tarantulas, 6 pts
2. Lions, 5 pts
3. FC Awesome, 1 pt
3. Snakes, 1 pt
5. Grouches, 0 pts
PS C:\Users\ADMIN\source\repos\SpanDigital_osX\SpanDigital_osX>
____________________________________________________________________________________
What I found challenging:
Expected output:
1.	Tarantulas, 6 pts
2.	Lions, 5 pts
3.	FC Awesome, 1 pt
4.	Snakes, 1 pt
5.	Grouches, 0 pts
I struggled a bit with the display sequence for the 5th item from the .txt input. Iterating over tuples and developing the abstraction wasn’t straightforward, especially without using libraries like NumPy or Pandas. You might expect I'd have chosen those tools automatically, but I pushed myself to test my skills and decided to work with Pygame instead.
____________________________________________________________________________________
requirements.txt:
absl-py==2.1.0
aiohappyeyeballs==2.4.4
aiohttp==3.11.11
aiosignal==1.3.2
annotated-types==0.7.0
anyio==4.8.0
astunparse==1.6.3
async-timeout==5.0.1
attrs==24.3.0
blinker==1.9.0
boto3==1.26.0
botocore==1.29.165
build==1.2.2.post1
cachelib==0.9.0
cachetools==5.5.0
certifi==2024.12.14
cffi==1.17.1
charset-normalizer==2.1.1
chex==0.1.88
click==8.1.8
colorama==0.4.6
cryptography==44.0.0
dill==0.3.6
distro==1.9.0
dnslib==0.9.25
dnspython==2.7.0
ecdsa==0.19.0
etils==1.5.2
exceptiongroup==1.2.2
fastapi==0.115.6
filelock==3.16.1
Flask==3.1.0
Flask-Caching==2.3.0
Flask-Cors==5.0.0
flatbuffers==1.12
flax==0.8.5
frozenlist==1.5.0
fsspec==2024.12.0
gast==0.4.0
google-auth==2.37.0
google-auth-oauthlib==0.4.6
google-pasta==0.2.0
grpcio==1.69.0
gunicorn==23.0.0
h11==0.14.0
h5py==3.12.1
httpcore==1.0.7
httpx==0.28.1
huggingface-hub==0.27.1
humanize==4.11.0
idna==3.10
importlib_metadata==8.5.0
importlib_resources==6.5.2
itsdangerous==2.2.0
jax==0.4.30
jaxlib==0.4.30
Jinja2==3.1.5
jiter==0.8.2
jmespath==1.0.1
keras==2.9.0
Keras-Preprocessing==1.1.2
libclang==18.1.1
localstack==4.0.3
localstack-core==4.0.3
localstack-ext==4.0.3
Markdown==3.7
markdown-it-py==3.0.0
MarkupSafe==3.0.2
marshmallow==3.19.0
mdurl==0.1.2
ml-dtypes==0.4.1
mpmath==1.3.0
msgpack==1.1.0
multidict==6.1.0
namex==0.0.8
nest-asyncio==1.6.0
nested-lookup==0.2.25
networkx==2.8.8
node==1.2.2
ntlm-auth==1.5.0
numpy==2.0.2
oauthlib==3.2.2
odict==1.9.0
openai==0.27.0
opt_einsum==3.4.0
optax==0.2.4
optree==0.13.1
orbax-checkpoint==0.6.4
packaging==24.2
pillow==11.1.0
pinecone-client==5.0.1
pinecone-plugin-inference==3.1.0
pinecone-plugin-interface==0.0.7
pip==24.3.1
plumber==1.7
plux==1.12.1
propcache==0.2.1
protobuf==5.29.3
psutil==6.1.1
pyaes==1.6.1
pyasn1_modules==0.4.1
pyasn1==0.6.1
pycparser==2.22
pydantic_core==2.27.2
pydantic==2.10.5
Pygments==2.18.0
pyotp==2.9.0
pyproject_hooks==1.2.0
pyspnego==0.11.2
python-dateutil==2.9.0.post0
python-dotenv==1.0.1
python-jose==3.3.0
PyYAML==6.0.2
regex==2024.11.6
requests==2.28.1
requests-api==1.1.5
requests-kerberos==0.15.0
requests-ntlm3==6.1.3b1
requests-oauthlib==2.0.0
rich==13.9.4
rsa==4.9
s3transfer==0.6.2
safetensors==0.5.2
scipy==1.13.1
semver==3.0.2
setuptools==58.1.0
six==1.17.0
sniffio==1.3.1
sspilib==0.2.0
starlette==0.41.3
sympy==1.13.1
tabulate==0.9.0
tailer==0.4.1
tensorboard==2.9.0
tensorboard-data-server==0.6.1
tensorboard-plugin-wit==1.8.1
tensorflow_intel==2.18.0
tensorflow==2.18.0
tensorflow-estimator==2.9.0
tensorflow-gpu==2.9.0
tensorflow-io-gcs-filesystem==0.31.0
tensorstore==0.1.69
termcolor==2.5.0
tokenizers==0.21.0
tomli==2.2.1
toolz==1.0.0
torch==1.10.0+cu113
torchaudio==0.10.0+cu113
torchvision==0.11.1+cu113
tqdm==4.67.1
transformers==4.48.0
typing_extensions==4.12.2
urllib3==1.26.20
uvicorn==0.34.0
Werkzeug==3.1.3
wheel==0.45.1
windows-curses==2.4.0
wrapt==1.17.0
yarl==1.18.3
zipp==3.21.0
zope.component==6.0
zope.deferredimport==5.0
zope.deprecation==5.0
zope.event==5.0
zope.hookable==7.0
zope.interface==7.2
zope.lifecycleevent==5.0
zope.proxy==6.1
pygame==2.6.1
astroid==3.3.8
isort==5.13.2
mccabe==0.7.0
mypy==1.14.1
mypy-extensions==1.0.0
platformdirs==4.3.6
pylint==3.3.3
tomlkit==0.13.2
altgraph==0.17.4
macholib==1.16.3
modulegraph==0.19.6
py2app==0.28.8
iniconfig==2.0.0
pluggy==1.5.0
pytest==8.3.4

