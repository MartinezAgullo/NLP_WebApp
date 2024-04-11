
# NLP Sentiment Analysis  

Tool for sentiment analysis based on the Watson NLP Library.
The aim of this tool is to to recognize sentiment or emotion expressed in a text.

  
## Execution
The tool can be executed 

For calling the function from `sentiment_analysis.py`, open the python3.11 shell:

> from sentiment_analysis import sentiment_analyzer
> 
> sentiment_analyzer("I love exploring new technologies")

  

For using the tool as a package, use the python3.11 shell:

> from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
> 
> sentiment_analyzer("I love exploring new technologies")

  

## Unit testing

Unit tests on some test cases are ran with `test_sentiment_analysis.py` to check the validity of the application.

  

## Deploy as web application using Flask
Once the application is ready it is possible to deploy it for usage over a web interface.
The template for the web interface has been obtained from the repository
 [ibm-developer-skills-network/zzrjt-practice-project-emb-ai](https://github.com/ibm-developer-skills-network/zzrjt-practice-project-emb-ai.git).
 It consist on three files:
 - `index.html` in `templates` folder: Code for the web interface
 - `mywebscript.js` in  `static`  folder: Clicking the `Run Sentiment Analysis` button, on the html interface, calls this javascript file which executes a GET request and takes the text provided by the user as input.
 - `server.py`  in the  `practice_project`  folder.
 
## Static testing
Static program analysis is the analysis of computer programs performed without executing them
Use `pylint`:
       python3.11  -m pip install pylint
       pylint server.py


This would provide a score on how much the code agrees with the [PEP8 guidelines](peps.python.org/pep-0008/).


