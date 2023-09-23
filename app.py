import pandas as pd
import openai
from fastapi import FastAPI, UploadFile, HTTPException, File
from pydantic import BaseModel

app = FastAPI()

def match(source: pd.Series, target: pd.DataFrame, api_key:str):
    try:
        names=['Date', 'EmployeeName', 'Plan', 'PolicyNumber', 'Premium']
        openai.api_key = api_key

        prompt = f"Which column from this {target.head(20)} is most similar to this {source} column. Give to this column one of these names {names} and send me the name and similar column from {target.head(20)}. Answer only in this format without any explanations - name, similar column "

        response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=3790,
        n=1,
        stop=None,  
        temperature=0.7,
        timeout=60
        )

        result = response.choices[0].text.strip().split()

        return [result[0].strip(), result[1].strip()]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OpenAI API request failed: {str(e)}")

class TableUpload(BaseModel):
    table_a: pd.DataFrame
    table_b: pd.DataFrame
    api_key: str

@app.post('/upload/')
async def upload(data: TableUpload):
    table_a = data.table_a
    table_b = data.table_b
    api_key = data.api_key
    
    if len(table_a.columns) != len(table_b.columns):
        raise HTTPException(status_code=400, detail="The number of columns in table_a and table_b must be the same.")
    
    result = pd.DataFrame()
    for col_a in table_a.columns:
        col_b_name, similar_col_name = match(table_a[col_a], table_b, api_key)
        result[col_a] = table_a[col_b_name] + table_b[similar_col_name]

    return {"status": 200, "table": result}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host='0.0.0.0', port=8000)