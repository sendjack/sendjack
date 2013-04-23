"""
    survey_monkey
    -------------

    A small set of absolute URLs that link to surveys from SurveyMonkey. To see
    any of these, login to our SurveyMonkey account.

    e.g., "http://www.surveymonkey.com/s/ASDSKDJ"

"""
from .absolute import AbsoluteURL


class SurveyMonkeyURL(AbsoluteURL):

    SURVEY_MONKEY_HOST = unicode("www.surveymonkey.com")
    SURVEY_PATH_BASE = unicode("/s/")

    def __init__(self):
        super(SurveyMonkeyURL, self).__init__(
                self.SURVEY_MONKEY_HOST,
                path=unicode("{}{}").format(self.SURVEY_PATH_BASE, self.ID))


class CustomerFeedbackControlSurvey(SurveyMonkeyURL):

    ID = unicode("DFX55JX")


class CustomerFeedbackTestSurvey(SurveyMonkeyURL):

    ID = unicode("JX2KYXQ")


class RejectedTaskControlSurvey(SurveyMonkeyURL):

    ID = unicode("2XBXBY8")


class RejectedTaskTestSurvey(SurveyMonkeyURL):

    ID = unicode("YZPBF6Z")
