# Video Downloader for Youtube


Video Downloader is a Python application that allows users to download videos, playlists, and audio from YouTube. This tool provides a simple command-line interface to download media in various formats directly to your local machine.

<br>

# Installation

Before you begin, ensure you have Python installed on you machine [Python Download Page](https://www.python.org/downloads/)


## Step 1: Install dependencies using a virtual environment

**For arch linux users and derivates**

```bash
pacman -S python3-venv
python -m venv .venv
source .venv/bin/activate
pip install yt-dlp
```


**For debian linux users and derivates**

```bash
sudo apt install python3 python3-venv
python -m venv .venv
source .venv/bin/activate
pip install yt-dlp
```

**For windows users**

Fist you need install the **Python** downloader **[here](https://www.python.org/downloads/)**
During the installation check this:
* "Add Python to PATH"
* Choose _"Customize installation"_ and make sure _"venv"_ is selected

Create a virutal environment
```powershell
py -m venv .venv
.venv\Scripts\activate
pip install yt-dlp
```

> To deactivate the virtual environment for any OS use **"deactivate"**


## Step 2: Clone repository

``` bash
git clone https://github.com/corniergown/YT-VideoDownload.git
cd YT-VideoDownload
```

<br>

# Usage

To run the Video Downloader, navigate to the project directory and run the following command.

`python3 main.py`

### Image

<center>

![Menu](/img/image.png)

</center>

<br>

# Features

* Download Videos: Download Individual videos from youtbe
* Download Playlists: Download entire playlists at once.
* Extract and download only the audio from videos.
* User-Friendly Interface: Simple command-line prompts guide you through the process.

<br>

# Contributing

Contributions to the Video Downloader are welcome! Please fork the repository and submit a pull request with your enhancements.

Ensure to update tests as appropriate.

<br>

# License

This project is licenced under the MIT License - see the [LICENSE.md](https://github.com/corniergown/VideoDownload/blob/main/LICENSE) file for details 
