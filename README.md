# **TOPIC - SOCIAL MEDIA WEB APP**

## **Introduction**
Our mini project is based on the topic Social Media Web App. This Python project aims at connecting different people around the world together to share thoughts, morals or pictures. Django Web App framework of Python is used to create this project.\
Dynamic web app using Django, Django-REST-Framework. The technologies used were Django, Django-REST-Framework, HTML5, CSS3, JavaScript, jQuery, AJAX, JSON, Bootstrap-4, MySQL/SQLite3/any type of SQL with the help of Django. The top functionalities are Search without reload via AJAX and JSON, check if username/email is already registered and notify before as well as after submitting. Follow/Unfollow users without reload via AJAX, Create/Update/Delete Posts without reload via AJAX, JSON. API's were created for all AJAX/JSON functionalities.

## **Software used**
* Python v3.7.2
* PyCharm Community (Updated)
* Visual Studio Code (Updated)

## **Packages used**
* Django v2.1.5
* Django AllAuth v0.38.0
* Django Crispy Forms v1.7.2
* Django REST Framework v3.9.1
* Pillow v5.4.1

## **Code**
1. Create a virtual Environment for the Project with PyCharm
2. Activate the virtual environment
3. Install all necessary packages via pip command.
4. Create Django Project with **django-admin startproject socialmedia** command.
5. Rename socialmedia to src and change directory in cmd to src and create hashtags, posts, user_registration using **python manage.py startapp hashtags** ; **python manage.py startapp posts** ; **python manage.py startapp user_registration** commands.
6. Add all apps in the list of INSTALLED_APPS, along with social media apps, Django crispy forms and Django REST Framework in settings.py file under socialmedia folder
7. Configure ALLOWED_HOSTS; templates directory; AllAuth settings from AllAuth Documentation; Media URL and ROOT; Static URL and ROOT; Django crispy form template and necessary settings for sending Email in settings.py file under socialmedia folder.  
8. We created a superuser by **python manage.py createsuperuser** command. And ran the server with **python manage.py runserver** command.
9. Go to 127.0.0.1:8000 in the browser, it’ll redirect you to the login page at [/accounts/login/](http://127.0.0.1:8000/accounts/login/) , user should enter his username and password associated with his account, else user can login/signup with his social account. If user doesn’t have an account the user can create an account by going to the sign-up page at [/accounts/signup/](http://127.0.0.1:8000/accounts/signup/) .
10. After Sign up, user is sent a mail to his entered Email address for verification of his Email. After verification of users email, user is allowed to login into the web app.
11. If user forgot his password, then user can ask for a password reset mail at Forgot password link on the login page and enter the primary Email address associated with his account to get the password reset mail.
12. After login, user can access his Settings, Profile page and Sign-Out under his profile picture at the topmost right corner. If logged in user is a super user, then Admin Panel is displayed.
13. User can update his First name, Last name in the General Tab; user can update his Location(optional) and Profile Image(optional) in the Profile Tab; User can add or remove email address or change primary email address in the Account Tab. User can change his password in the Change Password Tab (Displayed if password is set); User can set password for his account in the Set Password Tab (Displayed if password is not set and ser uses other social accounts to login); User can connect or disconnect other social accounts with his account in the Connections Tab; User can delete his account with all his info and posts in the Delete Account Tab. 
14. User can head towards the Posts link in the navbar to check his posts and the posts of the users he is following.
15. User can type a message in the message box(not optional) of minimum 500 characters and choose an image(optional) for that post and click on the Post button. The post gets added to the top in the post feed.
16. User can add #hashtags and @username in the post.
17. User can click on @username in post to view that users profile.
18. User can click on #hashtags, to view all related #hashtags from all users.
19. User can update the post by clicking on the 3 horizontal dots at the topmost right corner of the post and click on Update, a pop-up box will appear, user and update the content(optional) or the image(optional) and click on Update button.
20. User can delete the post by clicking on the 3 horizontal dots at the topmost right corner of the post and click on Delete, a pop-up box will appear, user has to click on the Delete button to delete the post.
21. User can click on the time created/updated and it’ll show that post on a new page.
22. User can click on the owner of the post to view his profile page.
23. At a time only 5 Posts are fetched, to view more posts, user has to click on the Load more posts option to fetch next five posts and so on.
24. User can click on the like button, to like or dislike a post and the count of likes will increase or decrease accordingly.
25. User can search for any specific post or user on the Search box available on the navbar and it’ll filter within seconds without pressing enter key.
26. User can view his profile by moving to the topmost right corner and clicking on My Profile under his profile picture.
27. User can view all his posted content and photos on his profile page.
28. User can view his followers usernames by clicking on Followers and follow/unfollow other users.
29. User can remove his followers by clicking on the cross(X) symbol, in the Followers pop-up.
30. User can view which users he is following by clicking on Following and follow/unfollow other users.
31. Users can follow or unfollow other users, without page reload.
32. Follow button is present for all users, except the current user logged in.
33. If feed is empty, then No Posts currently found is displayed.

## **Results**
This mini project has the functionalities of a user Sign-up with Email account verification, sent via mail. User can Sign-up using other Social media networks like Google, Github, BitBucket and Twitter and select a username. If user has not verified the Email, then user is not allowed to login or use the account. After user has verified the Email, the user is allowed to login into the account. User can also login from other Social Networks connected to the users account. User can ask for a password reset mail, incase if user has forgot the password.
User can go in the settings page after login and update his name, location, profile image, connect or remove emails associated with the account and verify those Email accounts with a verification mail; make an email primary for sending the password reset mail; connect or disconnect other Social media networks with the account; delete user account with all it’s activities; change password or set password(if social login is used and password is not set). Users can post text content, along with image on this web app; users can update the text content or image in the post; users can delete the post; users can view the post on a separate page. Users can view the how many minutes/hours/days/weeks/months ago the post was created or updated User can view only the post feeds of the users, whom the user follows, along with the current user post feeds. User can like and unlike a post feed. Users can follow and unfollow other users; users can view others profile and view that user followers and whom that user is following. User can search for a all types of post feed in the search bar, regardless of whom the current user is following.


## **Snapshots**
**1. Sign-Up page (user-dms24):**
![image alt text](docs/images/image_0.png)

**2. Email sent for verification after Sign-Up or if user has not yet verified his Email (user-dms24):**
![image alt text](docs/images/image_1.png)

**3. Verification Email Sent from email configured in settings.py file under socialmedia folder (user-dms24).**
![image alt text](docs/images/image_2.png)

**4. Confirm Email address page from verification link (user-dms24):**
![image alt text](docs/images/image_3.png)

**5. Sign-In Page (user-dms24):**
![image alt text](docs/images/image_4.png)

**6. Forgot Password page (user-dms24):**
![image alt text](docs/images/image_5.png)

**7. Password Reset mail sent (user-dms24):**
![image alt text](docs/images/image_6.png)

**8. Password Reset mail received (user-dms24):**
![image alt text](docs/images/image_7.png)

**9. Changing password with password reset link (user-dms24):**
![image alt text](docs/images/image_8.png)

**10. Authenticating Google account without any Web app (user-dms):**
![image alt text](docs/images/image_9.png)

**11. Signing up for a Web app account after authenticating with Google account (user-dms):**
![image alt text](docs/images/image_10.png)

**12. Set Password, if user uses other social media to sign-in into the Web app (user-dms):**
![image alt text](docs/images/image_11.png)

**13. Admin Panel access displayed to super-users only (user-admin):**
![image alt text](docs/images/image_12.png)

**14. Post Feed page (user-dms24):**
![image alt text](docs/images/image_13.png)

**15. User profile page (user-dms24):**
![image alt text](docs/images/image_14.png)

**16. General Tab Page (user-dms24):**
![image alt text](docs/images/image_15.png)

**17. Profile Tab Page (user-dms24):**
![image alt text](docs/images/image_16.png)

**18. Account Tab Page (user-dms24):**
![image alt text](docs/images/image_17.png)

**19. Change Password Tab Page (user-dms24):**
![image alt text](docs/images/image_18.png)

**20. Connections Tab Page (user-dms24):**
![image alt text](docs/images/image_19.png)

**21. Adding and authenticating Google Account with an already existing Web app account (user-dms24):**
![image alt text](docs/images/image_20.png)

**22. Connection added to an already existing Google Account (user-dms24):**
![image alt text](docs/images/image_21.png)

**23. Delete Account Tab Page (user-dms24):**
![image alt text](docs/images/image_22.png)

**24. Creating a Post with #hashtags and @username and minimum 500 characters in content of Post (user-dms24):**
![image alt text](docs/images/image_23.png)

**25. Page with all #hello (user-dms24):**
![image alt text](docs/images/image_24.png)

**26. Liking post and viewing post on separate page by clicking on the time the post was created/updated (user-dms24):**
![image alt text](docs/images/image_25.png)

**27. User profile with users post (user-dms24):**
![image alt text](docs/images/image_26.png)

**28. Following pop-up (user-dms24):**
![image alt text](docs/images/image_27.png)

**29. Followers pop-up (user-dms24):**
![image alt text](docs/images/image_28.png)

**30. After removing a follower dms, by clicking on cross(X) button and following admin (user-dms24):**
![image alt text](docs/images/image_29.png)

**31. Search for the word admin in posts and users (user-dms24):**
![image alt text](docs/images/image_30.png)

**32. Post with options to update and delete (user-dms24):**
![image alt text](docs/images/image_31.png)

**33. Update Post (user-dms24):**
![image alt text](docs/images/image_32.png)

**34. Delete Post (user-dms24):**
![image alt text](docs/images/image_33.png)

**35. Crop and update/upload Profile Image (user-dms24):**
![image alt text](docs/images/image_34.png)

**36. Sign-out page (user-dms24):**
![image alt text](docs/images/image_35.png)

## **Conclusion**
This mini project can help to connect users from all around the globe to share their thoughts and pictures. In this project we implemented the concepts of functions, classes in Python; models, forms, generic views, admin, urls, mixins in Django; serializers, pagination, API view in Django REST API; HTML, CSS, Javascript as frontend and AJAX using Javascript to communicate with the API in backend of the web app.

## **Future Scope**
This mini project can be deployed and hosted from Heroku server, to help connect users from all around the globe to share their thoughts and pictures. Users can meet new people and learn the way of communicating with others. Users can share their knowledge and skills on this web app.

## **References**
* DR.NAGESHWAR RAO – "Core Python Programming"
* [www.tutorialspoint.com/python](http://www.tutorialspoint.com/python)
* [www.geeksforgeeks.com/python3](http://www.geeksforgeeks.com/python3)
* CodingEntrepreneurs [https://www.youtube.com/channel/UCWEHue8kksIaktO8KTTN_zg](https://www.youtube.com/channel/UCWEHue8kksIaktO8KTTN_zg)
* Max Goodridge [https://www.youtube.com/channel/UCAx4nmhI7S1RcPiaG-Uw0tg](https://www.youtube.com/channel/UCAx4nmhI7S1RcPiaG-Uw0tg)
* JustDjango [https://www.youtube.com/channel/UCRM1gWNTDx0SHIqUJygD-kQ](https://www.youtube.com/channel/UCRM1gWNTDx0SHIqUJygD-kQ)
* The Dumbfounds [https://www.youtube.com/channel/UC33uwXXDrI5TxG4IXnjS28g](https://www.youtube.com/channel/UC33uwXXDrI5TxG4IXnjS28g)
* [https://simpleisbetterthancomplex.com/](https://simpleisbetterthancomplex.com/)
* [https://stackoverflow.com/](https://stackoverflow.com/)

