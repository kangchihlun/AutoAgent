# autoagent_db_query.py
#from langchain.llms import OpenAI
from langchain_community.llms import OpenAI
from langchain.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()  # This loads the variables from .env



class ChinookQueryAgent:
    def __init__(self):
        # 設置資料庫連接
        self.engine = create_engine('sqlite:///./data/chinook.db')
        self.db = SQLDatabase(self.engine)
        
        # 初始化 LLM 模型
        self.llm = OpenAI(temperature=0, verbose=True)
        
        # 建立查詢鏈
        self.db_chain = SQLDatabaseChain.from_llm(
            self.llm, 
            self.db, 
            verbose=True,
            use_query_checker=True
        )

    def query(self, natural_language):
        return self.db_chain.run(natural_language)

# AutoAgent 集成接口
if __name__ == "__main__":
    agent = ChinookQueryAgent()
    result = agent.query("how many customer bought the track 'Restless and Wild'")
    print(f"Query Result: {result}")
