# fundare
Django Rest Framework crowdfunding app project. Introducing Fundare! Get your fave charities funded by Fun dares!

- PLEASE NOTE - I have used dares instead of projects and dollars instead of pledges.

See below for links;

## Links
- Link to [project brief](https://docs.google.com/document/d/1ocfmn1AmxYTIDKVRrycK2PQ4Fx3dnMd4JXgC0GE8csQ/edit?usp=sharing)
- Link to [Github repo](https://github.com/bel-lloyd/fundare)
- Link to [deployed project](https://fundare-crowdfunding-app.herokuapp.com/dares/)

## Stack
# Backend
- Python
- Django
- Django Rest Framework (DRF)
# Frontend
- Javascript
- React
# Tools
- VSCode
- Insomnia

## Screenshots

- Insomnia Screenshots
    - GET for Dares run on Heroku
    <img src="screenshots/GET-Heroku.png"/>
    - POST for Dares fun on Heroku
    <img src="screenshots/POST-Heroku.png"/>
    - AUTH TOKEN request from Heroku
    <img src="screenshots/POST-auth-token.png"/>

## API Endpoints

1. Please reference API specs in [brief document here](https://docs.google.com/document/d/1ocfmn1AmxYTIDKVRrycK2PQ4Fx3dnMd4JXgC0GE8csQ/edit#)

Step by step

## How to register a new user
1. Navigate to the POST /users/ request
2. In the 'body' tab, select JSON
3. In the 'body' field, enter new user credentials:
    {
        "username": "username",
        "email": "email",
        "password": "password"
    }
4. Send the request and the new user is successfully created
   
## How to create a new project
1. Navigate to the POST /dares/ request
2. In the 'body' tab, select JSON
3. In the 'body' field, enter new project details:
        {
            "title": "Dance all day Dare",
            "dare_description": "Dance all day from 7am til 7pm to support the Surf Lifesaver Foundation",
            "rules": "Must be willing to boogie all day",
            "goal": 5000,
            "image": "https://raw.githubusercontent.com/bel-lloyd/my-files/master/Dance-all-day.png",
            "is_open": true,
            "created_at": "2021-10-19T14:28:23.382748Z",
            "updated_at": "2021-10-20T14:28:23.382748Z",
            "date_for_dare": "2022-01-20T14:28:23.382748Z",
            "for_charity": "Queensland Surf Life Saving",
            "charity_url": "https://lifesaving.com.au/",
            "owner": 2
        }
4. Send the request and the dare is created successfully 
   
## Future Considerations

Much more to come! Stay tuned!