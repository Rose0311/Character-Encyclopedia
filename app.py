from flask import Flask,render_template,url_for,redirect,request
import requests

app = Flask(__name__)
API_BASE_URL = "https://potterapi-fedeperin.vercel.app/en/characters"


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def search():
    if request.method == 'POST':
       search_c=request.form['search-bar']
       response = requests.get(f"{API_BASE_URL}?search={search_c}")
       if response.status_code==200:
           characters=response.json()
           if characters:
               return render_template('results.html', characters=characters[0])
           else:
               return render_template('results.html', error="No such character is found in the API.")
       else:
        return render_template('results.html', error="Failed to fetch data from the API.")

@app.route('/random_c',methods=['POST'])      
def random_c():
    if request.method == 'POST':
        response=requests.get(f"{API_BASE_URL}/random")    
        if response.status_code==200:
           characters=response.json()
           if characters:
               return render_template('results.html', characters=characters)
           else:
               return render_template('results.html', error="No such character is found in the API.")
        else:
            return render_template('results.html', error="Failed to fetch data from the API.")    
       






if __name__ == '__main__':
    app.run(debug=True)
