
# Wlan Portal Template

portal template wlan settings

## Structure

`WlanPortalTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_code_alternate_email` | `string` | Optional | “Please provide valid alternate email” |
| `alignment` | `string` | Optional | defines alignment on portal. “left” is default. |
| `auth_button_amazon` | `string` | Optional | label for Amazon auth button |
| `auth_button_azure` | `string` | Optional | label for Azure auth button |
| `auth_button_email` | `string` | Optional | label for Email auth button |
| `auth_button_facebook` | `string` | Optional | label for Facebook auth button |
| `auth_button_google` | `string` | Optional | label for Google auth button |
| `auth_button_microsoft` | `string` | Optional | label for Microsoft auth button |
| `auth_button_passphrase` | `string` | Optional | label for passphrase auth button |
| `auth_button_sms` | `string` | Optional | label for SMS auth button |
| `auth_button_sponsor` | `string` | Optional | label for Sponsor auth button |
| `auth_label` | `string` | Optional | “Connect to WiFi with” |
| `back_link` | `string` | Optional | label of the link to go back to /logon |
| `color` | `string` | Optional | “#1074bc” |
| `color_dark` | `string` | Optional | “#0b5183” |
| `color_light` | `string` | Optional | “#3589c6” |
| `company` | `bool` | Optional | whether company field is required<br>**Default**: `False` |
| `company_error` | `string` | Optional | error message when company not provided |
| `company_label` | `string` | Optional | label of company field |
| `email` | `bool` | Optional | whether email field is required<br>**Default**: `False` |
| `email_access_domain_error` | `string` | Optional | error message when a user has valid social login but doesn’t match specified email domains. |
| `email_cancel` | `string` | Optional | Label for cancel confirmation code submission using email auth |
| `email_code_cancel` | `string` | Optional | - |
| `email_code_error` | `string` | Optional | “Please provide valid alternate email” |
| `email_code_field_label` | `string` | Optional | “Confirmation Code” |
| `email_code_message` | `string` | Optional | “Enter the access number that was sent to your email address.” |
| `email_code_submit` | `string` | Optional | “Sign In |
| `email_code_title` | `string` | Optional | “Access Code” |
| `email_error` | `string` | Optional | error message when email not provided |
| `email_field_label` | `string` | Optional | “Enter your email address” |
| `email_label` | `string` | Optional | label of email field |
| `email_message` | `string` | Optional | “We will email you an authentication code which you can use to connect to the WiFi network.” |
| `email_submit` | `string` | Optional | Label for confirmation code submit button using email auth |
| `email_title` | `string` | Optional | “Sign in with Email” |
| `field_1` | `bool` | Optional | whether to ask field1 |
| `field_1_error` | `string` | Optional | error message when field1 not provided |
| `field_1_label` | `string` | Optional | label of field1 |
| `field_1_required` | `bool` | Optional | whether field1 is required field |
| `field_2` | `bool` | Optional | whether to ask field2 |
| `field_2_error` | `string` | Optional | error message when field2 not provided |
| `field_2_label` | `string` | Optional | label of field2 |
| `field_2_required` | `bool` | Optional | whether field2 is required field |
| `field_3` | `bool` | Optional | whether to ask field3 |
| `field_3_error` | `string` | Optional | error message when field3 not provided |
| `field_3_label` | `string` | Optional | label of field3 |
| `field_3_required` | `bool` | Optional | whether field3 is required field |
| `field_4` | `bool` | Optional | whether to ask field4 |
| `field_4_error` | `string` | Optional | error message when field4 not provided |
| `field_4_label` | `string` | Optional | label of field4 |
| `field_4_required` | `bool` | Optional | whether field4 is required field |
| `message` | `string` | Optional | “Please enjoy the complimentary Wifi” |
| `name` | `bool` | Optional | whether name field is required<br>**Default**: `False` |
| `name_error` | `string` | Optional | error message when name not provided |
| `name_label` | `string` | Optional | label of name field |
| `optout` | `bool` | Optional | whether to display “Do Not Store My Personal Information” |
| `optout_label` | `string` | Optional | label for “Do Not Store My Personal Information” |
| `page_title` | `string` | Required | “Welcome” |
| `passphrase_cancel` | `string` | Optional | “Cancel” |
| `passphrase_error` | `string` | Optional | error message when invalid passphrase is provided |
| `passphrase_label` | `string` | Optional | Passphrase |
| `passphrase_message` | `string` | Optional | “Login using passphrase” |
| `passphrase_submit` | `string` | Optional | “Sign in” |
| `passphrase_title` | `string` | Optional | Title for passphrase details page |
| `powered_by` | `bool` | Optional | whether to show “Powered by Mist”<br>**Default**: `True` |
| `required_field_label` | `string` | Optional | label to denote required field |
| `sign_in_label` | `string` | Optional | label of the button to /signin |
| `sms_carrier_default` | `string` | Optional | “Please Select” |
| `sms_carrier_error` | `string` | Optional | “Please select a mobile carrier” |
| `sms_carrier_field_label` | `string` | Optional | label for mobile carrier drop-down list |
| `sms_code_cancel` | `string` | Optional | Label for cancel confirmation code submission |
| `sms_code_error` | `string` | Optional | error message when confirmation code is invalid |
| `sms_code_field_label` | `string` | Optional | “Confirmation Code” |
| `sms_code_message` | `string` | Optional | “Enter the confirmation code” |
| `sms_code_submit` | `string` | Optional | Label for confirmation code submit button |
| `sms_code_title` | `string` | Optional | “Access Code” |
| `sms_country_field_label` | `string` | Optional | “Country Code” |
| `sms_country_format` | `string` | Optional | “+1” |
| `sms_have_access_code` | `string` | Optional | Label for checkbox to specify that the user has access code |
| `sms_message_format` | `string` | Optional | format of access code sms message. {{code}} and {{duration}} are place holders and should be retained as is. |
| `sms_number_cancel` | `string` | Optional | label for canceling mobile details for SMS auth |
| `sms_number_error` | `string` | Optional | “Invalid Mobile Number” |
| `sms_number_field_label` | `string` | Optional | label for field to provide mobile number |
| `sms_number_format` | `string` | Optional | “2125551212 (digits only)” |
| `sms_number_message` | `string` | Optional | “We will send an access code to your mobile number which you can use to connect to the WiFi network. Message and data rates may apply.” |
| `sms_number_submit` | `string` | Optional | label for submit button for code generation |
| `sms_number_title` | `string` | Optional | Title for phone number details |
| `sms_username_format` | `string` | Optional | “username” |
| `sms_validity_duration` | `int` | Optional | how long confirmation code should be considered valid (in minutes) |
| `sponsor_back_link` | `string` | Optional | “Go back and edit request form” |
| `sponsor_cancel` | `string` | Optional | “Cancel” |
| `sponsor_email` | `string` | Optional | label for Sponsor Email |
| `sponsor_email_error` | `string` | Optional | “Please provide valid sponsor email” |
| `sponsor_email_template` | `string` | Optional | html template to replace/override default sponsor email template<br><br>Sponsor Email Template supports following template variables:<br><br>* `approve_url`: Renders URL to approve the request; optionally &minutes=N query param can be appended to change the Authorization period of the guest, where N is a valid integer denoting number of minutes a guest remains authorized<br>* `deny_url`: Renders URL to reject the request<br>* `guest_email`: Renders Email ID of the guest<br>* `guest_name`: Renders Name of the guest<br>* `field1`: Renders value of the Custom Field 1<br>* `field2`: Renders value of the Custom Field 2<br>* `sponsor_link_validity_duration`: Renders validity time of the request (i.e. Approve/Deny URL)<br>* `auth_expire_minutes`: Renders Wlan-level configured Guest Authorization Expiration time period (in minutes), If not configured then default (1 day in minutes) |
| `sponsor_info_approved` | `string` | Optional | “Your request was approved by” |
| `sponsor_info_denied` | `string` | Optional | “Your request was denied by” |
| `sponsor_info_pending` | `string` | Optional | “Your notification has been sent to” |
| `sponsor_name` | `string` | Optional | label for Sponsor Name |
| `sponsor_name_error` | `string` | Optional | “Please provide sponsor’s name” |
| `sponsor_note_pending` | `string` | Optional | “Please wait for them to acknowledge.” |
| `sponsor_request_access` | `string` | Optional | ‘submit button label request Wifi Access and notify sponsor about guest request |
| `sponsor_select_email` | `string` | Optional | “Select Sponsor” |
| `sponsor_status_approved` | `string` | Optional | text to display if sponsor approves request |
| `sponsor_status_denied` | `string` | Optional | text to display when sponsor denies request |
| `sponsor_status_pending` | `string` | Optional | text to display if request is still pending |
| `sponsor_submit` | `string` | Optional | submit button label to notify sponsor about guest request |
| `sponsors_error` | `string` | Optional | “Please select a sponsor” |
| `sponsors_info_approved` | `string` | Optional | “Your request was approved” |
| `sponsors_info_denied` | `string` | Optional | “Your request was denied” |
| `sponsors_info_pending` | `string` | Optional | “Your notification has been sent to the sponsors” |
| `tos` | `bool` | Optional | **Default**: `True` |
| `tos_accept_label` | `string` | Optional | prefix of the label of the link to go to /tos |
| `tos_error` | `string` | Optional | error message when tos not accepted |
| `tos_link` | `string` | Optional | label of the link to go to /tos |
| `tos_text` | `string` | Optional | text of the Terms of Service |

## Example (as JSON)

```json
{
  "company": false,
  "email": false,
  "name": false,
  "pageTitle": "pageTitle8",
  "poweredBy": true,
  "tos": true,
  "accessCodeAlternateEmail": "accessCodeAlternateEmail6",
  "alignment": "alignment2",
  "authButtonAmazon": "authButtonAmazon2",
  "authButtonAzure": "authButtonAzure6",
  "authButtonEmail": "authButtonEmail4"
}
```

