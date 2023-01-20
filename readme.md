# Team Tactix

This repository contains a Python-based GraphQL scraper that pulls data from an API and restructures it into JSON files. The data is then visualized on a Flask web server to display match statistics and additional information from various APIs. The tool was developed to help my esports league team scout our opponents, but can be adapted for other use cases as well. 

**NOTE: All possibly senative data or sensative data gathering scripts have been removed.**

![Screenshot of a game that was played](/screenshots/Screenshot%20from%202023-01-19%2023-59-36.png)
![Screenshot of the team's match history and pick history](/screenshots/Screenshot%20from%202023-01-19%2023-58-13.png)

# The Idea

I am a member of my local esports league and I had the goal to scout out, my enemy teams. However, I encountered a problem. The site to do this was very buggy, glitchy, and sometimes did not even show the data I needed. So I proposed a solution to my team, How about I dig through their API and code, then develop my stat viewer tool.

My team was enthusiastic about this and gave me a list of things that they wanted to see. Like KDAs, damage, CSPM (Creep Score per minute), and much more. So I went to work digging through network calls and building this.


# How I built it

The process I used to build this tool was very iterative. I researched how to get the data using browser debugging tools, then I built a basic tool just to query the API. Then I expanded this tool to get more data. Then I developed a tool to read this data. Then I developed a tool to clean this data. The whole process was all done step by step in small chunks so that I could debug, reformat, and improve anything along the way. This allowed me to build the tool in a short amount of time and I never found myself lost in a sea of work to do because each step was bite-sized.

One major step in completing this project was reverse engineering the JS file that PlayVS sends to all clients on request that contains all code for the entire website including react components and the GraphQL structure.


# The Outcome

Our team placed as rank 4 out of 100 which I am personally proud of. This achievement is not in all part due to the program but as my team can attest, this tool helped tremendously. And for me, it was a great learning experience as I had never worked with APIs and reverse engineer problems to itteratively find solutions. This project also let me grow my data skills and flex my python strengths.
