
# Webhook Delivery

## Structure

`WebhookDelivery`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `string` | Optional | error message, if there is one |
| `id` | `uuid\|string` | Optional | delivery ID |
| `org_id` | `uuid\|string` | Optional | - |
| `req_headers` | `string` | Optional | HTTP request headers |
| `req_payload` | `string` | Optional | HTTP request payload |
| `req_url` | `string` | Optional | HTTP request URL |
| `resp_body` | `string` | Optional | HTTP response body |
| `resp_headers` | `string` | Optional | HTTP response headers |
| `site_id` | `uuid\|string` | Optional | - |
| `status_code` | `int` | Optional | - |
| `timestamp` | `float` | Optional | - |
| `topic` | [`Topic1Enum`](../../doc/models/topic-1-enum.md) | Optional | webhook topic |
| `webhook_id` | `uuid\|string` | Optional | - |

## Example (as JSON)

```json
{
  "id": "55b0f02f-ebf6-4ad2-8b10-200508a97581",
  "org_id": "fc7e2967-e7ef-41e6-b007-1217713de05a",
  "req_headers": "{\"Content-Type\":[\"application/json\"],\"User-Agent\":[\"Mist-webhook\"]}",
  "req_payload": "{\"topic\":\"audits\",\"events\":[{\"admin_name\":\"John Doe john.doe@juniper.net\",\"after\":\"{\\\"radio_config\\\": {\\\"band_24\\\": {\\\"disabled\\\": false, \\\"allow_rrm_disable\\\": false, \\\"power_min\\\": null, \\\"power_max\\\": null, \\\"power\\\": 10, \\\"preamble\\\": \\\"short\\\", \\\"channels\\\": [1, 10], \\\"bandwidth\\\": 20}}}\",\"before\":\"{\\\"radio_config\\\": {\\\"band_24\\\": {\\\"disabled\\\": false, \\\"allow_rrm_disable\\\": false, \\\"power_min\\\": 8, \\\"power_max\\\": 18, \\\"power\\\": null, \\\"preamble\\\": \\\"long\\\", \\\"channels\\\": [1, 10], \\\"bandwidth\\\": 20}}}\",\"id\":\"737909a2-04ff-4aeb-b9da-cc924e74a4dd\",\"message\":\"Update Site Settings\",\"org_id\":\"fc7e2967-e7ef-41e6-b007-1217713de05a\",\"site_id\":\"256c3a35-9cb7-436e-bc6d-314972645d95\",\"site_name\":\"Test Site\",\"src_ip\":\"1.2.3.4\",\"timestamp\":1685956576.923601,\"user_agent\":\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36\"}]}",
  "req_url": "http://example.com",
  "resp_body": "Ok",
  "site_id": "256c3a35-9cb7-436e-bc6d-314972645d95",
  "status_code": 200,
  "timestamp": 1687962508.58366,
  "topic": "audits",
  "webhook_id": "7a11b901-f719-4c91-8aef-deb8699a6364",
  "error": "error4"
}
```

