# Multimodal-Biometric-System
<a name="br1"></a> 

**Indian Institute of Information Technology Design and**

**Manufacturing, Kancheepuram, Melakottaiyur,**

**Chennai 600127**

**Multimodal Biometrics using Gait and Ear**

**as biometric features**

K Sai Dinesh (CS20B1122), Lokesh Reddy (CS20B1128), Rudhra (CS20B1104)

Department of Computer Science and Engineering

Indian Institute of Information Technology, Design and Manufacturing,

Kancheepuram

**ABSTRACT**

Multimodal biometrics using gait and ear features combine two different biometric

modalities to improve the accuracy and reliability of biometric identiﬁcation

systems. Gait recognition involves analyzing a person's walking pattern, while ear

biometrics involves analyzing the unique shape and features of a person's ear.

Recent research studies have shown that by combining these two modalities, a

more robust and accurate identiﬁcation system can be created rather than a

standalone biometric system, as it is less likely that both gait and ear features will

be affected by external factors such as clothing or lighting. This approach has

potential applications in various domains, including security, healthcare, and sports.

In this project, we shall attempt to design a multimodal biometric system using gait

and ear features and also compare its performance to standalone gait recognition

system & ear biometric system respectively and go on to increase the accuracy of

the multimodal biometric system. The database for this project was done from our

side by “taking the prior permission” of the subjects in the video.

**I: INTRODUCTION**

Let’s look at gait and ear biometrics on an individual note and look at the techniques

used in recent times to perform individual identiﬁcation. We shall also look at the

math behind the feature extraction and representation of the biometric.

Gait biometric involves using the person’s walking style as the differentiating factor

and recognising him/her based on certain factors associated with it. Medical



<a name="br2"></a> 

studies have shown that the Gait pattern is unique to a person and is suﬃcient to

identify the person in normal circumstances. The factors associated with Gait can

range from the positions of the various body parts, the paths traced by different

joints of the hand and leg of the person in consideration to the swing and stance

patterns of the person’s hand and leg. These features can be extracted using

specialized cameras and sensors to determine the body structure, muscle strength,

gait line and neurological patterns. These features are then used to create a

biometric template that can be used to identify the individual in future instances.

However, there are also some challenges associated with gait biometric, such as

variations due to clothing and footwear, different walking speeds, and environmental

factors. Despite these challenges, gait biometric has shown promising results in

research studies and has the potential to become an important tool for biometric

identiﬁcation in various domains.

Here, we would be using a video of the person walking as the input and extract the

phases of the gait cycle which are shown below:

There are a couple of methods to get the features from the gait cycle phases from

the video which are discussed in the next section.

Ear biometrics involves detecting the side face of the person and then his/her ear

,later we will extract features like ear contours. For the face we can start with the

Haar cascade algorithm but for the ear detection we can’t get an ear by just using

the Haar cascade So, we have used edge detection and template matching method

like mentioned below. This gave us a very good accuracy in ﬁnding the ear.



<a name="br3"></a> 

Later after getting the ear segmented from the face we have extracted its ear

contours and used them for identifying the person.

**II: METHODS FOR FEATURE EXTRACTION**

For extracting gait features, there are 2 methods to do so. They are:

**1. Using Pose Estimation:**

This approach to get gait features involves the extraction of keypoints from

the image of a single phase of the gait cycle of the person. Keypoint

extraction involves identifying speciﬁc points on a person's body that are

critical to their gait. These key points can include the position of the head,

shoulders, hips, knees, and ankles. By analyzing the movement and position

of these key points over time, it is possible to create a unique "gait signature"

for each individual. Example is shown below:



<a name="br4"></a> 

Once the key points have been extracted, they can be used as input to a

machine learning algorithm to classify the gait pattern and identify the

person. This can be done using techniques such as deep neural networks,

support vector machines, or decision trees.

Gait recognition using pose estimation has several advantages over other

biometric identiﬁcation techniques. For example, it can be done at a distance,

