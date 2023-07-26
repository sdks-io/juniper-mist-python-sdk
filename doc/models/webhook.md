
# Webhook

## Structure

`Webhook`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_time` | `float` | Optional | - |
| `enabled` | `bool` | Optional | whether webhook is enabled<br>**Default**: `True` |
| `for_site` | `bool` | Optional | - |
| `headers` | `object` | Optional | custom headers : the headers name and value must be string, total bytes of headers name and value must be less than 1000 |
| `id` | `uuid\|string` | Optional | - |
| `modified_time` | `float` | Optional | - |
| `name` | `string` | Optional | name of the webhook |
| `org_id` | `uuid\|string` | Optional | - |
| `secret` | `string` | Optional | only if `type`=`http-post`<br>when `secret` is provided, two HTTP headers will be added:<br><br>* X-Mist-Signature-v2: HMAC_SHA256(secret, body)<br>* X-Mist-Signature: HMAC_SHA1(secret, body) |
| `site_id` | `uuid\|string` | Optional | - |
| `splunk_token` | `string` | Optional | splunk token (If splunk_token is not defined for a type Splunk webhook, it will not send, regardless if the webhook receiver is configured to accept it.) |
| `topics` | [`List of TopicEnum`](../../doc/models/topic-enum.md) | Optional | N.B. For org webhooks, only device-events/alarms/audits/client-join/client-sessions/nac-sessions topics are supported. |
| `mtype` | [`Type41Enum`](../../doc/models/type-41-enum.md) | Optional | http-post (default) / splunk / google-pubsub / aws-sns |
| `url` | `string` | Optional | - |
| `verify_cert` | `bool` | Optional | when url uses HTTPS, whether to verify the certificate<br>**Default**: `False` |

## Example (as JSON)

```json
{
  "enabled": true,
  "verify_cert": false,
  "created_time": 198.3,
  "for_site": false,
  "headers": {
    "key1": "val1",
    "key2": "val2"
  },
  "id": "00001770-0000-0000-0000-000000000000"
}
```

