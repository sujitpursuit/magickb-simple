
import os

from  llama_index.core import SimpleDirectoryReader,VectorStoreIndex



from flask import Flask,  request


openai_api_key=os.environ['OPENAI_API_KEY']


docs=SimpleDirectoryReader("kbdata").load_data()
index=VectorStoreIndex.from_documents(docs)
#Function to query
def query_kb(index_i,query_str):
    """Search Knowledge Base or KB"""

    query_engine=index_i.as_query_engine()
    
    response= query_engine.query(query_str)
    responseAsText = str(response).strip()
    
    return responseAsText






app = Flask(__name__)
app.static_folder = 'static'
@app.route("/")
def home():
    return "KB Seatch API "
@app.route("/kb")
def get_bot_response():
  
    user_prompt = request.args.get('prompt')
    user_query = f'Get the resolution for the Issue or Problem: {user_prompt} and then Compose the response in two parts Issue:   Resolution: ' 
    result = query_kb(index,user_query)
    return result
if __name__ == "__main__":
    app.run()