without the need for physical contact or the subject's cooperation. It is also

less intrusive than techniques such as ﬁngerprinting or iris scanning.

**Disadvantages:** Computationally intensive & takes a lot of time to get the

features on a local system. Susceptible to external objects like bags , coats, etc.

**2. Using Gait Energy Image (GEI):**

In this method of feature extraction, we use the phases of the gait cycle from

the video to get the “silhouettes” of the phase image. We then take the

average/weighted average of these silhouettes and thus obtain the Gait

Energy Image (GEI) of the person in consideration. The purpose of

silhouettes is that it’s invariant of background noise and other environmental

factors and removes all such noise. Also, it is unaffected by the external



<a name="br5"></a> 

objects like bags, coats, etc. and also its space eﬃcient in terms of database

template storage.

Formula for Gait Energy Image

Extraction.

Gait Energy Image (GEI)

For extracting ear features, we ﬁnd the ear contours using the following method:

**Using Ear Contours:**

In this method we start with edge detection and thresholding for contour Detection

and will do the Binarization.

Then will calculate the centroid and do the normalization of coordinates. Later for

the feature vector we will follow below steps:

1\. we create a set of circles with the center in the centroid

2\. number of circles Nr is ﬁxed and unchangeable

3\. we create circles in such a manner that the corresponding radiuses are

α pixels longer from the previous radius

4\. since each circle is crossed by the contour image pixels we count the number

of intersection pixels lr

5\. next we calculate all the distances d between neighboring pixels, we

proceed in the counterclockwise direction

6\. we build the feature vector that consists of all the radiuses with the



<a name="br6"></a> 

corresponding number of pixels belonging to each radius and with the sum

of all the distances between those pixels ∑d

**III: PROPOSED METHODOLOGY:**

In this project, we shall be using the concept of Gait Energy Image (GEI) for gait

feature extraction and contour boundaries for ear feature extraction. We then use

the “SIFT detector” to get feature matches and identify the person using the

“Minimum Distance” classiﬁcation technique. The detailed procedure is given below:

**(i) Gait Classiﬁcation using GEI:**

● First, we shall take the video of the person’s walking style as input.

● From this video, we shall extract the 8 phases of the gait cycle (as shown in

the images of the feature extraction section of this doc).

● We then obtain the silhouettes of these 8 individual phases using

“*deeplabv3\_resnet101*” which is a deep learning and semantic segmentation

algorithm used to extract the contours of the person’s body.

● Using the output of the above model, we shall binarize the image, which in

turn gives the silhouette of the image.

● We then center the silhouette images (8 images) before performing the

averaging operation.

● Finally, we take the mean of the 8 silhouettes to obtain the ﬁnal gait energy

image (GEI) and store this template in the database for further use.

*(Example Template for a test subject we considered)*



<a name="br7"></a> 

For Classiﬁcation, we shall get the feature matches using the SIFT detector and

calculate the distance from database templates using these matches as the criteria.

Finally, we assign the class as the template class with the minimum distance from

the test subject’s GEI. We store the distances of the test subject’s GEI from the

Database templates in an array for further use in the multimodal system.

**(ii) Ear Detection using Ear Contours:**

● First, we shall start with detecting the side face of the person using Haar

cascade algorithm

● Then we shall do the ear segmentation by edge detection and template

matching.

● After Segmenting the ear from the face, We shall get the feature vector by

ﬁnding the contours and using centroid for feature representation as

mentioned in above Ear contours method.

For Classiﬁcation, we shall get the feature matches using the SIFT detector and

calculate the distance from database templates using these matches as the criteria.

Finally, we assign the class as the template class with the minimum distance from

the test subject’s feature vector. We store the distances of the test subject’s feature

vector from the Database templates in an array for further use in the multimodal

system.

**(iii) Combining the two biometrics:**

Now, after we acquire the gait and ear distance arrays, we shall normalize the

distance values in these arrays as the gait array has values in the 200-300 range

