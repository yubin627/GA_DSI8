import flask
from retrieval import load_feat_db, dump_single_feature_npy, naive_query
from file import Anno, Eval
import random
import re

#----- CONFIG -----#

# set static url path
app = flask.Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True
# first part of path of images hosted by aws
static_path = "https://capstone-deepfashion.s3.us-east-2.amazonaws.com/"


#-------- FEATURES DATA -----------#

deep_feats, color_feats, labels = load_feat_db()

#----- ROUTES -----#

@app.route("/")
def random_query_sample(batch=1): 
	'''Get an image from the test dataset, upper wear only'''
	ann = Anno(is_train=False)
	paths = []
	for i in range(batch):
		ran = random.randrange(0, len(ann))
		paths.append(ann.loc[ran]['image_name'])

	selected_path = static_path + paths[0]
	return flask.render_template('query_styling.html',selected_path=selected_path) 

@app.route("/input_page")
def send_form():
	'''Back up input page to take file path string as input'''
	return flask.render_template('input_page.html')

@app.route('/results', methods=['POST', 'GET'])
def result():
	'''Gets top 4 similar images based on input from the post method'''
	if flask.request.method == 'POST':
		RESULTS_ARRAY = []
		inputs = flask.request.form
		image_path = inputs['imagesrc'].replace(static_path,'')

	
		f = dump_single_feature_npy(image_path)

		if any(list(map(lambda x: x is None, f))):
			return flask.jsonify("Input feature is None")
			exit()

		result = naive_query(f, deep_feats, color_feats, labels, 4)

		# loop over the results, displaying the score and image name
		for (path, score) in result:
			RESULTS_ARRAY.append(
				{"image": str(static_path+path), "score": str("{:.2f}%".format(float(1/(float(score) + 1)*100))), \
                 "title": re.search('img\/(.*)\/',path).group(0)})		

		return flask.render_template('output_styling.html',RESULTS_ARRAY=RESULTS_ARRAY)

		
#----- MAIN SENTINEL -----#

if __name__ == "__main__":
    app.run()