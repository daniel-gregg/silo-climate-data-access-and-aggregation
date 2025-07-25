# silo-climate-data-access-and-aggregation
Scripts to access the SILO (Queensland Government) climate data and to download and aggregate this for user-specified target regions. 

## getting started

### Setting up an Amazon IAM User profile (SILO data access)

#### Set up your profile

#### Create access key and password for a user

#### Create a permissions/policy set for the user
You need to ttach this policy to your IAM user in order to access the silo data. To do sofollow these steps:

1. Sign in to the AWS Management Console and open the IAM console at https://console.aws.amazon.com/iam/.
2. In the navigation pane, click "Policies", then click the "Create policy" button.
3. Choose the "JSON" tab and replace the existing content with the JSON policy:
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::silo-open-data/*",
                "arn:aws:s3:::silo-open-data"
            ]
        }
    ]
}
```
4. Click "Review policy", give your policy a name and description, and click "Create policy".
5. In the navigation pane, click "Users", and then click on the name of the user you want to attach the policy to.
6. On the "User details" page, navigate to the "Permissions" tab.
7. Click "Add permissions", then choose "Attach existing policies directly".
8. Search for the policy you just created, select it, and click the "Attach policy" button.

### Copernicus registration (NDVI/ground cover data)

Follow the instructions here:
https://documentation.dataspace.copernicus.eu/APIs/openEO/Python_Client/Python.html

### Other setup

#### Create .env variables to safeguard your passwords
Check if a .env file exists in your main directory (it should). If not, create one.
Add your Amazon IAM User key and password to the .env as:

```
AWS_ACCESS_KEY_ID = 'XXX'
AWS_SECRET_KEY = 'YYY'
```

#### Ensure .gitignore includes 'data/'
BEFORE running the script ensure your .gitignore file includes:
```
data/
```
This ensures that the data folder is not shared to github. The data files are large and should not be copied across commits/push/pull between your local drive and the repository. This is also good practice for data safety in general. 

## Run script


### get_data


### choose geo masking strategy


### mask and aggregate data


