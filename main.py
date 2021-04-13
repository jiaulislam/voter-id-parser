
from jsonify import jasonify_data as js
import static_data as sd
import actions


def main():
    """
    Combined all actions
    """
    nid_number, dob = actions.take_arguments()
    browser = actions.OpenBrowser()
    actions.OpenURL(browser, sd.STATIC_DATA['URL'])
    actions.DoLogin(browser)
    actions.GotoNIDVerification(browser)
    actions.DoSearch(browser, nid_number, dob)
    parsed_data = actions.Parse_Search_Result(browser)
    js.make_json_file(parsed_data)
    js.read_json_file()
    actions.ExitBrowser(browser)
    print("Json File Exported Successfully")


if __name__=="__main__":
    main()
