
# Api V1 Utils Test Twilio Request

## Structure

`ApiV1UtilsTestTwilioRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mfrom` | `string` | Required | One of the numbers you have in your Twilio account |
| `to` | `string` | Required | Phone number of the recipient of SMS |
| `twilio_auth_token` | `string` | Required | Auth Token associated with twilio account |
| `twilio_sid` | `string` | Required | Twilio Account SID |

## Example (as JSON)

```json
{
  "from": "from2",
  "to": "to6",
  "twilio_auth_token": "twilio_auth_token4",
  "twilio_sid": "twilio_sid2"
}
```

