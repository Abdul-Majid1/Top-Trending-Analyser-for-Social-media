# CS201 - Data Structures - Social Media Analyser (Pairing heap)

This repository is a final project submission for the DS2 spring 2022 offering at Habib University.


## Introduction
Social Media forms a huge part of our entertainment and daily communication. Facebook, twitter and all other major social media apps have incorporated the top trending feature whose intention is to show the  top liked few posts at the time, understandably this can be done using a priority queue or heap whose priority is the number of likes. It is also true that most users are there on the top trending are interested only in the few of the very top messages making a priority heap with consecutive pop min operations even more relevant.  Since the likes frequently change and need to be updated constantly, the decrease key function will be a frequent operation in the structure and since the main strength of out pairing heap structure is its quick decrease key operation. It forms a perfect choice for our top trending back end implementation which we have used.


![toptrending](https://user-images.githubusercontent.com/77571253/169244806-b276d861-e556-4fee-8514-183f831f1c42.jpg)

