# Accessing Private Datasets on BossDB

To access private (non-public) data that is hosted on BossDB, you will need to create an account and do some additional set up to work with [intern](https://github.com/jhuapl-boss/intern). To access public data you do not need to create an account!

You can follow along with this document or watch a video tutorial [here](https://www.youtube.com/watch?v=eVNr6Pzxoh8&t=50s). 

## Creating a BossDB account

To create an account, navigate to [api.bossdb.io](api.bossdb.io). You will be prompted to log in or register a new account. Click the Register button at the bottom of the page and fill out the requested information, including a username and password. Click the large blue Register button at the bottom of the page and you will be signed in to the Boss Management Console.

I recommend taking the tour of the management console by clicking the **Tour** button at the top right of the page. 

## [Boss Mangement Console](https://api.bossdb.io/v1/mgmt/)

The boss management console will show you which datasets you have access to and which permissions groups you belong to. 

### [Manage Resources](https://api.bossdb.io/v1/mgmt/resources)

If you click the `Manage Resources` button on the top of the page, you can view the data collections to which you have access. Only public datasets and private datasets that you have been given permission to view will appear here. Any data collections you create will also be visible here. 

### [Manage Groups](https://api.bossdb.io/v1/mgmt/groups)

If you click the `Manage Groups` button on the top of the page, you can view the permissions groups you belong to. These groups will determine what data you can view. 

### [Authentication API Token](https://api.bossdb.io/v1/mgmt/token)

To access private data using our python API intern, you will need to generate an API token. Click on your username in the top right corner and `API Token`. Then click the `Generate Token` button to generate your own API token. Keep this token private, like a password, as anyone with this token can access your private datasets. You can revoke and generate a new token at any time on this page. 

To use this token with intern you will need to create a new configuration file called `intern.cfg` on your computer at the following location:

```
Mac and Linux:
~/.intern/intern.cfg

Windows:
C:Users\myusername\.intern\intern.cfg
```

Inside the file you will need to place the following information:

```
[Default]
protocol = https
host = api.bossdb.io
token = <your token here>
```

The intern API will automatically know to look for this file in that location and you should now be able to access your private datasets using intern in python. 

