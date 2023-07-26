
# Ike Proposal

## Structure

`IkeProposal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auth_algo` | [`AuthAlgoEnum`](../../doc/models/auth-algo-enum.md) | Optional | - |
| `dh_group` | [`DhGroupEnum`](../../doc/models/dh-group-enum.md) | Optional | * 1<br>* 2 (1024-bit)<br>* 5<br>* 14 (default, 2048-bit)<br>* 15 (3072-bit)<br>* 16 (4096-bit)<br>* 19 (256-bit ECP)<br>* 20 (384-bit ECP)<br>* 21 (521-bit ECP)<br>* 24 (2048-bit ECP)<br>**Default**: `'14'` |
| `enc_algo` | [`EncAlgoEnum`](../../doc/models/enc-algo-enum.md) | Optional | **Default**: `'aes256'` |

## Example (as JSON)

```json
{
  "dh_group": "14",
  "enc_algo": "aes256",
  "auth_algo": "md5"
}
```

