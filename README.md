# Twitter Sentiment Analysis

For training

```
  python twitt_training.py -p your_csv_path
```
For testing

```
  python twitt_prediction.py -t "your_sample_text"
```
<<<<<<< HEAD
![](pred.png)
<img src="pred.gif" width="600" height="400"/>
=======
![](pred.gif)
<img src="pred.gif" width="800" height="500"/>
>>>>>>> d903b2059dfcc2d61566d5704755abc440f7d144
* If you want to retrain according to your own twitter data set, columns called "twitts" and "sentiment" should be used..
* *(optional)* If you want to do hyperparameter tuning;
```
  python twitt_training.py -p your_csv_path -t True
```


