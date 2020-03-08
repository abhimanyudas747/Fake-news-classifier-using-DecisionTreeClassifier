# Fake-news-classifier-using-DecisionTreeClassifier
This is an API deployed on flask, which implemets a DecisionTreeClassifier to classify fake news.
The training dataset used here is the Fake News detection dataset available on kaggle. (URL given at the bottom)
The training dataset contains 4009 instances, with URL, body and heading. Each instance is labelled '1' for genuiene and '0' for fake.
The URLs column was dropped and the model is trained only on the heading and body columns. The IPython notebook is included in the repo, which was used for EDA and training of the model.

The initial preprocessing of the text was done using the nltk library and the feature matrix was generated using CountVecotrizer of Scikit-learn. 

The API is deployed on Flask, it takes the URL, heading and body as JSON request and responds with a JSON object predicting the instance.

To see it in action:
1. Clone this repo
2. Fire up Anaconda shell
3. Navigate to the repo directory
4. type in Anaconda shell : python "FakenewsclassifierAPI.py"
5. The flask server will run on localhost:5000
6. Send HTTP POST request to localhost:5000/predict
7. request should be a JSON object of format : {
                                                "URL" : "[url of the news]",
                                                "Heading" : "[Heading of the news]",
                                                "Body" : "[Body of the news]"
                                              }
8. You should get a response(JSON object) in the format : {
                                                          "Prediction" : "[Fake/Genuine]"
                                                        }
 
 Note: You can also use it over WAN by forwarding the port
 
 URL to training dataset : https://www.kaggle.com/jruvika/fake-news-detection
 The training of the classifier and the preprocessing of the dataset is done on a Kaggle IPython notebook, which is included here. (Since, my potato pc can't handle a 147 MiB dataset)
 
 Thanks for checking out this project, this is my first on Github :D
