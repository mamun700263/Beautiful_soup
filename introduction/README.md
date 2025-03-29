1. **Dynamic or static website?**
    Before scraping any website we have to check either the website is static or dynamic . You can read [this](https://medium.com/@mamun700263/how-to-identify-if-a-website-is-dynamic-or-static-b87b0383c1ff) for checking if the website is static or not. if static we can use Beautiful soup.

2. **Start the Virtual environment**
    ```bash 
    python3 -m venv venv
    source venv/bin/activate
    ```
3. **Install required packeges**
    ```bash 
    pip install jupyter bs4 requests
    ```
    - `bs4` for Beautiful soup package.
    - `jupyter` for writing code in small parts
    - `requests` for making requests to target websites
4. **Create file**
    just create a jupyter file `name.ipynb'
    or,
    ```bash
    touch name.ipynb
    ```
    open the file and select the karnel

5. **Import packeges**
    ```python
    from bs4 import BeautifulSoup 
    import requests
    ```
    




