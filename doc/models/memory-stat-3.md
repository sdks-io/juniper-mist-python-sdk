
# Memory Stat 3

Memory usage

## Structure

`MemoryStat3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `active` | `int` | Optional | The amount of memory, in kibibytes, that has been used more recently and is usually not reclaimed unless absolutely necessary. |
| `available` | `int` | Optional | An estimate of how much memory is available for starting new applications, without swapping. |
| `buffers` | `int` | Optional | The amount, in kibibytes, of temporary storage for raw disk blocks. |
| `cached` | `int` | Optional | The amount of physical RAM, in kibibytes, used as cache memory. |
| `free` | `int` | Optional | The amount of physical RAM, in kibibytes, left unused by the system |
| `inactive` | `int` | Optional | The amount of memory, in kibibytes, that has been used less recently and is more eligible to be reclaimed for other purposes. |
| `swap_cached` | `int` | Optional | The amount of memory, in kibibytes, that has once been moved into swap, then back into the main memory, but still also remains in the swapfile. |
| `swap_free` | `int` | Optional | The total amount of swap free, in kibibytes. |
| `swap_total` | `int` | Optional | The total amount of swap available, in kibibytes. |
| `total` | `int` | Optional | Total amount of usable RAM, in kibibytes, which is physical RAM minus a number of reserved bits and the kernel binary code |
| `usage` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "active": 142,
  "available": 56,
  "buffers": 154,
  "cached": 194,
  "free": 84
}
```

