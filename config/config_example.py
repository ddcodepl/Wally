from selenium.webdriver.firefox.options import Options as FirefoxOptions

slack = {
    'enabled': True,
    'bot_token': 'xoxb-222222222222-3333333333333-444444444444444444444444',
    'channel': 'secret-channel',
    'username': 'Wally Bot',
    'description': 'Wally Bot to notify about visual changes on the web',
    'icon_emoji': ':robot_face:'
}

sites = [
    'https://bbc.com',
    'https://nytimes.com',
]

screen_sizes = [
    '320',
    '768',
    '1440',
    '1920',
]

save = {
    'source': True,
    'screenshots': True,
}

browser = {
    'options': FirefoxOptions(),
    'headless': True,
    'extensions': [
        'extensions/idc.xpi',
        'extensions/ublock.xpi',
    ]
}

browser['options'].headless = browser['headless']