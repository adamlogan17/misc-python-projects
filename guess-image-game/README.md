## Create Service Account JSON

Instructions below found [here](https://stackoverflow.com/questions/46287267/how-can-i-get-the-file-service-account-json-for-google-translate-api)

1. Go to <https://console.cloud.google.com/apis/credentials>
   1. (Optional) Create a new project
2. On the top left there is a blue "create credentials" button click it and select "service account key." (see below if its not there)
3. Choose the service account you want, that you created
4. Go to the 'Keys' tab
5. Select the 'ADD KEY' button
6. Select 'Generate new key'
7. It should allow give you a json to download

## Enable Google APIs

1. Go to <https://console.cloud.google.com/apis/credentials>
2. Ensure the same project as your service account JSON is selected
3. Go to 'Enabled APIs and services', in the side bar
4. Select '+ ENABLE APIS AND SERVICES'
5. Search for 'Google Slides API'
6. Hit 'Enable'
7. Search for 'Google Drive API'
8. Hit 'Enable'