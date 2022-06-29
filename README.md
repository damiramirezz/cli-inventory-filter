# Lab Python - Inventory Filter

[Lab](https://edransdevelopment.atlassian.net/wiki/spaces/HC/pages/2254307331/LAB+-+Python+2022)

## Inventory filter
Given a file that contains a **server inventory**, a list of devices (one per line) that follow a specific naming standard, create a python script that will act as a command that allows the user to retrieve a sub set of the devices, filtered by any or a combination of the characteristics defined in the naming standard, print the sub set to the terminal as well as the amount of devices.

The server inventory has the following naming convention:


```
{id}.{task}.{environment}.{location}.{team}
Example: 45.dns.dev.bcn.siteops
```
The script will get its user input at the time of execution as most CLI commands do: 


```
filter.py [-f inventory_file.txt] [-i id] [-k task] [-e env] [-l location] [-t team]
```
Arguments will be optional, if no arguments are supplied, the command will return the full list. The script should also print a message if no devices are found that match the requirements, and a different message if a device that does not follow the naming standard is found.

Proper handling of errors will be evaluated (ie the user did not supply a correct path to the server_list.txt)

**BONUS**: Add an argument to send the output to a new text file called filtered_inventory.txt on the user’s desktop. 