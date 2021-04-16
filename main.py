from post import post_request as PQ
from jsonify import jasonify_data as Json
import static_data as SD
import actions


def run(nid, dob):
    """
    Combined all actions
    """
    browser = actions.OpenBrowser()
    actions.OpenURL(browser, SD.STATIC_DATA['URL'])
    # actions.DoLogin(browser)
    # actions.GotoNIDVerification(browser)
    actions.DoSearch(browser, nid, dob)
    parsed_data = actions.Parse_Search_Result(browser)
    # js.make_json_file(parsed_data)
    actions.ExitBrowser(browser)
    return Json.read_json_file(parsed_data)
    # print(PQ.post_data(sd.STATIC_DATA['POST_URL'], parsed_data)) # do post reqeust 

