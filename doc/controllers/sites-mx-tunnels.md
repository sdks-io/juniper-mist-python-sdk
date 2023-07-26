# Sites Mx Tunnels

```python
sites_mx_tunnels_controller = client.sites_mx_tunnels
```

## Class Name

`SitesMxTunnelsController`


# Preempt Sites Mx Tunnel

To preempt AP’s which are not connected to preferred peer to the preferred peer

```python
def preempt_sites_mx_tunnel(self,
                           site_id,
                           mxtunnel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_id` | `string` | Template, Required | - |
| `mxtunnel_id` | `string` | Template, Required | - |

## Response Type

[`ApiV1SitesMxtunnelsPreemptApsResponse`](../../doc/models/api-v1-sites-mxtunnels-preempt-aps-response.md)

## Example Usage

```python
site_id = 'site_id6'

mxtunnel_id = 'mxtunnel_id2'

result = sites_mx_tunnels_controller.preempt_sites_mx_tunnel(
    site_id,
    mxtunnel_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The API endpoint exists but its syntax/payload is incorrect, detail may be given | `APIException` |
| 401 | Unauthorized | [`ApiV1SitesMxtunnelsPreemptAps401ErrorException`](../../doc/models/api-v1-sites-mxtunnels-preempt-aps-401-error-exception.md) |
| 403 | Permission Denied | [`ApiV1SitesMxtunnelsPreemptAps403ErrorException`](../../doc/models/api-v1-sites-mxtunnels-preempt-aps-403-error-exception.md) |
| 404 | Not found. The API endpoint doesn't exist or resource doesn't exist | [`ApiV1SitesMxtunnelsPreemptAps404ErrorException`](../../doc/models/api-v1-sites-mxtunnels-preempt-aps-404-error-exception.md) |

