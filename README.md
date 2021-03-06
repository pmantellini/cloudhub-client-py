# Python Client for Cloudhub API

API Documentation: http://www.mulesoft.org/documentation/display/current/API

+ [Basic help](#basichelp)
+ [Creation of **cloudhub** alias](#cloudhubalias)
	* [Mac OS X](#chaliasmacosx)
+ [Subcommands](#subcommands)
    * [Get Application Info](#getapplicationinfo)
    * [Get All Applications](#getallapplications)
    * [Update Application Metadata](#updateapplicationmetadata)
    * [Deploy Application](#deployapplication)
    * [Create Application](#createapplication)
    * [Delete Application](#deleteapplication)
+ [Environments (Sandbox)](#environments)
+ [Requirements](#requirements)

## Basic help <a name="basichelp"/>

Command list and help. Try in the cloned project:
```
python cloudhubClient.py -h
```

Subcommands help
```
python cloudhubClient.py {subcommand} -h
```

## Creation of **cloudhub** alias<a name="cloudhubalias"/>

Setting an alias to run the client can provide a better experience. You should be able to use the client from everywhere in your terminal by just typing **cloudhub** instead of writing **python cloudhubClient.py** under the client directory.
```
cloudhub -h
cloudhub {subcommand} -h
```

### Mac OS X <a name="chaliasmacosx"/> 

Steps from Command Line
```
git clone https://github.com/cesaraugustogarcia/cloudhub-client-py
cd cloudhub-client-py
mkdir ~/.cloudhubclient
cp -rf . ~/.cloudhubclient/
echo -e "\nalias cloudhub='python ~/.cloudhubclient/cloudhubClient.py'" >> ~/.bash_profile
chmod +x ~/.cloudhubclient/cloudhubClient.py
source ~/.bash_profile
```

This steps copy the project on your User directory (~). In some cases the last step could depend on your terminal, for example ```source ~/.bash_profile``` could be required instead.

## Subcommands <a name="subcommands"/>


### Get Application Info <a name="getapplicationinfo"/>

Doc: http://www.mulesoft.org/documentation/display/current/Get+Application

**Usage** 
Lets say we want to get the belonging information for an app that placed in *https://fandermole.cloudhub.io/*. Then I should run the following command:
```
python cloudhubClient.py gai -cu cloudhubUser -cp cloudhubPassword -an fandermole
```


### Get All Applications <a name="getallapplications"/>

Doc: http://www.mulesoft.org/documentation/display/current/List+All+Applications

**Usage** 
```
python cloudhubClient.py gaa -cu cloudhubUser -cp cloudhubPassword
```


### Update Application Metadata <a name="updateapplicationmetadata"/>

Doc: http://www.mulesoft.org/documentation/display/current/Update+Application+Metadata

**Usage** 
Lets now figure out we want to update the properties for an app that is placed in ```https://fandermole.cloudhub.io/```. Then I should run the following command:
```
python cloudhubClient.py uam -cu cloudhubUser -cp cloudhubPassword -an fandermole --properties_path propertiesFilePath
```


This method expects a properties file that should look like the following example:
```
#Endpoints configuration
propertyname.a=propertya
propertyname.b=propertyb
```
### Deploy Application <a name="deployapplication"/>

Doc: http://www.mulesoft.org/documentation/display/current/Deploying+a+CloudHub+Application

**Usage** 
```
python cloudhubClient.py dam -cu cloudhubUser -cp cloudhubPassword --file_path application.zip
```


### Create Application <a name="createapplication"/>

Doc: http://www.mulesoft.org/documentation/display/current/Create+Application

**Usage** 
```
python cloudhubClient.py cap -cu cloudhubUser -cp cloudhubPassword -an app_name --properties_path application.zip --mule_version 3.4.1
```


This method expects a properties file that should look like the following example:
```
#Endpoints configuration
propertyname.a=propertya
propertyname.b=propertyb
```

### Delete Application <a name="deleteapplication"/>

Doc: http://www.mulesoft.org/documentation/display/current/Delete+Application

**Usage** 
```
python cloudhubClient.py dea -cu cloudhubUser -cp cloudhubPassword -an app_name
```


## Environments (Sandbox) <a name="environments"/>

In order to use this Command Line Client with apps on different environments than the default, the environment name after a ´@´ symbol must be added to the User Name on every call.

For example if you have a ***qa*** environment that you are using as a Sandbox, and want to use Get Application Info for the app created on this environment, the call should be like:

```
python cloudhubClient.py gai -cu cloudhubUser@qa -cp cloudhubPassword -an fandermole
```


## Requirements <a name="requirements"/>

### Python requests module

How to install Docs: http://docs.python-requests.org/en/latest/user/install/  

Take into account that you may need to excecute the instalation using admin permissions; otherwise you could receive the following error message:
```
[Errno 13] Permission denied: '/Library/Python/2.7/site-packages/test-easy-install-2478.write-test'
```
