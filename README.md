# Wally - Automatically detect visual changes in your websites

![](https://i.imgur.com/PWuhElX.png)

Wally script allow us to track visual and content changes in web pages, will prepare screenshots for you and send them over slack if detects any changes.

## Requirements

- Python 3.6+
- Selenium
- NumPy
- OpenCV

To install the requirements, run:

```bash
pip install -r requirements.txt
```

## Important aspects

* Track visual changes in web pages and save screenshots
* Track content changes in web pages
* Support for batch mode
* Uses headless browser in order to render pages
* You can send slack notifications with screenshots when changes are detected

## Configuration

Whole configuration should be provided in `config/config.py` file.
**Note**: This file is required and app will not run without it!

### URLs

Please provide all interesting you urls, which you want to track in `URLS` variable.

It's allowed to use custom parameters so it's perfect solution if you would like to test A/B tests.

### Screen Sizes

Wally always takes full height of the page but allow to set width of the page.

Please provide all interesting you screen widths in `SCREEN_SIZES` variable in the config file.

For all important information please rely on `config/config_example.py` file.


## Running 🚀

## Docker 🐋

The simplest way to run Wally is to use Docker. Only one command is required to run the script:

```bash
docker-compose up
```

### Local Machine 🖥


### Command line example

```bash
python3 main.py https://www.google.com
```

### File example with batch mode

```bash
python3 main.py
```

Please refer to `config/config_example.py` and check `sites` variable to see example of configuration file for urls.

## Supported browsers

By default, we use Firefox, so we support and use plugins for it, but nothing stops you from using Chrome and Chrome plugins, patter will be same.

Default plugins: 
* [uBlock Origin](https://addons.mozilla.org/en-US/firefox/addon/ublock-origin/)
* [I Don't Care About Cookies](https://addons.mozilla.org/en-US/firefox/addon/i-dont-care-about-cookies/)

To add new extension just add `xpi` file to `extensions` directory and add it to `browser.extensions` variable in `config/config.py` file.