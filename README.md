# CS201 - Data Structures - Social Media Analyser (Pairing heap)

This repository is a final project submission for the DS2 spring 2022 offering at Habib University.


## Introduction
Social Media forms a huge part of our entertainment and daily communication. Facebook, twitter and all other major social media apps have incorporated the top trending feature whose intention is to show the  top liked few posts at the time, understandably this can be done using a priority queue or heap whose priority is the number of likes. It is also true that most users are there on the top trending are interested only in the few of the very top messages making a priority heap with consecutive pop min operations even more relevant.  Since the likes frequently change and need to be updated constantly, the decrease key function will be a frequent operation in the structure and since the main strength of out pairing heap structure is its quick decrease key operation. It forms a perfect choice for our top trending back end implementation which we have used.


![toptrending](https://user-images.githubusercontent.com/77571253/169244806-b276d861-e556-4fee-8514-183f831f1c42.jpg)

## Flow and App Structure 
On running the tkinter application, our social media app opens where you can either login from your ID or register from a new ID using the register ID, the app itself is interest based so that apart from your username and password, you have to choose from a list of interests, the rationale being that a user will be able to see only posts of his own interest once he logins.

<p align="center">
  <img src="Login page.png" +/>
</p>

<p align="center">
  <img src="registerpage.png" +/>
</p>



these posts will be in order of time posted with most recent on top. The user can post in any category including his own and if he posts in his own category then he can see in real time the post appear on top, if not the post is relayed to other users who match the category of interest. Each user has the facility of liking posts also, on each insert the post inserted into our pairing heap and the decrease function is called on each like , this allows our heap to be updated ,clicking on the top trending button will pop min from the heap and show you the top most liked posts, you can click on the next and previous buttons 

