# Google hosted authentification for the web application

### Create a project in Google Cloud

- Go to website: `https://console.cloud.google.com/` 
- Create a project
- Go to `API` > `Credentials` > `Create Credential`
- First `Configure Consent Screen`
- Choose `External` to accept any user and `Create`
- Fill up with your info and press `Save and continue`

Go back to dashboard

### Create Google Auth credentials

- From dashboard, go to `API` and then to `Credentials`
- Press `Create Credentials` and choose `OAuth client ID`
- Feel up the form
- Add `URI` ('http://localhost/callback ') for `Authorized redirect URIs`, otherwise it won't work.
- After saving, download the credentials into json format and paste it into project folder
<!-- -->
  Credit for this repo: https://www.youtube.com/watch?v=n4e3Cy2Tq3Q

  ### How to run
  Build the docker image
  ```bash
  docker-compose build
  ```
  Start the container
  ```bash
  docker-compose up
  ```