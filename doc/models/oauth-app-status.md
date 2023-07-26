
# Oauth App Status

## Structure

`OauthAppStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List of Account`](../../doc/models/account.md) | Optional | List of linked apps(zoom/teams) account details |
| `authorization_url` | `string` | Optional | Only if `forward_url` is set in the request |
| `linked` | `bool` | Optional | OAuth application linked status, is mist portal authorized with the OAuth appliation |

## Example (as JSON)

```json
{
  "accounts": [
    {
      "account_id": "account_id2",
      "error": "error4",
      "last_status": {
        "key1": "val1",
        "key2": "val2"
      },
      "last_sync": {
        "key1": "val1",
        "key2": "val2"
      },
      "linked_by": "linked_by2"
    },
    {
      "account_id": "account_id3",
      "error": "error5",
      "last_status": {
        "key1": "val1",
        "key2": "val2"
      },
      "last_sync": {
        "key1": "val1",
        "key2": "val2"
      },
      "linked_by": "linked_by1"
    }
  ],
  "authorization_url": "authorization_url0",
  "linked": false
}
```

