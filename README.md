# IT job listing(backend)
#### Video Demo:  https://youtu.be/_PsatrMk0rM


### Description:

#### Purpose
The backend of our system is powered by Flask servers. These servers are responsible for web scraping data from job markets in Lithuania, systematically retrieving job advertisements one by one. One of the standout features of this system is its ability to extract information from individual job postings, sending this scraped text to the OpenAI API. In return, the API generates a concise summary that includes the required years of experience for the job and the coding languages necessary for the position.

#### How to use it
When you load the web app in your browser, the first step is to press the top button to fetch job advertisements from the specific job market of your choice. As you scroll down to the bottom of the page, a timer will initiate, counting down to 3 seconds, and then it will automatically load the next job market's listings.

However, if you scroll back up to the point where the button is once again in view, the timer will pause, allowing you more time to review the current job market.

Additionally, you'll notice a "short summary" button located near the job listings in some markets. Clicking this button will extract data from that particular job advertisement and request the AI to create a concise summary of the content in just a few sentences.

#### Stack used
- HTML and SCSS
- React.js and Vite
- Python for backend using Flask
- Open AI API to connect with AI

#### API
OpenAI - [openAI documentation](https://platform.openai.com/)

#### More about files and project structure
- ask_AI.py
Gets text and sends it to openAi to get summary.
prompt used for project - "Find what is needed in add - give ONLY years of experience, coding languages in max 10 words"
Returns JSON.

- commons.py
Here are all the links stored for convenience and faster reach.

- cv_bankas_single_job.py
scrapes a single job add, cleans the gotten text a bit and returns data.

- cv_bankas.py, cv_lt.py, cv_market.py, cv_online.py
Are scraping data from represented websites. Since all websites use different approach for showing data - it was not possible to make one file to handle every website scraping.
Returns JSON.

- is_url_valid.py
Checks if provided text is a link. Returns True or False

- project.py
Main file with all the server endpoints and function calls

- test_project.py
All the tests for different function

- requirements.txt
All the libraries used for this project
