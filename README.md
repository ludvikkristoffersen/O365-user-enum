*for educational purposes only!*

## About
During a webinar hosted by [Kovert](https://www.linkedin.com/events/hvordanvibryterossinnisky-intro7176497881669935104/comments/) on enumeration and password guessing for the cloud, in this case specifically for Azure, I found it specifically interesting to learn that Microsoft has overlooked the aspect of username enumeration completely since they do not consider it necessary. Username enumeration might not be the most important aspect to secure since it would not grant you access right away, but it would definitely speed up the process of gaining access, and with user passwords still being insufficient knowing the existence of user accounts becomes crucial in my opinion! And that's exactly the purpose of this little Python script, to simply automate the process of finding user accounts. Now, there are probably a ton of scripts out there that do this process better than mine, I just created my version to see how it works and decided to share it.
## Installation
First, clone the repository:
```
git clone https://github.com/ludvikkristoffersen/microsoft-user-enum.git
```
Secondly, run the requirements.txt file to install the necessary packages used in this script:
```
pip3 install -r requirements.txt
```
## Usage
