from post import post_request as pq
from jsonify import jasonify_data as js
import static_data as sd
import actions


def run(nid, dob):
    """
    Combined all actions
    """
    browser = actions.OpenBrowser()
    actions.OpenURL(browser, sd.STATIC_DATA['URL'])
    # actions.DoLogin(browser)
    # actions.GotoNIDVerification(browser)
    # actions.DoSearch(browser, nid_number, dob)
    parsed_data = actions.Parse_Search_Result(browser)
    js.make_json_file(parsed_data)
    actions.ExitBrowser(browser)
    return f"{js.read_json_file()}"
    # js.read_json_file()
    # print(pq.post_data(sd.STATIC_DATA['POST_URL'], parsed_data)) # do post reqeust 

