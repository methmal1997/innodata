import os

import common_function
url_id = None
duplicate_list = None
error_list = None
completed_list = None
ini_path = None
attachment = None
current_date = None
current_time = None
Ref_value = None
out_excel_file = r'C:\Users\SL1184\PycharmProjects\Spec_project\Ref_35\final3'

Email_Sent = "true"
try:
    if str(Email_Sent).lower() == "true":
        attachment_path = out_excel_file
        if os.path.isfile(attachment_path):
            attachment = attachment_path
        else:
            attachment = None
        common_function.attachment_for_email(url_id, duplicate_list, error_list, completed_list,
                                             len(completed_list), ini_path, attachment, current_date,
                                             current_time, Ref_value)
except:
    print("Heeeeee")
    attachment_path = out_excel_file
    if os.path.isfile(attachment_path):
        attachment = attachment_path
    else:
        attachment = None
