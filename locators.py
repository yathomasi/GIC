from selenium.webdriver.common.by import By

# Locators
class LoginPageLocators(object):
    USER_NAME = (By.ID, 'login_field')
    PASSWORD = (By.ID, 'password')
    SIGN_IN = (By.LINK_TEXT, 'Sign in')
    COMMIT = (By.NAME, 'commit')


class IssuePageLocators(object):
    ISSUE = (By.LINK_TEXT, 'Add new algorithm, data structure, puzzle, cipher')
    CLOSE_ISSUE = (By.CLASS_NAME, 'js-comment-and-button')
    NEW_ISSUE = (By.LINK_TEXT, 'New issue')
    TITLE = (By.ID, 'issue_title')
    DESCRIPTION = (By.ID, 'issue_body')
    LABELS = (By.CLASS_NAME, 'discussion-sidebar-heading')
    LABELS_LIST = (By.CSS_SELECTOR, '[data-label-name="bug"]')