whereas the ear distances are in the range 20,000-30,000. Thus we see that the ear

feature is dominating over the gait feature and thus must be normalized to nullify

this effect on the biometric system.

Now, we combine the two distances by assigning a speciﬁc weight value to these

distance values. The formula we used is:

**Combined\_distance = α \* (Gait Distance) + β \* (Ear Distance)**

Based on this distance metric, we shall classify the subject depending on its

minimum distance from the stored database templates. This process is carried out

for every test subject and the corresponding class labels are obtained to calculate

the accuracy score.



<a name="br8"></a> 

**IV: RESULTS:**

**Biometric Considered**

**Accuracy Score**

45\.45%

Gait Classiﬁcation System (GEI)

Gait Classiﬁcation System (Hamming Distance)

Ear Classiﬁcation System (Ear Contours)

Multimodal (Gait + Ear)

41\.67%

41\.67%

58\.33%

**V: CONCLUSION:**

Thus, we conclude that the multimodal biometric system performs better than the

individual biometric systems of gait or ear. This system can ﬁnd its applications in

person identiﬁcation through CCTV cameras, pedestrian detection through dash

cams, etc. This is a non-invasive system and works for the subjects at a distance

from the camera. Also, it is robust to artifacts on the body like bags, coats, etc.

In the future, we can make an advanced implementation of this system by fusing it

with other biometric traits like face, hand geometry, etc. in order to improve its

reliability and security. Also, there is a huge scope in improving the accuracy score

of this system by using higher resolution cameras as in our case, even in lower

resolution conditions, we could achieve a decent accuracy of more than 50%. Also,

we can work on making the system robust to external occlusions like tables, walls,

etc. which affect the capturing of gait patterns of the persons.

Thus, this project can serve as an example for many other multimodal systems to

come up in the future and develop more robust and secure identiﬁcation systems.

**REFERENCES:**

1\. [Gait](https://www.hindawi.com/journals/ijo/2015/763908/)[ ](https://www.hindawi.com/journals/ijo/2015/763908/)[Recognition](https://www.hindawi.com/journals/ijo/2015/763908/)[ ](https://www.hindawi.com/journals/ijo/2015/763908/)[Using](https://www.hindawi.com/journals/ijo/2015/763908/)[ ](https://www.hindawi.com/journals/ijo/2015/763908/)[GEI](https://www.hindawi.com/journals/ijo/2015/763908/)[ ](https://www.hindawi.com/journals/ijo/2015/763908/)[and](https://www.hindawi.com/journals/ijo/2015/763908/)[ ](https://www.hindawi.com/journals/ijo/2015/763908/)[AFDEI](https://www.hindawi.com/journals/ijo/2015/763908/)[ ](https://www.hindawi.com/journals/ijo/2015/763908/)[(hindawi.com)](https://www.hindawi.com/journals/ijo/2015/763908/)

2\. <https://ietresearch.onlinelibrary.wiley.com/doi/10.1049/bme2.12103>

3\. [https://www.vislab.ucr.edu/PUBLICATIONS/pubs/Journal%20and%20Confere](https://www.vislab.ucr.edu/PUBLICATIONS/pubs/Journal%20and%20Conference%20Papers/after10-1-1997/Conference/2004/Human%20Ear%20Detection%20from%20Side%20Face04.pdf)

[nce%20Papers/after10-1-1997/Conference/2004/Human%20Ear%20Detectio](https://www.vislab.ucr.edu/PUBLICATIONS/pubs/Journal%20and%20Conference%20Papers/after10-1-1997/Conference/2004/Human%20Ear%20Detection%20from%20Side%20Face04.pdf)

[n%20from%20Side%20Face04.pdf](https://www.vislab.ucr.edu/PUBLICATIONS/pubs/Journal%20and%20Conference%20Papers/after10-1-1997/Conference/2004/Human%20Ear%20Detection%20from%20Side%20Face04.pdf)

4\. <https://elcvia.cvc.uab.cat/article/view/v5-n3-choras/104>


