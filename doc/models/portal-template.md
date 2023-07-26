
# Portal Template

Portal Template

## Structure

`PortalTemplate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `access_code_alternate_email` | `string` | Optional | **Default**: `'Please provide valid alternate email'` |
| `alignment` | `string` | Optional | defines alignment on portal. “left” is default. |
| `auth_button_amazon` | `string` | Optional | label for Amazon auth button<br>**Default**: `'Sign in with Amazon'` |
| `auth_button_azure` | `string` | Optional | label for Azure auth button<br>**Default**: `'Sign in with Azure'` |
| `auth_button_email` | `string` | Optional | label for Email auth button<br>**Default**: `'Sign in with Email'` |
| `auth_button_facebook` | `string` | Optional | label for Facebook auth button<br>**Default**: `'Sign in with Facebook'` |
| `auth_button_google` | `string` | Optional | label for Google auth button<br>**Default**: `'Sign in with Google'` |
| `auth_button_microsoft` | `string` | Optional | label for Microsoft auth button<br>**Default**: `'Sign in with Microsoft'` |
| `auth_button_passphrase` | `string` | Optional | label for passphrase auth button |
| `auth_button_sms` | `string` | Optional | label for SMS auth button<br>**Default**: `'Sign in with Text Message'` |
| `auth_button_sponsor` | `string` | Optional | label for Sponsor auth button<br>**Default**: `'Sign in as Guest'` |
| `auth_label` | `string` | Optional | **Default**: `'“Connect to WiFi with”'` |
| `back_link` | `string` | Optional | label of the link to go back to /logon<br>**Default**: `'Go back and edit request form'` |
| `color` | `string` | Optional | **Default**: `'“#1074bc”'` |
| `color_dark` | `string` | Optional | **Default**: `'“#0b5183”'` |
| `color_light` | `string` | Optional | **Default**: `'“#3589c6”'` |
| `company` | `bool` | Optional | whether company field is required<br>**Default**: `False` |
| `company_error` | `string` | Optional | error message when company not provided<br>**Default**: `'Please provide company name'` |
| `company_label` | `string` | Optional | label of company field<br>**Default**: `'Company'` |
| `created_time` | `float` | Optional | - |
| `email` | `bool` | Optional | whether email field is required<br>**Default**: `False` |
| `email_access_domain_error` | `string` | Optional | error message when a user has valid social login but doesn’t match specified email domains.<br>**Default**: `'Access is restricted by email domain'` |
| `email_cancel` | `string` | Optional | **Default**: `'Cancel'` |
| `email_code_error` | `string` | Optional | **Default**: `'Please provide valid alternate email'` |
| `email_error` | `string` | Optional | error message when email not provided<br>**Default**: `'Please provide valid email'` |
| `email_field_label` | `string` | Optional | **Default**: `'Enter your email address'` |
| `email_label` | `string` | Optional | label of email field<br>**Default**: `'Email'` |
| `email_message` | `string` | Optional | **Default**: `'We will email you an authentication code which you can use to connect to the WiFi network.'` |
| `email_submit` | `string` | Optional | **Default**: `'“Send Access Code”'` |
| `email_title` | `string` | Optional | **Default**: `'“Sign in with Email”'` |
| `field_1` | `bool` | Optional | whether to ask field1<br>**Default**: `False` |
| `field_1_error` | `string` | Optional | error message when field1 not provided<br>**Default**: `'Please provide field1'` |
| `field_1_label` | `string` | Optional | label of field1<br>**Default**: `'Custom1'` |
| `field_1_required` | `bool` | Optional | whether field1 is required field<br>**Default**: `False` |
| `field_2` | `bool` | Optional | whether to ask field2<br>**Default**: `False` |
| `field_2_error` | `string` | Optional | error message when field2 not provided<br>**Default**: `'Please provide field2'` |
| `field_2_label` | `string` | Optional | label of field2<br>**Default**: `'Custom2'` |
| `field_2_required` | `bool` | Optional | whether field2 is required field<br>**Default**: `False` |
| `field_3` | `bool` | Optional | whether to ask field3<br>**Default**: `False` |
| `field_3_error` | `string` | Optional | error message when field3 not provided<br>**Default**: `'Please provide field3'` |
| `field_3_label` | `string` | Optional | label of field3<br>**Default**: `'Custom3'` |
| `field_3_required` | `bool` | Optional | whether field3 is required field<br>**Default**: `False` |
| `field_4` | `bool` | Optional | whether to ask field4<br>**Default**: `False` |
| `field_4_error` | `string` | Optional | error message when field4 not provided<br>**Default**: `'Please provide field4'` |
| `field_4_label` | `string` | Optional | label of field4<br>**Default**: `'Custom4'` |
| `field_4_required` | `bool` | Optional | whether field4 is required field<br>**Default**: `False` |
| `for_site` | `bool` | Optional | - |
| `id` | `uuid\|string` | Optional | - |
| `message` | `string` | Optional | **Default**: `'Please enjoy the complimentary Wifi'` |
| `modified_time` | `float` | Optional | - |
| `name` | `bool` | Optional | whether name field is required<br>**Default**: `False` |
| `name_error` | `string` | Optional | error message when name not provided<br>**Default**: `'Please provide your name'` |
| `name_label` | `string` | Optional | label of name field<br>**Default**: `'Name'` |
| `optout` | `bool` | Optional | whether to display “Do Not Store My Personal Information” |
| `optout_label` | `string` | Optional | **Default**: `'Do Not Store My Personal Information'` |
| `org_id` | `uuid\|string` | Optional | - |
| `page_title` | `string` | Required | **Default**: `'Welcome'` |
| `passphrase_cancel` | `string` | Optional | **Default**: `'Cancel'` |
| `passphrase_error` | `string` | Optional | error message when invalid passphrase is provided<br>**Default**: `'Invalid Passphrase'` |
| `passphrase_label` | `string` | Optional | **Default**: `'Passphrase'` |
| `passphrase_message` | `string` | Optional | **Default**: `'Login using passphrase'` |
| `passphrase_submit` | `string` | Optional | **Default**: `'Sign in'` |
| `passphrase_title` | `string` | Optional | Title for passphrase details page<br>**Default**: `'Sign in with Passphrase'` |
| `powered_by` | `bool` | Optional | whether to show “Powered by Mist”<br>**Default**: `True` |
| `required_field_label` | `string` | Optional | label to denote required field<br>**Default**: `'required'` |
| `sign_in_label` | `string` | Optional | label of the button to /signin<br>**Default**: `'Sign In'` |
| `site_id` | `uuid\|string` | Optional | - |
| `sms_carrier_default` | `string` | Optional | **Default**: `'Please Select'` |
| `sms_carrier_error` | `string` | Optional | **Default**: `'Please select a mobile carrier'` |
| `sms_carrier_field_label` | `string` | Optional | label for mobile carrier drop-down list<br>**Default**: `'Mobile Carrier'` |
| `sms_code_cancel` | `string` | Optional | Label for cancel confirmation code submission<br>**Default**: `'Cancel'` |
| `sms_code_error` | `string` | Optional | error message when confirmation code is invalid<br>**Default**: `'Invalid Access Code'` |
| `sms_code_field_label` | `string` | Optional | **Default**: `'Confirmation Code'` |
| `sms_code_message` | `string` | Optional | **Default**: `'Enter the confirmation code'` |
| `sms_code_submit` | `string` | Optional | Label for confirmation code submit button<br>**Default**: `'Submit Code'` |
| `sms_code_title` | `string` | Optional | **Default**: `'Access Code'` |
| `sms_country_field_label` | `string` | Optional | “Country Code” |
| `sms_country_format` | `string` | Optional | **Default**: `'“+1”'` |
| `sms_have_access_code` | `string` | Optional | Label for checkbox to specify that the user has access code<br>**Default**: `'I have an access code'` |
| `sms_message_format` | `string` | Optional | format of access code sms message. {{code}} and {{duration}} are place holders and should be retained as is.<br>**Default**: `'Code {{code}} expires in {{duration}} minutes.'` |
| `sms_number_cancel` | `string` | Optional | label for canceling mobile details for SMS auth<br>**Default**: `'Cancel'` |
| `sms_number_error` | `string` | Optional | **Default**: `'Invalid Mobile Number'` |
| `sms_number_field_label` | `string` | Optional | label for field to provide mobile number<br>**Default**: `'Mobile Number'` |
| `sms_number_format` | `string` | Optional | **Default**: `'“2125551212 (digits only)”'` |
| `sms_number_message` | `string` | Optional | **Default**: `'We will send an access code to your mobile number which you can use to connect to the WiFi network. Message and data rates may apply.'` |
| `sms_number_submit` | `string` | Optional | label for submit button for code generation<br>**Default**: `'Sign In'` |
| `sms_number_title` | `string` | Optional | Title for phone number details<br>**Default**: `'Text Message Confirmation'` |
| `sms_username_format` | `string` | Optional | **Default**: `'username'` |
| `sms_validity_duration` | `float` | Optional | how long confirmation code should be considered valid (in minutes)<br>**Default**: `5` |
| `sponsor_auto_approved` | `string` | Optional | **Default**: `'Your request was approved.'` |
| `sponsor_auto_approved_note` | `string` | Optional | **Default**: `'Your notification has been sent to'` |
| `sponsor_back_link` | `string` | Optional | **Default**: `'Go back and edit request form'` |
| `sponsor_cancel` | `string` | Optional | **Default**: `'Cancel'` |
| `sponsor_email` | `string` | Optional | label for Sponsor Email<br>**Default**: `'Please provide valid sponsor email'` |
| `sponsor_email_error` | `string` | Optional | **Default**: `'Please provide valid sponsor email'` |
| `sponsor_email_template` | `string` | Optional | “html template to replace/override default sponsor email template” |
| `sponsor_info_approved` | `string` | Optional | **Default**: `'Your request was approved by'` |
| `sponsor_info_denied` | `string` | Optional | **Default**: `'Your request was denied by'` |
| `sponsor_info_pending` | `string` | Optional | **Default**: `'Your notification has been sent to'` |
| `sponsor_name` | `string` | Optional | label for Sponsor Name<br>**Default**: `'Sponsor Name'` |
| `sponsor_name_error` | `string` | Optional | **Default**: `'Please provide sponsor’s name'` |
| `sponsor_note_pending` | `string` | Optional | **Default**: `'Please wait for them to acknowledge.'` |
| `sponsor_status_approved` | `string` | Optional | text to display if sponsor approves request<br>**Default**: `'Your request was approved'` |
| `sponsor_status_denied` | `string` | Optional | text to display when sponsor denies request<br>**Default**: `'Your request was denied'` |
| `sponsor_status_pending` | `string` | Optional | text to display if request is still pending<br>**Default**: `'Notification Sent'` |
| `sponsor_submit` | `string` | Optional | submit button label to notify sponsor about guest request<br>**Default**: `'Notify Sponsor'` |
| `sponsors_auto_approved_note` | `string` | Optional | **Default**: `'Your notification has been sent to the sponsors."'` |
| `sponsors_error` | `string` | Optional | **Default**: `'Please select a sponsor'` |
| `tos` | `bool` | Optional | **Default**: `True` |
| `tos_accept_label` | `string` | Optional | prefix of the label of the link to go to /tos<br>**Default**: `'I accept the Terms of Service'` |
| `tos_error` | `string` | Optional | error message when tos not accepted<br>**Default**: `'Please review and accept terms of service'` |
| `tos_link` | `string` | Optional | label of the link to go to /tos<br>**Default**: `'Terms of Service'` |
| `tos_text` | `string` | Optional | text of the Terms of Service<br>**Default**: `'terms of service'` |

## Example (as JSON)

```json
{
  "accessCodeAlternateEmail": "Please provide valid alternate email",
  "authButtonAmazon": "Sign in with Amazon",
  "authButtonAzure": "Sign in with Azure",
  "authButtonEmail": "Sign in with Email",
  "authButtonFacebook": "Sign in with Facebook",
  "authButtonGoogle": "Sign in with Google",
  "authButtonMicrosoft": "Sign in with Microsoft",
  "authButtonSms": "Sign in with Text Message",
  "authButtonSponsor": "Sign in as Guest",
  "authLabel": "“Connect to WiFi with”",
  "backLink": "Go back and edit request form",
  "color": "“#1074bc”",
  "colorDark": "“#0b5183”",
  "colorLight": "“#3589c6”",
  "company": false,
  "companyError": "Please provide company name",
  "companyLabel": "Company",
  "email": false,
  "emailAccessDomainError": "Access is restricted by email domain",
  "emailCancel": "Cancel",
  "emailCodeError": "Please provide valid alternate email",
  "emailError": "Please provide valid email",
  "emailFieldLabel": "Enter your email address",
  "emailLabel": "Email",
  "emailMessage": "We will email you an authentication code which you can use to connect to the WiFi network.",
  "emailSubmit": "“Send Access Code”",
  "emailTitle": "“Sign in with Email”",
  "field1": false,
  "field1Error": "Please provide field1",
  "field1Label": "Custom1",
  "field1Required": false,
  "field2": false,
  "field2Error": "Please provide field2",
  "field2Label": "Custom2",
  "field2Required": false,
  "field3": false,
  "field3Error": "Please provide field3",
  "field3Label": "Custom3",
  "field3Required": false,
  "field4": false,
  "field4Error": "Please provide field4",
  "field4Label": "Custom4",
  "field4Required": false,
  "message": "Please enjoy the complimentary Wifi",
  "name": false,
  "nameError": "Please provide your name",
  "nameLabel": "Name",
  "optoutLabel": "Do Not Store My Personal Information",
  "pageTitle": "Welcome",
  "passphraseCancel": "Cancel",
  "passphraseError": "Invalid Passphrase",
  "passphraseLabel": "Passphrase",
  "passphraseMessage": "Login using passphrase",
  "passphraseSubmit": "Sign in",
  "passphraseTitle": "Sign in with Passphrase",
  "poweredBy": true,
  "requiredFieldLabel": "required",
  "signInLabel": "Sign In",
  "smsCarrierDefault": "Please Select",
  "smsCarrierError": "Please select a mobile carrier",
  "smsCarrierFieldLabel": "Mobile Carrier",
  "smsCodeCancel": "Cancel",
  "smsCodeError": "Invalid Access Code",
  "smsCodeFieldLabel": "Confirmation Code",
  "smsCodeMessage": "Enter the confirmation code",
  "smsCodeSubmit": "Submit Code",
  "smsCodeTitle": "Access Code",
  "smsCountryFormat": "“+1”",
  "smsHaveAccessCode": "I have an access code",
  "smsMessageFormat": "Code {{code}} expires in {{duration}} minutes.",
  "smsNumberCancel": "Cancel",
  "smsNumberError": "Invalid Mobile Number",
  "smsNumberFieldLabel": "Mobile Number",
  "smsNumberFormat": "“2125551212 (digits only)”",
  "smsNumberMessage": "We will send an access code to your mobile number which you can use to connect to the WiFi network. Message and data rates may apply.",
  "smsNumberSubmit": "Sign In",
  "smsNumberTitle": "Text Message Confirmation",
  "smsUsernameFormat": "username",
  "smsValidityDuration": 5,
  "sponsorAutoApproved": "Your request was approved.",
  "sponsorAutoApprovedNote": "Your notification has been sent to",
  "sponsorBackLink": "Go back and edit request form",
  "sponsorCancel": "Cancel",
  "sponsorEmail": "Please provide valid sponsor email",
  "sponsorEmailError": "Please provide valid sponsor email",
  "sponsorInfoApproved": "Your request was approved by",
  "sponsorInfoDenied": "Your request was denied by",
  "sponsorInfoPending": "Your notification has been sent to",
  "sponsorName": "Sponsor Name",
  "sponsorNameError": "Please provide sponsor’s name",
  "sponsorNotePending": "Please wait for them to acknowledge.",
  "sponsorStatusApproved": "Your request was approved",
  "sponsorStatusDenied": "Your request was denied",
  "sponsorStatusPending": "Notification Sent",
  "sponsorSubmit": "Notify Sponsor",
  "sponsorsAutoApprovedNote": "Your notification has been sent to the sponsors.\"",
  "sponsorsError": "Please select a sponsor",
  "tos": true,
  "tosAcceptLabel": "I accept the Terms of Service",
  "tosError": "Please review and accept terms of service",
  "tosLink": "Terms of Service",
  "tosText": "terms of service",
  "alignment": "alignment2"
}
```

