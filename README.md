# Team name: Alpha_CIC

# Working on the theme Audio Translator ( Mainly for YouTube )

we are trying to solve this problem by dividing it into parts. In the first part, we will extract the captions of a youtube video using the youtube API. 
The second part will be the implementation of converting the captions from one language to another language using google Translate.
The third part will be the implementation of converting the translated captions to audio by using the audiopy python module and last we will try to play the youtube video muted with this translated audio.

Our final demo will be like a YouTube search engine-like interface with an option like converting it from one language to another language and there will be an embedded Youtube player-like video player in which the Youtube  Video will play muted and the translated audio will be played along the youtube video.


## Which tech stack or tools are you using?
Django framework, Python programming language 
 
##How much have you implemented? 
Milestones you have achieved : Successful extracted transcript from one language to another language and built a webpage with YouTube like search engine search bar.

Milestones you plan to achieve in the next 24 hours: working on the audio processing of translated transcript by audiopy and Google-text-to-speech python module.

## Live demo link  
 ```sh
    https://drive.google.com/file/d/17QYhTFfPo73mBV-9xsZcibc3JqwwlJzy/view?usp=share_link
  ```  


## How do you plan to work on the remarks provided in the ideation stage evaluation? 
The work is going on..

## Are you facing any issues?
Yes, Searching stackoverrflow for the code help and some youtube tutorials...


<!-- ABOUT THE PROJECT -->
# In Detail

## 1. Abstract
Website to view any youtube video in any desired language and also to manually record audio for a particular video and store it.

## 2. Built With

### Programming Languages
* Python 3.6

### Main Libraries/Frameworks
* Django

<!-- Setting up the project -->
## 3. Setting up the project

To get a local copy up and running follow these simple steps.

First clone the repository by running the following command in the terminal of your desired directory:

  ```sh
   git clone https://github.com/Abhishek-kumar0503/Test-Team-Alpha.git
   ```

Enter into the project directory by running the following command:

  ```sh
   cd team-alpha
   ```
Then setup the prerequisites to run the programs.

### Prerequisites

Option 2: Setup virtual environment.

* install venv if not installed
  ```sh
  python3 -m pip install --user virtualenv
  ```  

* create new virtual environment
  ```sh
  python3 -m venv team-alpha
  ```  
  
* activate virtual environemt
  ```sh
  source team-alpha/bin/activate
  ```  
 
* run the follwing command to download the dependencies 
  ```sh
  pip install -r requirements.txt
  ```  

## 4. Usage

Run the django website using the below given command

  ```sh
  python manage.py runserver
  ```  

## 5. Output
 ```sh
  Under development, shortly output will be released 
 ```

## 6. Roadmap

<a href="https://github.com/Abhishek-kumar0503/Test-Team-Alpha/issues">Request Feature</a>

![youtube_language_translate_pipeline](https://user-images.githubusercontent.com/43710239/189086179-66cfd5dc-ebd4-448c-929d-323fcea196e3.png)

See the [open issues](https://github.com/Abhishek-kumar0503/Test-Team-Alpha/issues) for a full list of proposed features (and known issues).

## 7. Contributing

1. Setup the local copy of the project as mentioned above
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 8. References
complying them.
