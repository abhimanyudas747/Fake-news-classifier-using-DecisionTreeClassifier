# Fake-news-classifier-using-DecisionTreeClassifier
This is an API deployed on flask, which implemets a DecisionTreeClassifier to classify fake news.
The training dataset contains [] instances, with URL, body and heading. Each instance is labelled '1' for genuiene and '0' for fake.
The URLs column was dropped and the model is trained only on the heading and body columns. The IPython notebook is included in the repo, which was used for EDA and training of the model.

The initial preprocessing of the text was done using the nltk library and the feature matrix was generated using CountVecotrizer of Scikit-learn. 

The API is deployed on Flask, it takes the URL, heading and body as JSON request and responds with a JSON object predicting the instance.

To see it in action:
*Fire up Anaconda shell
*Navigate to the directory where the "Fake news classifier API.py" is present
*type in Anaconda shell : python "Fake news classifier API.py"
*The flask server will run on localhost:5000
*Send HTTP POST request to localhost:5000/predict
* request should be a JSON object of format : {
                                                "URL" : "[url of the news]"
                                                "Heading" : "[Heading of the news]"
                                                "Body" : "[Body of the news]"
                                              }
*You should get a response(JSON object) in the format : {
                                                          "Prediction" : "[Fake/Genuine]"
                                                        }
 
 Note: You can also use it over WAN by forwarding the port
 
 Thanks for checking out this project, this is my first on Github :D
