# Msps Inventory

```python
msps_inventory_controller = client.msps_inventory
```

## Class Name

`MspsInventoryController`


# Get Msp Inventory by Mac

Get Inventoy By device MAC address

```python
def get_msp_inventory_by_mac(self,
                            msp_id,
                            device_mac)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `msp_id` | `uuid\|string` | Template, Required | - |
| `device_mac` | `string` | Template, Required | **Constraints**: *Pattern*: `^[0-9a-fA-F]{12}$` |

## Response Type

[`ApiV1MspsInventoryResponse`](../../doc/models/api-v1-msps-inventory-response.md)

## Example Usage

```python
msp_id = '000000ab-00ab-00ab-00ab-0000000000ab'

device_mac = '0000000000ab'

result = msps_inventory_controller.get_msp_inventory_by_mac(
    msp_id,
    device_mac
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "mac": "5c5b35000018",
  "model": "AP200",
  "org_id": "b069b358-4c97-5319-1f8c-7c5ca64d6ab1",
  "serial": "FXLH2015150025",
  "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
  "type": "ap"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1MspsInventory401ErrorException`](../../doc/models/api-v1-msps-inventory-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1MspsInventory403ErrorException`](../../doc/models/api-v1-msps-inventory-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1MspsInventory404ErrorException`](../../doc/models/api-v1-msps-inventory-404-error-exception.md) |

